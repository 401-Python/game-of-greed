## Lab 06: Game of Greed

### Author: Alvian Joseph

### Links and Resources
* [PR](https://github.com/401-Python/game-of-greed)
* [![Build Status]()
* [front end]()

### Tasks
Today is all about tackling the highest risk features - scoring and the game flow.
Define a Game class.
Handle calculating score for dice roll
Add calculate_score instance method to Game class.
The input to calculate_score is a tuple of integers that represent a dice roll.
The output from calculate_score is an integer representing the roll’s score according to rules of game.
Begin work on verifying the game proceeds according to game flow
Add play instance method to Game class
Ensure that the initial game flow is followed
Greet user by printing ‘Welcome to Game of Greed’
Prompt user with ‘Wanna play?’
if user enters ‘y’ then print ‘Great! Check back tomorrow :D’
if user enters anything else print ‘OK. Maybe another time’
NOTE: use Dependency Injection to handle input/output.

### Modules
#### game_of_greed.py
  #### methods
  * ```calculate_score()```
  This method takes in a tuple of 6 integers representing a random dice roll
  Using the rules of Game of Greed, scoring scenario is calculated using a combination of
  Conditions and the collections.Counter method. The score is stored in a variable and tracked through all the scenarios, then returned once all conditions have failed or passed.





### Testing
  pytest
  ptw
  

