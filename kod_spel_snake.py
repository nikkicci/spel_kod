#!pygame/bin/python
import pygame
import random

# Define some size constants used by the game. A 30x30 grid, where each cell will be 20x20 pixels
playfieldSize = (30,30)
scale = 20

# Initialize pygame
pygame.init()
pygame.display.set_caption('Snake')

# Helper function to quit the game
def die():
	pygame.quit()
	quit()

# Define some color constants for example Green: (0,255,0)
class Colors:
	BACKGROUND = pygame.Color(0,0,0)
	SNAKE = pygame.Color(255,100,180)
	FOOD = pygame.Color(255,255,255)

# Define a class representing a direction
class Direction:
	UP = 0
	RIGHT = 1
	DOWN = 2
	LEFT = 3

	def isOppositeDirection(dirA, dirB):
		return (dirA+2)%4 == dirB;

# Define a snake class
#
# Properties of a snake:
# - direction (One of UP,DOWN,LEFT or RIGHT, defined above)
# - body (A list of tuples, where each tuple has an X and Y coordinate)
class Snake:
	# Initialize a snake at startPosition (x,y) and a length
	# The snake will always start in the UP direction
	# The body will always go down initally.
	def __init__(self, startPosition, length):
		self.direction = Direction.UP
		self.body = [startPosition]

		# Create the body by appending position tuples downwards
		for i in range(1, length):
			self.body.append((startPosition[0], startPosition[1]+i))

	# Helper method to change direction of the snake, but only if the direction
	# is NOT opposite to the current direction
	def changeDirection(self, direction):
		if not Direction.isOppositeDirection(direction, self.direction):
			self.direction = direction

	# Helper function to move the snake
	#
	# Prepend a new head in the direction of the current head
	# Optionally cut the tail
	def move(self, grow):
		# Current head position
		x = self.body[0][0]
		y = self.body[0][1]

		# Prepend new head
		match self.direction:
			case Direction.UP:
				self.body.insert(0, (x, y-1))
			case Direction.RIGHT:
				self.body.insert(0, (x+1, y))
			case Direction.DOWN:
				self.body.insert(0, (x, y+1))
			case Direction.LEFT:
				self.body.insert(0, (x-1, y))

		# Cut the tail
		if not grow:
			self.body.pop()

# Define a class that represents the playfield
# The playfield has a snake and a food snack
class Playfield:
	# Initialize the playfield with a certain size tuple (width, height)
	def __init__(self, size):
		self.size = size

		# Spawn the snake in the middle, and have a default body length of 4
		self.snake = Snake((size[0]/2, size[1]/2), 4)

		self.spawnFood()

	# Method to randomly spawn food
	def spawnFood(self):
		# Try forever...
		while True:
			# A random position within the current playfield
			position = (random.randrange(0, self.size[0]), random.randrange(0,self.size[1]))

			# ...as long as the position overlaps the snake body
			if not position in self.snake.body:
				break

		# Found a clear location, assign the new food position
		self.foodPosition = position

	# Method to draw the playfield onto the screen
	def render(self):
		# First clear with background
		gameWindow.fill(Colors.BACKGROUND)

		# Then draw each snake body cell as a rectangle with size scale
		for pos in self.snake.body:
			pygame.draw.rect(gameWindow, Colors.SNAKE, pygame.Rect(pos[0]*scale, pos[1]*scale, scale, scale))

		# Then draw the food, also as a rectangle with size scale
		pygame.draw.rect(gameWindow, Colors.FOOD, pygame.Rect(self.foodPosition[0]*scale, self.foodPosition[1]*scale, scale, scale))

	# Method to check for collisions
	def checkCollisions(self):
		head = self.snake.body[0]

		# Is the head on the food position?
		if head == self.foodPosition:
			return 'FOOD'

		# Is the head outside the playfield?
		x = head[0]
		y = head[1]
		if x < 0 or x >= self.size[0] or y < 0 or y >= self.size[1]:
			return 'EDGE'

		# Is the head on the body?
		if head in self.snake.body[1:]:
			return 'BODY'

		# No collision
		return '';

# Initialize the playfield
playfield = Playfield(playfieldSize)

# Create a game window that is scale times bigger than the playfield
gameWindow = pygame.display.set_mode((playfield.size[0]*scale, playfield.size[1]*scale))

# Create a clock to have timing control
fps = pygame.time.Clock()


# Helper function to check for keyboard strokes
# Return True if a key was handled, otherwise False
def handleKeyboard(event):
	match event.key:
		case pygame.K_ESCAPE:
			die()

		case pygame.K_UP:
			playfield.snake.changeDirection(Direction.UP)
			return True

		case pygame.K_DOWN:
			playfield.snake.changeDirection(Direction.DOWN)
			return True

		case pygame.K_LEFT:
			playfield.snake.changeDirection(Direction.LEFT)
			return True

		case pygame.K_RIGHT:
			playfield.snake.changeDirection(Direction.RIGHT)
			return True

	return False

# Main game loop
while True:
	# Check for input events
	for event in pygame.event.get():
		# Dispatch keyboard stokes to the helper function above
		if event.type == pygame.KEYDOWN:
			if handleKeyboard(event):
				# Abort handling events if a key was handled, to ensure that we don't
				# capture multiple key strokes per frame (i.e. a quick turn into the snake body)
				break

	# Check for collisions
	match playfield.checkCollisions():
		# Die on edge collision
		case 'EDGE':
			die()

		# Die on self-body collision
		case 'BODY':
			die()

		# Spawn new food on food collision
		# Move snake, but keep tail (i.e. it grows by 1)
		case 'FOOD':
			playfield.spawnFood()
			playfield.snake.move(True)

		# No collision. Just move the snake
		case _:
			playfield.snake.move(False)

	# Draw everything to the screen
	playfield.render()

	# Show it, and wait a bit
	pygame.display.update()
	fps.tick(5)
	
    
