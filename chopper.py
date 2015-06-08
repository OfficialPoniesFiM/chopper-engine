# Chopper Engine, an engine written in Python for games.
# Copyright (C) 2015, Nathan Guerrero under Chopper Studios
#
# This file is part of Chopper Engine.
#
# Chopper Engine is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Chopper Engine is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with Chopper Engine.  If not, see <http://www.gnu.org/licenses/>.

import pygame # Imports a big load of load of things 2D for use in our engine.
import sys # Imports a lot of things for use in our engine.
import time # Imports time modules for us to use.
import easygui # Allows us to do dialog boxes and other things.
import psutil # Allows us to see how much (logical) CPUs are available for the engine to use.
runall = True
safeModeDisplay = False # A variable that will be checked to see if safe mode is enabled.

coresAvailable = psutil.cpu_count()

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

configFile = open("config.yaml", "w+")
if configFile.readLine(1) != "# NORESET\n":
  noConfig == True
  configFile.write("# NORESET\n")
  configFile.write("multicore: True\n")
  multiprocessing = True
  if safeModeDisplay == True:
    configFile.write("fullscreen == False\n")
    configFile.write("resolution: 800x600\n")
  else:
    configFile.write("fullscreen == True\n")
    configFile.write("resolution: " + str(fullScreenWidth) + "x" + str(fullScreenHeight) + "\n")
else:
  noConfig = False
  rawYaml = configFile.read()
  gameConfig == yaml.load(rawYaml)

if noConfig == True:
  multiCoreOn == True
elif multiprocessing == True:
  multiCoreOn == True
else:
  multiCoreOn == False

import basegame

oneTime() # Does initial things for game (loading, processing, terrain generation, etc)

while runall == true:
  gameLoop() # Runs game loop from basegame file.
