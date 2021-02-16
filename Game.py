#!/usr/bin/python3

import game_module
from weapon_class import Weapon
from magic_class import Magic
from enemy_class import Enemy
from player_class import Player
from dungeon_class import Dungeon


print("Welcome to Dungeon Crawler!")
print()
x = input("Press enter to continue...")
print()


player = Player()
weapon = player.get_weapon()

print("You are an adventurer seeking fame and fortune.")
x = input("Press enter to continue...")
print()
print("Your travels have taken you far and wide.")
x = input("Press enter to continue...")
print()
print("However, success has constantly been out of reach.")
x = input("Press enter to continue...")
print()
print("Perhaps this new land will bring you the fame and fortune you seek.")
x = input("Press enter to start the game")
print()

while True:
      print("Option 1: Go on a quest")
      print("Option 2: Check your gear and experience")
      print("Option 3: Save")
      print("Option 4: Load")
      print("Option 5: Quit")
      option = int(input("Select an option: "))
      print()
      print("===============")

      if option == 1:
            dungeon = Dungeon(player.get_level())
            name = dungeon.get_name()
            rooms = dungeon.get_rooms()
            if rooms == 1:
                  print("You are offered a quest in the " + name + " to clear " + str(rooms) + " room")
            else:
                  print("You are offered a quest in the " + name + " to clear " + str(rooms) + " rooms")
            print("===============")

            while True:
                  accept = input("Do you accept this quest? (y/n): ")
                  print("===============")
                  if accept == "y":
                        win = game_module.quest(player, dungeon)
                        break
                  elif accept == "n":
                        print("You didn't want to go to the" + name)
                        print("===============")
                        break
                  else:
                        print("Enter a valid option")
                        print("===============")

            print()
            
            if win == False:
                  break


      elif option == 2:
            weapon = player.get_weapon()
            weapon.check()
            print("===============")
            magic = player.get_magic()
            magic.check()
            print("===============")
            player.check_exp()
            print("===============")
            print()


      elif option == 3:
            game_module.save(player)


      elif option == 4:
            player = game_module.load()


      elif option == 5:
            print("QUITTING WILL DELETE ALL UNSAVED PROGRESS")
            choice = input("Are you sure you want to quit? (y/n): ")
            if choice == "y":
                  break
            elif choice == "n":
                  print("===============")
                  print()
            else:
                  print("Enter a valid option")
                  print("===============")


      else:
            print("Enter a valid option")
            print("===============")
            









                  
            
            
