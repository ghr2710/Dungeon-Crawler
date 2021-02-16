#!/usr/bin/python3

import save_and_load
from weapon_class import Weapon
from magic_class import Magic
from enemy_class import Enemy
from player_class import Player
from dungeon_class import Dungeon

while True:
      print("Option 1: Weapons Test")
      print("Option 2: Spells Test")
      print("Option 3: Enemy Test")
      print("Option 4: Player Test")
      print("Option 5: Dungeon Test")
      print("Option 6: Save and Load Test")
      print("Option 7: End Tests")
      print()
      c = int(input("Select Option: "))
      print()

      if c == 1:
            player_weapon = Weapon(1)
            while True:
                  level = int(input("Enter player's level: "))
                  print()
                  test_weapon = Weapon(level)
                  test_weapon.found()
                  player_weapon.check()
                  wep = input("Do you want to replace your weapon with it? (y/n): ")
                  if wep == "y":
                        player_weapon = test_weapon
                        print("\nYou have replaced your weapon")
                        print("==========")
                  print()

                  again = input("Do you want to find another weapon? (y/n): ")
                  print()
                  if again == "n":
                        break

      if c == 2:
            player_magic = Magic(1)
            level = int(input("Enter player's level: "))
            print()
            while True:
                  test_magic = Magic(level)
                  test_magic.learn()
                  player_magic.check()
                  mag = input("Do you want to replace your magic with it? (y/n): ")
                  if mag == "y":
                        player_magic = test_magic
                        print("\nYou have replaced your magic")
                        print("==========")
                  print()

                  again = input("Do you want to learn another spell? (y/n): ")
                  
                  if again == "n":
                        print()
                        break
                  else:
                        print("==========")
                        print()

      if c == 3:
            while True:
                  level = int(input("Enter player's level: "))
                  print()
                  test_enemy = Enemy(level)
                  player_weapon = Weapon(level)
                  player_magic = Magic(level)

                  test_enemy.encounter()
                  player_weapon.check()
                  player_magic.check()

                  player_spell = player_magic.get_spell()
                  player_type = player_weapon.get_type()
                  enemy_type = test_enemy.get_race()

                  attack = input("Do you want to attack the enemy? (y/n): ")
                  print()

                  if attack == "y":
                        player_weapon_damage = player_weapon.get_damage()
                        player_magic_damage = player_magic.get_damage()
                        enemy_damage = test_enemy.get_attack()
                        while True:
                              if test_enemy.get_health() <= 0:
                                    print("You defeated the enemy " + enemy_type)
                                    print("===============")
                                    print()
                                    break
                              else:
                                    while True:
                                          print("Your turn to attack")
                                          print("===============")
                                          test_enemy.stats()
                                          hit = input("WEAPON / MAGIC / PASS: ")
                                          print("===============")
                                          if hit == "magic" or hit == "MAGIC" or hit == "Magic" or hit == "m" or hit == "M":
                                                print("You hit the " + enemy_type + " with a " + player_spell + " spell")
                                                print("You hit for " + str(player_magic_damage) + " damage")
                                                print("===============")
                                                test_enemy.take_damage(player_magic_damage)
                                                break
                                          
                                          if hit == "weapon" or hit == "WEAPON" or hit == "Weapon" or hit == "w" or hit == "W":
                                                print("You hit the " + enemy_type + " with your " + player_type)
                                                print("You hit for " + str(player_weapon_damage) + " damage")
                                                print("===============")
                                                test_enemy.take_damage(player_weapon_damage)
                                                break
                                          
                                          if hit == "pass" or hit == "PASS" or hit == "Pass" or hit == "p" or hit == "P":
                                                print("You did nothing")
                                                print("===============")
                                                break
                                          
                                          else:
                                                print("\n\nPlease select a valid option\n\n")
                              
                              if test_enemy.get_health() > 0:                  
                                    print("The enemy " + enemy_type + " tried to hit you, but failed")
                                    print("===============")

                  new_enemy = input("Make a new enemy? (y/n): ")
                  print()
                  if new_enemy == "n":
                        break


      if c == 4:
            test_player = Player()
            print("New player created")
            print("===============")
            test_player.stats()
            print("===============")
            
            while True:
                  level_up = input("Level up? (y/n): ")
                  print("===============")
                  if level_up == "y":
                        test_player.level_up()
                  elif level_up == "n":
                        print("No level up")
                        print("===============")
                        break
                  else:
                        print("Enter a valid option")
                        print()

            test_enemy = Enemy(100)

            player_weapon = test_player.get_weapon()
            player_magic = test_player.get_magic()
            
            player_weapon_damage = player_weapon.get_damage()
            player_magic_damage = player_magic.get_damage()
            
            player_spell = player_magic.get_spell()
            player_type = player_weapon.get_type()
            
            enemy_damage = test_enemy.get_attack()
            enemy_type = test_enemy.get_race()

            while True:
                        if test_enemy.get_health() <= 0:
                              print("You defeated the enemy " + enemy_type)
                              print("===============")
                              print()
                              break
                        else:
                              while True:
                                    print("Your turn to attack")
                                    print("===============")
                                    test_enemy.stats()
                                    hit = input("WEAPON / MAGIC / PASS: ")
                                    print("===============")
                                    if hit == "magic" or hit == "MAGIC" or hit == "Magic" or hit == "m" or hit == "M":
                                          print("You hit the " + enemy_type + " with a " + player_spell + " spell")
                                          print("You hit for " + str(player_magic_damage) + " damage")
                                          print("===============")
                                          test_enemy.take_damage(player_magic_damage)
                                          break
                                    
                                    if hit == "weapon" or hit == "WEAPON" or hit == "Weapon" or hit == "w" or hit == "W":
                                          print("You hit the " + enemy_type + " with your " + player_type)
                                          print("You hit for " + str(player_weapon_damage) + " damage")
                                          print("===============")
                                          test_enemy.take_damage(player_weapon_damage)
                                          break
                                    
                                    if hit == "pass" or hit == "PASS" or hit == "Pass" or hit == "p" or hit == "P":
                                          print("You did nothing")
                                          print("===============")
                                          break
                                    
                                    else:
                                          print("\n\nPlease select a valid option\n\n")
                        
                        if test_enemy.get_health() > 0:                  
                              print("The enemy " + enemy_type + " is attacking!")
                              print("It hit you for " + str(enemy_damage) + " damage")
                              test_player.take_damage(enemy_damage)
                              if test_player.get_health() <= 0:
                                    print("==========YOU ARE DEAD==========")
                                    print("===========GAME OVER===========")
                                    print()
                                    break
                              else:
                                    print("===============")

      if c == 5:
            level = int(input("Enter player's level: "))
            print("===============")
            print("Generating Dungeon")
            test_dungeon = Dungeon(level)
            print("===============")
            name = test_dungeon.get_name()
            rooms = test_dungeon.get_rooms()
            print("You walk up to " + name + " with " + str(rooms) + " rooms")
            print("===============")
            print()


      if c == 6:
            while True:
                  ask = input("Save, Load, Exit: ")
                  print("===============")
                  if ask == "save":
                        test_player = Player()
                        magic = test_player.get_magic()
                        magic.check()
                        save_and_load.save(test_player)
                        print("===============")
                  elif ask == "load":
                        load_player = save_and_load.load()
                        magic = load_player.get_magic()
                        magic.check()
                        print("===============")
                  elif ask == "exit":
                        break
                  else:
                        print("Enter valid option")
                        print()
            print("===============")
            print()
                  
                  
      if c == 7:
            break


      else:
            print("Enter a valid option")
            print()
            
            
                        
                              
                                                
                                                
                                          













                              
            
