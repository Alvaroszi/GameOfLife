#Alvaro Szigethi Marcos
#This is a small Python script in which you can run your own small version of the Game of Life using your computer terminal
#This is a small 2-day project that I wanted to do after watching Numberphile's "Inventing Game of Life - Numberphile" video
#This project is supposed to show something that I find very fun and beautiful and related to Computer Science 
import time

OFF = "X"
ON = " "

def initializeGrid(width, height):
	grid = []
	for y in range(0,height):
		toAppend=[]
		for x in range(0,width):
			toAppend.append(OFF)
		grid.append(toAppend)
	return grid

def printGrid(grid):
	for x in range(0,len(grid)):
		toPrint = ""
		for y in grid[x]:
			toPrint+=y
		print(toPrint)

def gosperGliderGun(x,y,grid):
	try:
		grid[y+5][x+1] = ON
	except IndexError:
		pass
	try:
		grid[y+5][x+2] = ON
	except IndexError:
		pass
	try:
		grid[y+6][x+1] = ON
	except IndexError:
		pass
	try:
		grid[y+6][x+2] = ON
	except IndexError:
		pass
	try:
		grid[y+5][x+11] = ON
	except IndexError:
		pass
	try:
		grid[y+6][x+11] = ON
	except IndexError:
		pass
	try:
		grid[y+7][x+11] = ON
	except IndexError:
		pass
	try:
		grid[y+4][x+12] = ON
	except IndexError:
		pass
	try:
		grid[y+8][x+12] = ON
	except IndexError:
		pass
	try:
		grid[y+3][x+13] = ON
	except IndexError:
		pass
	try:
		grid[y+9][x+13] = ON
	except IndexError:
		pass
	try:
		grid[y+3][x+14] = ON
	except IndexError:
		pass
	try:
		grid[y+9][x+14] = ON
	except IndexError:
		pass
	try:
		grid[y+6][x+15] = ON
	except IndexError:
		pass
	try:
		grid[y+4][x+16] = ON
	except IndexError:
		pass
	try:
		grid[y+8][x+16] = ON
	except IndexError:
		pass
	try:
		grid[y+5][x+17] = ON
	except IndexError:
		pass
	try:
		grid[y+6][x+17] = ON
	except IndexError:
		pass
	try:
		grid[y+7][x+17] = ON
	except IndexError:
		pass
	try:
		grid[y+6][x+18] = ON
	except IndexError:
		pass
	try:
		grid[y+3][x+21] = ON
	except IndexError:
		pass
	try:
		grid[y+4][x+21] = ON
	except IndexError:
		pass
	try:
		grid[y+5][x+21] = ON
	except IndexError:
		pass
	try:
		grid[y+3][x+22] = ON
	except IndexError:
		pass
	try:
		grid[y+4][x+22] = ON
	except IndexError:
		pass
	try:
		grid[y+5][x+22] = ON
	except IndexError:
		pass
	try:
		grid[y+2][x+23] = ON
	except IndexError:
		pass
	try:
		grid[y+6][x+23] = ON
	except IndexError:
		pass
	try:
		grid[y+1][x+25] = ON
	except IndexError:
		pass
	try:
		grid[y+2][x+25] = ON
	except IndexError:
		pass
	try:
		grid[y+6][x+25] = ON
	except IndexError:
		pass
	try:
		grid[y+7][x+25] = ON
	except IndexError:
		pass
	try:
		grid[y+3][x+35] = ON
	except IndexError:
		pass
	try:
		grid[y+4][x+35] = ON
	except IndexError:
		pass
	try:
		grid[y+3][x+36] = ON
	except IndexError:
		pass
	try:
		grid[y+4][x+36] = ON
	except IndexError:
		pass

def addGlider(x,y,grid):
	try:
		grid[y][x] = ON
	except IndexError:
		pass
	try:
		grid[y+1][x+1] = ON
	except IndexError:
		pass
	try:
		grid[y+2][x+1] = ON
	except IndexError:
		pass
	try:
		grid[y+2][x] = ON
	except IndexError:
		pass
	try:
		grid[y+2][x-1] = ON
	except IndexError:
		pass

def addBlinker(x,y,grid):
	try:
		grid[y][x] = ON
	except IndexError:
		pass
	try:
		grid[y][x+1] = ON
	except IndexError:
		pass
	try:
		grid[y][x+2] = ON
	except IndexError:
		pass

def addTub(x,y,grid):
	try:
		grid[y+1][x] = ON
	except IndexError:
		pass
	try:
		grid[y][x+1] = ON
	except IndexError:
		pass
	try:
		grid[y+1][x+2] = ON
	except IndexError:
		pass
	try:
		grid[y+2][x+1] = ON
	except IndexError:
		pass

def addBoat(x,y,grid):
	try:
		grid[y][x] = ON
	except IndexError:
		pass
	try:
		grid[y+1][x] = ON
	except IndexError:
		pass
	try:
		grid[y][x+1] = ON
	except IndexError:
		pass
	try:
		grid[y+1][x+2] = ON
	except IndexError:
		pass
	try:
		grid[y+2][x+1] = ON
	except IndexError:
		pass

def addLoaf(x,y,grid):
	try:
		grid[y+1][x] = ON
	except IndexError:
		pass
	try:
		grid[y][x+1] = ON
	except IndexError:
		pass
	try:
		grid[y][x+2] = ON
	except IndexError:
		pass
	try:
		grid[y+1][x+3] = ON
	except IndexError:
		pass
	try:
		grid[y+2][x+3] = ON
	except IndexError:
		pass
	try:
		grid[y+2][x+1] = ON
	except IndexError:
		pass
	try:
		grid[y+3][x+2] = ON
	except IndexError:
		pass

def addBlock(x,y,grid):
	try:
		grid[y][x] = ON
	except IndexError:
		pass
	try:
		grid[y][x+1] = ON
	except IndexError:
		pass
	try:
		grid[y+1][x] = ON
	except IndexError:
		pass
	try:
		grid[y+1][x+1] = ON
	except IndexError:
		pass

def addBeacon(x,y,grid):
	try:
		grid[y][x] = ON
	except IndexError:
		pass
	try:
		grid[y+1][x] = ON
	except IndexError:
		pass
	try:
		grid[y][x+1] = ON
	except IndexError:
		pass
	try:
		grid[y+1][x+1] = ON
	except IndexError:
		pass
	try:
		grid[y+2][x+2] = ON
	except IndexError:
		pass
	try:
		grid[y+3][x+2] = ON
	except IndexError:
		pass
	try:
		grid[y+2][x+3] = ON
	except IndexError:
		pass
	try:
		grid[y+3][x+3] = ON
	except IndexError:
		pass

def addToad(x,y,grid):
	try:
		grid[y][x+1] = ON
	except IndexError:
		pass
	try:
		grid[y][x+2] = ON
	except IndexError:
		pass
	try:
		grid[y][x+3] = ON
	except IndexError:
		pass
	try:
		grid[y+1][x] = ON
	except IndexError:
		pass
	try:
		grid[y+1][x+1] = ON
	except IndexError:
		pass
	try:
		grid[y+1][x+2] = ON
	except IndexError:
		pass

def addBeehive(x,y,grid):
	try:
		grid[y+1][x] = ON
	except IndexError:
		pass
	try:
		grid[y][x+1] = ON
	except IndexError:
		pass
	try:
		grid[y][x+2] = ON
	except IndexError:
		pass
	try:
		grid[y+1][x+3] = ON
	except IndexError:
		pass
	try:
		grid[y+2][x+1] = ON
	except IndexError:
		pass
	try:
		grid[y+2][x+2] = ON
	except IndexError:
		pass

def addLWSS(x,y,grid):
	try:
		grid[y][x+1] = ON
	except IndexError:
		pass
	try:
		grid[y][x+2] = ON
	except IndexError:
		pass
	try:
		grid[y+1][x] = ON
	except IndexError:
		pass
	try:
		grid[y+1][x+1] = ON
	except IndexError:
		pass
	try:
		grid[y+1][x+2] = ON
	except IndexError:
		pass
	try:
		grid[y+1][x+3] = ON
	except IndexError:
		pass
	try:
		grid[y+2][x] = ON
	except IndexError:
		pass
	try:
		grid[y+2][x+1] = ON
	except IndexError:
		pass
	try:
		grid[y+2][x+3] = ON
	except IndexError:
		pass
	try:
		grid[y+2][x+4] = ON
	except IndexError:
		pass
	try:
		grid[y+3][x+2] = ON
	except IndexError:
		pass
	try:
		grid[y+3][x+3] = ON
	except IndexError:
		pass

def addMWSS(x,y,grid):
	try:
		grid[y][x+1] = ON
	except IndexError:
		pass
	try:
		grid[y][x+2] = ON
	except IndexError:
		pass
	try:
		grid[y][x+3] = ON
	except IndexError:
		pass
	try:
		grid[y+1][x] = ON
	except IndexError:
		pass
	try:
		grid[y+1][x+1] = ON
	except IndexError:
		pass
	try:
		grid[y+1][x+2] = ON
	except IndexError:
		pass
	try:
		grid[y+1][x+3] = ON
	except IndexError:
		pass
	try:
		grid[y+1][x+4] = ON
	except IndexError:
		pass
	try:
		grid[y+2][x] = ON
	except IndexError:
		pass
	try:
		grid[y+2][x+1] = ON
	except IndexError:
		pass
	try:
		grid[y+2][x+2] = ON
	except IndexError:
		pass
	try:
		grid[y+2][x+4] = ON
	except IndexError:
		pass
	try:
		grid[y+2][x+5] = ON
	except IndexError:
		pass
	try:
		grid[y+3][x+3] = ON
	except IndexError:
		pass
	try:
		grid[y+3][x+4] = ON
	except IndexError:
		pass

def addHWSS(x,y,grid):
	try:
		grid[y][x+1] = ON
	except IndexError:
		pass
	try:
		grid[y][x+2] = ON
	except IndexError:
		pass
	try:
		grid[y][x+3] = ON
	except IndexError:
		pass
	try:
		grid[y][x+4] = ON
	except IndexError:
		pass
	try:
		grid[y+1][x] = ON
	except IndexError:
		pass
	try:
		grid[y+1][x+1] = ON
	except IndexError:
		pass
	try:
		grid[y+1][x+2] = ON
	except IndexError:
		pass
	try:
		grid[y+1][x+3] = ON
	except IndexError:
		pass
	try:
		grid[y+1][x+4] = ON
	except IndexError:
		pass
	try:
		grid[y+1][x+5] = ON
	except IndexError:
		pass
	try:
		grid[y+2][x] = ON
	except IndexError:
		pass
	try:
		grid[y+2][x+1] = ON
	except IndexError:
		pass
	try:
		grid[y+2][x+2] = ON
	except IndexError:
		pass
	try:
		grid[y+2][x+3] = ON
	except IndexError:
		pass
	try:
		grid[y+2][x+5] = ON
	except IndexError:
		pass
	try:
		grid[y+2][x+6] = ON
	except IndexError:
		pass
	try:
		grid[y+3][x+4] = ON
	except IndexError:
		pass
	try:
		grid[y+3][x+5] = ON
	except IndexError:
		pass

def addPenta(x,y,grid):
	try:
		grid[y+6][x+4] = ON
	except IndexError:
		pass
	try:
		grid[y+11][x+4] = ON
	except IndexError:
		pass
	try:
		grid[y+6][x+6] = ON
	except IndexError:
		pass
	try:
		grid[y+11][x+6] = ON
	except IndexError:
		pass
	try:
		grid[y+4][x+5] = ON
	except IndexError:
		pass
	try:
		grid[y+5][x+5] = ON
	except IndexError:
		pass
	try:
		grid[y+7][x+5] = ON
	except IndexError:
		pass
	try:
		grid[y+8][x+5] = ON
	except IndexError:
		pass
	try:
		grid[y+9][x+5] = ON
	except IndexError:
		pass
	try:
		grid[y+10][x+5] = ON
	except IndexError:
		pass
	try:
		grid[y+12][x+5] = ON
	except IndexError:
		pass
	try:
		grid[y+13][x+5] = ON
	except IndexError:
		pass

def addPulsar(x,y,grid):
	try:
		grid[y][x] = ON
	except IndexError:
		pass
	try:
		grid[y+1][x] = ON
	except IndexError:
		pass
	try:
		grid[y+2][x] = ON
	except IndexError:
		pass
	try:
		grid[y+3][x] = ON
	except IndexError:
		pass
	try:
		grid[y+4][x] = ON
	except IndexError:
		pass
	try:
		grid[y][x+2] = ON
	except IndexError:
		pass
	try:
		grid[y+4][x+2] = ON
	except IndexError:
		pass
	try:
		grid[y][x+4] = ON
	except IndexError:
		pass
	try:
		grid[y+1][x+4] = ON
	except IndexError:
		pass
	try:
		grid[y+2][x+4] = ON
	except IndexError:
		pass
	try:
		grid[y+3][x+4] = ON
	except IndexError:
		pass
	try:
		grid[y+4][x+4] = ON
	except IndexError:
		pass

def update(grid):
	newGrid = initializeGrid(len(grid[0]), len(grid))
	for x in range(0, len(grid[0])):
		for y in range(0, len(grid)):
			#Dead cell
			aliveNeighbors = 0
			if grid[y][x] == OFF:
				if grid[y-1][x-1] == ON and y>0 and x>0:
						aliveNeighbors += 1
				if grid[y-1][x] == ON and y>0: 
						aliveNeighbors += 1
				try:
					if grid[y-1][x+1] == ON and y>0:
						aliveNeighbors += 1
				except IndexError:
					pass
				if grid[y][x-1] == ON and x>0:
						aliveNeighbors += 1
				try:
					if grid[y][x+1] == ON:
						aliveNeighbors += 1
				except IndexError:
					pass
				try:
					if grid[y+1][x-1] == ON and x>0:
						aliveNeighbors += 1
				except IndexError:
					pass
				try:
					if grid[y+1][x] == ON:
						aliveNeighbors += 1
				except IndexError:
					pass
				try:
					if grid[y+1][x+1] == ON:
						aliveNeighbors += 1
				except IndexError:
					pass
				if aliveNeighbors==3:
					newGrid[y][x] = ON
				else:
					newGrid[y][x] = OFF
					
			else:
				if grid[y-1][x-1] == ON and y>0 and x>0:
						aliveNeighbors += 1
				if grid[y-1][x] == ON and y>0: 
						aliveNeighbors += 1
				try:
					if grid[y-1][x+1] == ON and y>0:
						aliveNeighbors += 1
				except IndexError:
					pass
				if grid[y][x-1] == ON and x>0:
						aliveNeighbors += 1
				try:
					if grid[y][x+1] == ON:
						aliveNeighbors += 1
				except IndexError:
					pass
				try:
					if grid[y+1][x-1] == ON and x>0:
						aliveNeighbors += 1
				except IndexError:
					pass
				try:
					if grid[y+1][x] == ON:
						aliveNeighbors += 1
				except IndexError:
					pass
				try:
					if grid[y+1][x+1] == ON:
						aliveNeighbors += 1
				except IndexError:
					pass
				if aliveNeighbors==2 or aliveNeighbors==3:
					newGrid[y][x] = ON
				else:
					newGrid[y][x] = OFF
	return newGrid

stillLives =["block", "bee-hive", "loaf", "boat", "tub"]
oscillators = ["blinker", "toad", "beacon", "pulsar", "penta-decathlon"]
spaceships = ["glider", "light-weight spaceship (LWSS)", "middle-weight spaceship (MWSS)", "heavy-weight spaceship (HWSS)"]
advanced = ["gosper glider gun (gosper)"]

def main():
	print("Welcome to Conway's game of life, by Álvaro Szigethi Marcos")
	width, height = input("Please input the width and height you want in your grid (i.e 20 10):\n").split()
	grid = initializeGrid(int(width), int(height))
	printGrid(grid)
	inputsDone = False
	structures = {}
	while inputsDone == False:
		struct = input('Please input what type of structure you want:\nStill, Oscillator, Spaceship, Advanced\nIf done selecting type "done"\n')
		if struct == "done":
			inputsDone = True
		#Oscillators
		elif struct.lower() == "oscillator":
			allStructs = ""
			for word in oscillators:
				allStructs += word
				if word != "penta-decathlon":
					allStructs+=", "
			done = False
			while done == False:
				option = input(f'The available options are: {allStructs}\nIf done selecting type "done"\n')
				if option == "done":
					done = True
				elif option.lower() == "blinker":
					x, y = input("Please input the x and y values you want your blinker to be in (i.e 20 10):\n").split()
					addBlinker(int(x), int(y), grid)
				elif option.lower() == "toad":
					x, y = input("Please input the x and y values you want your toad to be in (i.e 20 10):\n").split()
					addToad(int(x), int(y), grid)
				elif option.lower() == "beacon":
					x, y = input("Please input the x and y values you want your beacon to be in (i.e 20 10):\n").split()
					addBeacon(int(x), int(y), grid)
				elif option.lower() == "pulsar":
					x, y = input("Please input the x and y values you want your pulsar to be in (i.e 20 10):\n").split()
					addPulsar(int(x), int(y), grid)
				elif option.lower() == "penta-decathlon":
					x, y = input("Please input the x and y values you want your penta-decathlon to be in (i.e 20 10):\n").split()
					addPenta(int(x), int(y), grid)
				else:
					print("Wrong input, please try again:\n")
		#Still lives
		elif struct.lower() == "still":
			allStructs = ""
			for word in stillLives:
				allStructs += word
				if word != "tub":
					allStructs+=", "
			done = False
			while done == False:
				option = input(f'The available options are: {allStructs}\nIf done selecting type "done"\n')
				if option == "done":
					done = True
				elif option.lower() == "block":
					x, y = input("Please input the x and y values you want your block to be in (i.e 20 10):\n").split()
					addBlock(int(x), int(y), grid)
				elif option.lower() == "bee-hive":
					x, y = input("Please input the x and y values you want your bee-hive to be in (i.e 20 10):\n").split()
					addBeehive(int(x), int(y), grid)
				elif option.lower() == "loaf":
					x, y = input("Please input the x and y values you want your loaf to be in (i.e 20 10):\n").split()
					addLoaf(int(x), int(y), grid)
				elif option.lower() == "boat":
					x, y = input("Please input the x and y values you want your boat to be in (i.e 20 10):\n").split()
					addBoat(int(x), int(y), grid)
				elif option.lower() == "tub":
					x, y = input("Please input the x and y values you want your tub to be in (i.e 20 10):\n").split()
					addTub(int(x), int(y), grid)
				else:
					print("Wrong input, please try again:\n")
		#Spaceships
		elif struct.lower() == "spaceship":
			allStructs = ""
			for word in spaceships:
				allStructs += word
				if word != "heavy-weight spaceship (HWSS)":
					allStructs+=", "
			done = False
			while done == False:
				option = input(f'The available options are: {allStructs}\nIf done selecting type "done"\n')
				if option == "done":
					done = True
				elif option.lower() == "glider":
					x, y = input("Please input the x and y values you want your glider to be in (i.e 20 10):\n").split()
					addGlider(int(x), int(y), grid)
				elif option.lower() == "lwss":
					x, y = input("Please input the x and y values you want your light-weight spaceship to be in (i.e 20 10):\n").split()
					addLWSS(int(x), int(y), grid)
				elif option.lower() == "mwss":
					x, y = input("Please input the x and y values you want your middle-weight spaceship to be in (i.e 20 10):\n").split()
					addMWSS(int(x), int(y), grid)
				elif option.lower() == "hwss":
					x, y = input("Please input the x and y values you want your heavy-weight spaceship to be in (i.e 20 10):\n").split()
					addHWSS(int(x), int(y), grid)
				else:
					print("Wrong input, please try again:\n")
		#Advanced
		elif struct.lower() == "advanced":
			allStructs = ""
			for word in advanced:
				allStructs += word
				if word != "gosper glider gun (gosper)":
					allStructs+=", "
			done = False
			while done == False:
				option = input(f'The available options are: {allStructs}\nIf done selecting type "done"\n')
				if option == "done":
					done = True
				elif option.lower() == "gosper":
					x, y = input("Please input the x and y values you want your gosper glider gun to be in (i.e 20 10):\n").split()
					gosperGliderGun(int(x), int(y), grid)
				else:
					print("Wrong input, please try again:\n")
		else:
			print("Wrong input, please try again:\n")

	while(1==1):
		print(f"\n\n\n\n\n")
		printGrid(grid)
		time.sleep(.1)
		grid = update(grid)

	
if __name__ == '__main__': 
	main() 