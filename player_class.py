#!/usr/bin/python3

import random
from weapon_class import Weapon
from magic_class import Magic


class Player():
      def __init__(self):
            self.level = 1
            self.exp = 0
            self.exp_cap = 100
            self.weapon = Weapon(self.level)
            self.magic = Magic(self.level)
            self.health = 10
            self.total_health = self.health


      def level_up(self):
            self.level += 1
            self.exp -= self.exp_cap
            self.exp_cap += 100
            print("You leveled up!")
            print("You are now level " + str(self.level))
            self.health += 10
            self.total_health = self.health
            print("Your max health has increased by 10")
            print("===============")
            new_spell = Magic(self.level)
            new_spell.learn()
            self.magic.check()
            while True:
                  c2 = input("Do you want to replace your current magic? (y/n): ")
                  print("===============")
                  if c2 == "y":
                        print("You replaced your old spell")
                        self.magic = new_spell
                        break
                  elif c2 == "n":
                        print("You gave up on the new spell")
                        break
                  else:
                        print("Enter a valid option")
                        print()
            print("===============")


      def get_weapon(self):
            return self.weapon


      def get_magic(self):
            return self.magic


      def check_exp(self):
            if self.exp >= self.exp_cap:
                  self.level_up()
            else:
                  print("Progress to next level up: " + str(self.exp) + "/" + str(self.exp_cap))


      def gain_exp(self, exp):
            self.exp += exp
            self.check_exp()


      def get_level(self):
            return self.level


      def get_health(self):
            return self.health


      def get_list(self):
            stuff = [str(self.level), str(self.exp), str(self.exp_cap), str(self.health)]
            return stuff


      def set_player(self, stuff):
            level = ""
            length = len(stuff[0])
            i = 0
            while i < length:
                  level += stuff[0][i]
                  i += 1
            self.level = int(level)

            exp = ""
            length = len(stuff[1])
            i = 0
            while i < length:
                  exp += stuff[1][i]
                  i += 1
            self.exp = int(exp)

            cap = ""
            length = len(stuff[2])
            i = 0
            while i < length:
                  cap += stuff[2][i]
                  i += 1
            self.exp_cap = int(cap)

            health = ""
            length = len(stuff[3])
            i = 0
            while i < length:
                  health += stuff[3][i]
                  i += 1
            self.health = int(health)
            
            self.total_health = self.health
            
            self.weapon = stuff[4]
            self.magic = stuff[5]


      def stats(self):
            print("Player")
            print("HP: " + str(self.health) + "/" + str(self.total_health))


      def take_damage(self, damage):
            self.health -= damage


      def heal(self):
            self.health = self.total_health

      def change_weapon(self, weapon):
            self.weapon = weapon
