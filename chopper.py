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

if pygame.display.Info().hw == False: # Stops anyone with hardware with no hardware acceleration to run the game within this engine.
  print "Your hardware is not supported. Your hardware must support hardware acceleration to run this game."
  easygui.msgbox("Chopper Engine couldn't find any way of hardware acceleration for this game! Your hardware/driver must support hardware acceleration to run this game. This problem can be solved by getting a better video card driver. Otherwise, get hardware that will work.", "Hardware/driver not supported")
  time.sleep(10)
  pygame.quit()
  sys.exit()

videoMemory = pygame.display.Info().video_mem
fullScreenWidth, fullScreenHeight = pygame.display.Info().current_w, pygame.display.Info().current_h
if fullScreenWdith == -1 or fullScreenHeight == -1:
  print "The game is having a problem with fullscreen. Error or SDL problem?"
  easygui.msgbox("The game is having a problem with fullscreen. Error or SDL problem?", "Fullscreen error")
  time.sleep(10)
  pygame.quit()
  sys.exit()
