#!/usr/bin/python3

import random

class Magic():
      def __init__(self, level):
            elements = ["Fire", "Ice", "Lightning", "Light", "Dark"]
            types = ["Ball", "Explosion", "Bolt", "Pulse", "Vortex"]
            
            pick = random.randint(0, 4)
            self.element = elements[pick]

            pick = random.randint(0, 4)
            self.type = types[pick]

            self.spell = self.element + " " + self.type

            if level == 0 or level == 1:
                  self.damage = 1
            else:
                  if level %2 == 1:
                        level += 1
                  self.damage = random.randint((level/2), level)


      def get_spell(self):
            return self.spell


      def get_damage(self):
            return self.damage


      def get_list(self):
            stuff = [str(self.damage), self.element, self.type]
            return stuff


      def set_magic(self, stuff):
            damage = ""
            length = len(stuff[0])
            i = 0
            while i < length:
                  damage += stuff[0][i]
                  i += 1
            self.damage = int(damage)

            element = ""
            length = len(stuff[1])
            i = 0
            while i < length:
                  element += stuff[1][i]
                  i += 1
            self.element = element

            typ = ""
            length = len(stuff[2])
            i = 0
            while i < length:
                  typ += stuff[2][i]
                  i += 1
            self.type = typ


      def check(self):
            spell = self.element + " " + self.type
            print("Your current magic is a " + spell + " spell")
            print("It does " + str(self.damage) + " damage")
            

      def learn(self):
            print("You can learn a " + self.spell + " spell")
            print("It does " + str(self.damage) + " damage")
