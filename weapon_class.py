#!/usr/bin/python3

import random

class Weapon():
      def __init__(self, level):
            weapon_types = ["Sword", "Bow", "Axe", "Flail", "Hammer"]
            pick = random.randint(0, 4)
            
            self.type = weapon_types[pick]

            if level == 0 or level == 1:
                  self.damage = 1
            else:
                  if level %2 == 1:
                        level += 1
                  self.damage = random.randint((level / 2), level)

            if level > 25:
                  damage_types = ["Fire", "Ice", "Lightning"]
                  chance = random.randint(0, 100)
                  if chance >= 60:
                        pick = random.randint(0, 2)
                        self.element = damage_types[pick]
                        self.element_damage = random.randint(1, (level / 5))
                  else:
                        chance = random.randint(0, 100)
                        if chance > 50:
                              self.element = "Normal"
                              self.element_damage = 0
                        else:
                              self.element = "Rusty"
                              self.element_damage = 0
            else:
                  self.element = "Rusty"
                  self.element_damage = 0

            self.total_damage = (self.damage + self.element_damage)


      def get_type(self):
            return self.type


      def get_damage(self):
            return self.total_damage


      def get_list(self):
            stuff = [str(self.damage), str(self.element_damage), self.element, self.type]
            return stuff


      def set_weapon(self, stuff):
            damage = ""
            length = len(stuff[0])
            i = 0
            while i < length:
                  damage += stuff[0][i]
                  i += 1
            self.damage = int(damage)

            damage = ""
            length = len(stuff[1])
            i = 0
            while i < length:
                  damage += stuff[1][i]
                  i += 1
            self.element_damage = int(damage)
            
            self.total_damage = self.damage + self.element_damage

            element = ""
            length = len(stuff[2])
            i = 0
            while i < length:
                  element += stuff[2][i]
                  i += 1
            self.element = element

            typ = ""
            length = len(stuff[3])
            i = 0
            while i < length:
                  typ += stuff[3][i]
                  i += 1
            self.type = typ


      def check(self):
            if self.element != "Normal" and self.element != "Rusty":
                  print("Your current weapon is a " + self.type + " of " + self.element)
                  print("It does " + str(self.damage) + " damage plus " + str(self.element_damage) + " " + self.element + " damage")
            else:
                  print("Your current weapon is a " + self.element + " " + self.type)
                  print("It does " + str(self.damage) + " damage")
                        
            

      def found(self):
            if self.element != "Normal" and self.element != "Rusty":
                  print("You found a " + self.type + " of " + self.element)
                  print("It does " + str(self.damage) + " damage plus " + str(self.element_damage) + " " + self.element + " damage")
            else:
                  print("You found a " + self.element + " " + self.type)
                  print("It does " + str(self.damage) + " damage")

            

            
