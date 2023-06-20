# snake-game
Python 100 Days of Code: Day 20 and Day 21

There were a lot of different pieces to building the Snake Game. Looking back, it was not really complicated. 
What got this to work was a knowledge of Python concepts (classes, inheritance, slicing) + understanding the Turtle library (distance) and then some cool bits of logic. 

Classes allowed for a clear separation of concerns
* Main.py - Manage control flow 
* Snake - Attributes and methods related to the Snake
* Food -  Attributes and methods related to the Food object that should keep popping up to help the snake grow longer
* Scoreboard - Constants and methods to increase the score, write the score to the screen, and announce when the game has ended

Key pieces of logic: 
* Treating the snake as one long array of segments (each a turtle)
* Snake motion is achieved by moving each segment to the position of the one ahead of it, essentially all following the head but moving from the rear
* Controlling when the screen is updated - so we don't see transitory states
* Collisions with the food, walls, and the snake itself is tracked using the turtle distance method


This was a fun exercise - my learning style is to follow along the Udemy course, write code ahead of time when I can see what the requirements are, and then clean up my code 
to match that of the instructors. So if my code matches that of the instructors, in at least a few cases, I have made an attempt to solve the problem first. 

Thank you for reading. The End. 🐍
