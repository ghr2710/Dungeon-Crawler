#!/usr/bin/python3

import data_utility
from weapon_class import Weapon
from magic_class import Magic
from enemy_class import Enemy
from player_class import Player
from dungeon_class import Dungeon


def found_weapon(player):
      weapon = Weapon(player.get_level())
      player_weapon = player.get_weapon()
      weapon.found()
      print("===============")
      player_weapon.check()
      print("===============")
      wep = input("Do you want to replace your weapon with it? (y/n): ")
      if wep == "y":
            player.change_weapon(weapon)
            print("===============")
            print("You have replaced your weapon")
            print("===============")
      else:
            print("===============")
            print("You left the weapon behind")
            print("===============")
      print()


def fight(player):
      win = False
      
      enemy = Enemy(player.get_level())

      player_weapon = player.get_weapon()
      player_magic = player.get_magic()
      
      player_weapon_damage = player_weapon.get_damage()
      player_magic_damage = player_magic.get_damage()
      
      player_spell = player_magic.get_spell()
      player_type = player_weapon.get_type()
      
      enemy_damage = enemy.get_attack()
      enemy_type = enemy.get_race()

      enemy.encounter()
      print("===============")

      while True:
                  if enemy.get_health() <= 0:
                        print("You defeated the enemy " + enemy_type)
                        win = True
                        print("===============")
                        player.gain_exp(enemy.get_exp())
                        print("===============")
                        print()
                        break
                  else:
                        while True:
                              print("Your turn to attack")
                              print("===============")
                              player.stats()
                              print("===============")
                              enemy.stats()
                              hit = input("WEAPON / MAGIC / PASS: ")
                              print("===============")
                              if hit == "magic" or hit == "MAGIC" or hit == "Magic" or hit == "m" or hit == "M":
                                    print("You hit the " + enemy_type + " with a " + player_spell + " spell")
                                    print("You hit for " + str(player_magic_damage) + " damage")
                                    print("===============")
                                    enemy.take_damage(player_magic_damage)
                                    break
                              
                              if hit == "weapon" or hit == "WEAPON" or hit == "Weapon" or hit == "w" or hit == "W":
                                    print("You hit the " + enemy_type + " with your " + player_type)
                                    print("You hit for " + str(player_weapon_damage) + " damage")
                                    print("===============")
                                    enemy.take_damage(player_weapon_damage)
                                    break
                              
                              if hit == "pass" or hit == "PASS" or hit == "Pass" or hit == "p" or hit == "P":
                                    print("You did nothing")
                                    print("===============")
                                    break
                              
                              else:
                                    print("\n\nPlease select a valid option\n\n")
                  
                  if enemy.get_health() > 0:                  
                        print("The enemy " + enemy_type + " is attacking!")
                        print("It hit you for " + str(enemy_damage) + " damage")
                        player.take_damage(enemy_damage)
                        if player.get_health() <= 0:
                              print()
                              print("==========YOU ARE DEAD==========")
                              print("===========GAME OVER===========")
                              break
                        else:
                              print("===============")
      return win


def quest(player, dungeon):
      num = dungeon.get_rooms()

      while num > 0:
            win = fight(player)
            if win == False:
                  break
            else:
                  found_weapon(player)
                  player.heal()
                  num -= 1

      if win == True:
            return True
      else:
            return False


def save(player):
      weapon = player.get_weapon()
      magic = player.get_magic()

      weapon_list = weapon.get_list()
      magic_list = magic.get_list()
      player_list = player.get_list()

      save_data = [player_list[0], player_list[1], player_list[2], player_list[3], weapon_list[0], weapon_list[1], weapon_list[2], weapon_list[3], magic_list[0], magic_list[1], magic_list[2]]

      data_utility.write(save_data)


def load():
      save_data = data_utility.read()

      weapon_list = [save_data[4], save_data[5], save_data[6], save_data[7]]
      magic_list = [save_data[8], save_data[9], save_data[10]]

      magic = Magic(0)
      magic.set_magic(magic_list)

      weapon = Weapon(1)
      weapon.set_weapon(weapon_list)

      player_list = [save_data[0], save_data[1], save_data[2], save_data[3], weapon, magic]
      player = Player()
      player.set_player(player_list)

      return player
