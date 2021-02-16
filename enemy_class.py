#!/usr/bin/python3

import random

class Enemy():
      def __init__(self, level):
            races = ["Goblin", "Golem", "Knight", "Mage", "Skeleton", "Zombie"]

            pick = random.randint(0, 5)
            self.race = races[pick]

            if level %2 == 1:
                  level -= 1

            if level == 0 or level == 1:
                  self.attack = 1
                  self.exp = 10
            else:
                  self.attack = random.randint((level / 2), level)
                  self.exp = (self.attack * random.randint(5, 10))

            self.health = (self.attack * random.randint(1, 10))
            
            self.total_health = self.health


      def take_damage(self, damage):
            self.health -= damage


      def get_health(self):
            return self.health


      def get_race(self):
            return self.race


      def get_exp(self):
            return self.exp


      def get_attack(self):
            return self.attack


      def encounter(self):
            print("You encounter an enemy " + self.race)
            print("It has " + str(self.health) + "HP")

      def stats(self):
            print("Enemy " + self.race)
            print("HP: " + str(self.health) + "/" + str(self.total_health))
