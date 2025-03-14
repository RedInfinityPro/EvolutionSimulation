
import random
from ursina import *
def update():
    global number
    # move cam around
    if held_keys['w']:
        camera.y += 10
    if held_keys['s']:
        camera.y -= 10
    if held_keys['d']:
        camera.x += 10
    if held_keys['a']:
        camera.x -= 10
    if held_keys['e']:
        camera.z -= 10
    if held_keys['r']:
        camera.z += 10
    # global
    global birth_chance, death_chance
    # kill bot
    random_death = random.randint(0, death_chance)
    # random death
    if random_death > 0:
        try:
            kill = random.choice(entity_list)
            destroy(kill)
            number -= 1
            entity_list.remove(kill)
        # if an error occurs
        except IndexError:
            pass
        except ValueError:
            pass
    # make new bot
    hit_info = bot.intersects()
    if hit_info.hit:
        if hit_info.entity in entity_list:
            # birth chance
            random_birth = random.randint(0,birth_chance)
            if random_birth > 0:
                # the new bot will need to find the color values to simulate evolution
                # values
                r, g, b = 0, 0, 0
                # red
                if hit_info.entity.R > max_list[number - 1][0]:
                    r = random.randint(max_list[number - 1][0],hit_info.entity.R)
                elif hit_info.entity.R < max_list[number - 1][0]:
                    r = random.randint(hit_info.entity.R,max_list[number - 1][0])
                else:
                    random_color = random.randint(0, 1)
                    if random_color == 0:
                        r = hit_info.entity.R
                    else:
                        r = max_list[number - 1][1]
                # green
                if hit_info.entity.G > max_list[number - 1][1]:
                    g = random.randint(max_list[number - 1][1],hit_info.entity.G)
                elif hit_info.entity.G < max_list[number - 1][1]:
                    g = random.randint(hit_info.entity.G,max_list[number - 1][1])
                else:
                    random_color = random.randint(0,1)
                    if random_color == 0:
                        g = hit_info.entity.G
                    else:
                        g = max_list[number - 1][1]
                # blue
                if hit_info.entity.B > max_list[number - 1][2]:
                    b = random.randint(max_list[number - 1][2],hit_info.entity.B)
                elif hit_info.entity.B < max_list[number - 1][2]:
                    b = random.randint(hit_info.entity.B,max_list[number - 1][2])
                else:
                    random_color = random.randint(0, 1)
                    if random_color == 0:
                        b = hit_info.entity.B
                    else:
                        b = max_list[number - 1][1]
                # make new bot
                new_bot = Bot(R=r, G=g, B=b,position = (hit_info.entity.x,hit_info.entity.y))
                number += 1
                entity_list.append(new_bot)
                max_list.append([r, g, b])
    # the random movements for each bot
    for bot_e in entity_list:
        move_random_pos = random.randint(1,4)
        if move_random_pos == 1:
            bot_e.x += 1
        elif move_random_pos == 2:
            bot_e.x -= 1
        elif move_random_pos == 3:
            bot_e.y -= 1
        elif move_random_pos == 4:
            bot_e.y += 1


app = Ursina()
# Birth rate slider
def Birth_rate():
    global birth_chance
    birth_chance = round(birth_rate.value)

# Death rate slider
def Death_rate():
    global death_chance
    death_chance = round(death_rate.value)

birth_chance = 10
birth_rate = Slider(0,99, default= birth_chance, on_value_changed = Birth_rate,y = -0.4,x = -0.3,dynamic = True,text = 'birth Chance')

death_chance = 0
death_rate = Slider(0,99, default = death_chance, on_value_changed = Death_rate,y = -0.45,x = -0.3,dynamic = True,text = 'death Chance')

# this part makes the bot
number = 0
max_list = []
class Bot(Button): # by allowing the shape to be a button it allows the text to be visible
    def __init__(self,R,G,B,position=(0,0)):
        super().__init__()
        global max_list,number
        self.parent = scene
        # the model, texture, collider can be changed respectively
        self.model = 'sphere'
        self.texture = 'white_cube'
        self.collider = 'sphere'
        self.scale = 5 # this scale allows the text to be shown on the shape
        self.position = position
        # this code make the first two bots
        if number < 2:
            self.R = R
            self.G = G
            self.B = B
        # this finds out what color in the evolution process the bot is at
        else:
            self.R = random.randint(0,max_list[0][0])
            self.G = random.randint(0,max_list[0][1])
            self.B = random.randint(0,max_list[0][2])
        self.color = color.rgb(self.R,self.G,self.B)
        # this displays text color values
        self.text = 'R {}  G {}  B {}'.format(self.R,self.G,self.B)
        self.text_origin = (0,0,-1)

# this allows the bots to be shown on the screen
entity_list = []
for x in range(2):
    r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    max_list.append([r, g, b])
    bot = Bot(R = r, G = g,B = b,position=(random.randint(-number,number),random.randint(-number,number)))
    entity_list.append(bot)
    number += 1





if __name__ == '__main__':
    app.run()
