import random
import ursina
from ursina import *

def update():
    ursina.SmoothFollow = True
    for entity in bacteria_list:
        if random.uniform(0,100) <= entity.reproduction_chance:
            bacteria = Bacteria(position=(random.uniform(1 - entity.x,entity.x + 1), random.uniform(1 - entity.y,entity.y + 1), -2))
            bacteria_list.append(bacteria)

app = Ursina()
genetic_code_letters = ['A','T','G','C']
R,B,G = 0,0,0
class Bacteria(Button):
    def __init__(self,position = (0,0,0)):
        super().__init__()
        global R,B,G
        R, B, G = 0, 0, 0
        self.parent = scene
        self.position = position
        self.model = 'cube'
        self.scale = 0.1
        # DNA
        self.DNA = []
        for x in range(150):
            self.DNA.append(random.choice(genetic_code_letters))
        for i in self.DNA:
            if i == 'A':
                R += 1
            if i == 'T':
                G += 1
            if i == 'G':
                B += 1
        # color
        self.color = color.rgb(R,G,B)
        # producing chance
        number_cs = []
        for ii in self.DNA:
            if ii == 'C':
                number_cs.append(ii)
        self.reproduction_chance = (len(number_cs) / len(self.DNA)) * 100

    def update(self):
        hit_info = self.intersects()
        if self.hit:
            if random.randint(0,3) == 0:
                self.y += 1
            elif random.randint(0,3) == 1:
                self.y -= 1
            elif random.randint(0,3) == 2:
                self.x += 1
            elif random.randint(0,3) == 3:
                self.x -= 1

bacteria_list = []
for i in range(1):
    bacteria = Bacteria(position = (0,0,-1))
    bacteria_list.append(bacteria)

app.run()
