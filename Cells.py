import pygame
import random

class Cells():
    """This class is used to keep track of each cell within the maze"""

    # Class attributes
    screenWidth = 800 # Size of the screen
    screenHeight = 600 # Heigh of the screen

    cellSize = 40 # How big the cells will be

    def __init__(self, x, y):
        """Constructor for the cells"""

        self.x = x # The x coordinate of the cell
        self.y = y # The y coordinate of the cell
        self.walls = [True, True, True, True] # This booleans variables represent which walls should be drawn
        self.discovered = False # This varialve is used to know if the cell is new or not


    def display(self, screen, c = (255, 255, 255)):
        """Display a rectangle that is drawn from 4 seperate lines, which can be removed later on

        Parameters
        ----------
        screen : The display window we are drawing to
        c = default(255, 255, 255),
            the color of what we are drawing in rgb value

        """
        if(self.discovered):
            # If the cell was been discovered a blue rectangle will be drawn in the position without an outline
            pygame.draw.rect(screen , (0, 0 , 100), (self.x * self.cellSize, self.y * self.cellSize, self.cellSize, self.cellSize))


        # Depeding on the values inside Walls, different parts of the rectangle will be drawn
        if(self.walls[0]):
            pygame.draw.line(screen, c, (self.x * self.cellSize,  self.y * self.cellSize), ((self.x + 1) * self.cellSize, self.y * self.cellSize)) # Draw top line

        if(self.walls[1]):
            pygame.draw.line(screen, c, (self.x * self.cellSize,  self.y * self.cellSize), (self.x * self.cellSize, (self.y + 1) * self.cellSize)) # Draw left line

        if(self.walls[2]):
            pygame.draw.line(screen, c, ((self.x + 1) * self.cellSize,  (self.y + 1) * self.cellSize), (self.x * self.cellSize, (self.y + 1) * self.cellSize)) # Draw bot line

        if(self.walls[3]):
            pygame.draw.line(screen, c, ((self.x + 1) * self.cellSize,  (self.y + 1) * self.cellSize), ((self.x + 1) * self.cellSize, self.y * self.cellSize)) # Draw right line




    def checkNeighbors(self, grid, x, y):
        """This method looks for new undiscovered neighbors based on the cell that calls it

        Parameters
        ---------------
        grid, the 2d array of cells
        x, the x coordinate of the current cell
        y, the y coordinate of the current cell
        """

        neighbors = []

        # This statement makes sure there is not array out of bounds error
        if(y - 1 >= 0):
            # This grabs the cell above the current cell
            top  =  grid[x][y - 1]

        # This statement makes sure there is not array out of bounds error
        if(x - 1 >= 0):
            # This grabs the cell to the left of the current cell
            left =  grid[x - 1][y]

        # This statement makes sure there is not array out of bounds error
        if(y + 1 < self.screenHeight // self.cellSize):
            # This grabs the cell below the current cell
            bot =   grid[x][y + 1]

        # This statement makes sure there is not array out of bounds error
        if(x + 1 < self.screenWidth // self.cellSize):
            # This grabs the cell to the right of the current cell
            right = grid[x + 1][y]

        if("top" in locals() and not top.discovered):
            neighbors.append(top) # If the top cell has not been discovered added to the neighbor array

        if("left" in locals() and not left.discovered):
            neighbors.append(left) # If the left cell has not been discovered added to the neighbor array

        if("right" in locals() and not right.discovered):
            neighbors.append(right) # If the right cell has not been discovered added to the neighbor array

        if("bot" in locals() and not bot.discovered):
            neighbors.append(bot) # If the bottom cell has not been discovered added to the neighbor array

        if(len(neighbors) > 0):
            return random.choice(neighbors) # Return a random cell
        else:
            return -1 # If all cells were discovered return -1


    def removeWalls(self, nextCell):
        """This method removes walls to create the maze based on the next cell that the program moves too

        Parameters
        ---------------
        nextCell, the newcell we are going to move to
        """
        
        x = self.x - nextCell.x # This is used to determine which walls to remove

        if(x == 1):
            self.walls[1] = False # remove left wall
            nextCell.walls[3] = False # remove right wall
        elif(x == -1):
            self.walls[3] = False # remove right wall
            nextCell.walls[1] = False # remove left wall

        y = self.y - nextCell.y

        if(y == 1):
            self.walls[0] = False # remove top wall
            nextCell.walls[2] = False # remove bottom wall
        elif(y == -1):
            self.walls[2] = False # remove bottom wall
            nextCell.walls[0] = False # remove top wall
