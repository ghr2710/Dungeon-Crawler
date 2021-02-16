#!/usr/bin/python3

import random

class Dungeon():
      def __init__(self, level):
            if level <= 10:
                  self.rooms = 1
            elif level <= 20:
                  self.rooms = 2
            elif level <= 30:
                  self.rooms = 3
            elif level <= 40:
                  self.rooms = 4
            elif level <= 50:
                  self.rooms = 5
            elif level > 50:
                  self.rooms = 6


            locations = ["Mine", "Cave", "House", "Crypt", "Ruins"]
            descriptions = ["Abandoned", "Old", "Haunted", "Creepy", "Ancient"]

            pick = random.randint(0, 4)
            location = locations[pick]

            pick = random.randint(0, 4)
            description = descriptions[pick]

            self.name = description + " " + location


      def get_rooms(self):
            return self.rooms


      def get_name(self):
            return self.name
