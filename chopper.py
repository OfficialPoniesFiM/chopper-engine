# Chopper Engine, an engine written in Python for games.
# Copyright (C) 2015, Nathan Guerrero under Chopper Games/Studios
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import pygame # Imports a big load of load of things 2D for use in our engine.
import sys # Imports a lot of things for use in our engine.
import time # Imports time modules for us to use.
import easygui # Allows us to do dialog boxes and other things.
safeModeDisplay = False

def gameExit(sleep): # A function that exits the game. It also allows the program to wait a bit if the argument is True.
  if sleep == True:
    time.sleep(10)
  pygame.quit()
  sys.exit()

if pygame.display.Info().hw == False: # Stops anyone with hardware with no hardware acceleration to run the game within this engine.
  print "Your hardware is not supported. Your hardware must support hardware acceleration to run this game."
  easygui.msgbox("Chopper Engine couldn't find any way of hardware acceleration for this game! Your hardware/driver must support hardware acceleration to run this game. This problem can be solved by getting a better video card driver. Otherwise, get hardware that will work.", "Hardware/driver not supported")
  gameExit(True)

videoMemory = pygame.display.Info().video_mem # Variable for how much video memory is in the system.
fullScreenWidth, fullScreenHeight = pygame.display.Info().current_w, pygame.display.Info().current_h # Variable for how big the desktop is for fullscreen.
if fullScreenWidth == -1 or fullScreenHeight == -1: #Stops engine if pygame.display.Info() return -1 for desktop size.
  print "The game is having a problem with fullscreen. Error or SDL problem?"
  easygui.msgbox("The game is having a problem with fullscreen. Error or SDL problem?", "Fullscreen error")
  gameExit(True)

vramUsage = fullScreenWidth * fullScreenHeight * pygame.display.Info().bytesize # We calculate how much VRAM we use from the number of all pixels * how much bytes each pixel takes.
if vramUsage > videoMemory:
  safeModeDisplay = True # We set safe mode for the display to true, and this will turn down the resolution to 800x600 or lower.
