import pygame
from Cells import Cells

# Intialize the display window
pygame.init()

# Colors for the maze generation
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
################################

# Screen display parameters and setup
screenDisplay = pygame.display.set_mode((Cells.screenWidth, Cells.screenHeight))
screenDisplay.fill(black)
###############################

# Cells information
cols = Cells.screenWidth//Cells.cellSize
rows = Cells.screenHeight//Cells.cellSize
cellList = []
cellStack = []
##############################


# Set up grid for the start of the maze generation
# This loop creates a 2d-array with each cells of the maze is assinged an x and y coordinate
for x in range(cols):
    temp_arr = []
    for y in range(rows):
        new_cell = Cells(x, y)
        temp_arr.append(new_cell)
    cellList.append(temp_arr)

currentCell = cellList[0][0] # The starting celll is the one on the top left corner
##########################################

maze_array = []
run_once = True
while True:

    # This neseted for loop will go through each cell and call the diplay method
    for cell_array in cellList:
        for single_cell in cell_array:
            single_cell.display(screenDisplay);

    # The statement below is used to keep track of how the maze is generating as it follows the most recent cell
    pygame.draw.rect(screenDisplay , (0, 255 , 0), (currentCell.x * Cells.cellSize, currentCell.y * Cells.cellSize, Cells.cellSize, Cells.cellSize))
    pygame.display.flip() # This updates the display window


    currentCell.discovered = True

    # The function will either return a new cell or -1
    nextCell = currentCell.checkNeighbors(cellList, currentCell.x, currentCell.y)

    # If the nextCell is not negative one then there is a new cell to move to
    if(not nextCell == -1):
        cellStack.append(currentCell) # Add the current Cell to the stack of cells

        currentCell.removeWalls(nextCell); #Remove the walls to create the maza
        currentCell = nextCell # change the current cell to the new one

    # If the stack of cells is not empty and nextCell was -1 that means we have to backtrack
    elif(len(cellStack) > 0):
        currentCell = cellStack.pop(len(cellStack) -1) # set the current cell to the previous cell

    else:
        #The maze finished generating.
        pass

    # this loop is used to close the program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Update the display windpw
    pygame.display.update()
