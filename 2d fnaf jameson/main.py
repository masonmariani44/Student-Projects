import pygame
from pygame.locals import *
from sys import exit
from Player import Player
from Night import Night
from RoomNode import RoomNode


pygame.init()
fps=30
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("FNAF")
clock = pygame.time.Clock()

player = Player()
night = Night()

map = RoomNode("The Office", None)


"""

References:

FNAF1 animatronic movement guide:
https://steamcommunity.com/sharedfiles/filedetails/?id=2995834654#:~:text=Every%204%2D5%20seconds%2C%20an,will%20not%20move%20at%20all.



"""


"""

player class 
   handling inputs
   handle button presses and environment interaction
   (doors, lights, etc, cameras)
   handling the view??? maybe?

environment? multiple classes each for an envornment object
   power/lights
   doors
   buttons?

class for animatronics/enemy
   enemy behavors
   animations? maybe?
   states they can be in etc.

map class
   what rooms are there
   cams in the room? where is the camera?


ui/menus... work on this later


"""




def handle_events():
   all_events = pygame.event.get()
   for event in all_events:
       if event.type == QUIT:
           pygame.quit()
           exit()
   return all_events

       

def draw():
    return

def update(all_events):
    player.update(all_events, night)


def setup_map_fnaf1():

   west_south = RoomNode("West Hall South", "2B")
   map.add_room(west_south)

   west_north = RoomNode("West Hall North", "2A")
   west_south.add_room(west_north)


   supply = RoomNode("Supply Closet", "1C")
   west_north.add_room(supply)

   dining = RoomNode("Dining Hall", "1B")
   west_north.add_room(dining)



   pirate = RoomNode("Pirate Cove", "3")
   dining.add_room(pirate)

   back = RoomNode("Backstage", "5")
   dining.add_room(back)

   show = RoomNode("Show Stage", "1A")
   dining.add_room(show)

   bath = RoomNode("Bathroom", "7")
   dining.add_room(bath)

   kitchen = RoomNode("Kitchen", "6")
   dining.add_room(kitchen)

   north_east = RoomNode("East Hall North", "4A")
   dining.add_room(north_east)

   south_east = RoomNode("East Hall South", "4B")
   north_east.add_room(south_east)

   map.add_room(south_east)







def main():

    while True:
        clock.tick(fps)
        all_events = handle_events()
        update(all_events)
        draw()


main()