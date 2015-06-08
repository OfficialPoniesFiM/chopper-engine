import sys
defSplashScreen = 1

if __name__ == "__main__":
  print "Wait, wait! You don't launch the game from the basegame file! You use the designated launcher! Not using it will cause multiple problems!"
  raw_input("Press return/enter to continue. ")
  sys.exit()

def render():
  pygame.flip() # Puts the frame onto the window/display.

def oneTime(): # Use this for loading, terrain generation, processing, etc)
  print "Loading game..."

def gameLoop(): # Game loop. Use this for rendering, physics, whatever is needed in real time.
  pygame.flip() # Displays the latest frame.
