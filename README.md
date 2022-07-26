
# Object Oriented Python: Battleship Game

Welcome,

Everyone knows the game of **Battleship** and is familiar with the rules. You will find here a representation of the Battleship game run through a Python terminal. This terminal is running on Heroku.

The purpose of the game is for the users to find all the computer ships (5 ships) before the player runs out of tries/bullets/guesses. The player has ten guesses to find as many ships as possible. The player with the most hits at the end of the ten guesses is the winner. Each ship occupies one square on the grid.

[View the live version of the programme running on Heroku]()

![opening page](Assets/images/enter-name.png)

## Table of Contents

- [How to play](#how-to-play)
- [Features](#features)
    - [Implemented features](#implemented-features)
    - [Future Features](#future-features)
- [Data Model](#data-model)
- [Testing](#testing)
    - [User Goals](#user-goals)
    - [Technology](#technology)
- [Bugs](#bugs)
    - [Fixed Bugs](#fixed-bugs)
    - [Validator Testing](#validator-testing)
- [Testing](#testing)
- [Credits](#credits)

## How to play
Battleship is a turn-based naval strategy game. Originally known as a pencil and paper game, the game has evolved in its format and has its own variations. You can find out more about this game and its history on its [Wikipedia page](https://en.wikipedia.org/wiki/Battleship_(game)#:~:text=Battleship%20(also%20known%20as%20Battleships,concealed%20from%20the%20other%20player.).

In this version of the game, the player sees the guess board. This is a one player game where the player has to try and sink all the ennemy ships before he is running out of tries. 

Each turn, the user will be select to select a row and a column that will work as coordinates to target a location on the grid. The outcome of this selection will display a "O" for a missed shot, or water, or a "X" for a hit. Locations that have not been hit yet are marked on the grid by a "_".

## Features

### Implemented features

- Introduction message explaining the programme, the board size, number of ships and requesting players name:

![intro message](Assets/images/generating-boards.png)

- The grid with the numbers for the rows and the letters for the columns to guide the player in how to select locations. The printing will iterate for the number of columns. The 5 enemy ships are randomly generated on the grid (but of course not displayed):


![enter-col](Assets/images/enter-col.png)

- asks player to input a column number


![enter-row](Assets/images/enter-row.png)

- asks player to enter row number

- Logic to verify the input for rows and columns.
    - Verifies if the row input is an integer.
    - Converts the row input in coordinates (substracts 1)
    - Verifies if the column is a letter.
    - Converts the letter in a number.
    - Returns error message to player

![invalid-shot](Assets/images/invalid-shot.png)


- Outcome logic after input has been validated
    - Verifies if the selected coordinates have not been previously hit.
    - Checks on the grid if an ennemy ship is located there.
    - Checks on the grid if it is an empty location. 
    - Reduces the count of tries left by one.

![player-hit](Assets/images/player-hit.png)
![misses](Assets/images/misses.png)

### Future Features

Imagination can go a long way. Battleship, through its variations, is a good display of that. Due to time constraints, I could not implement all the features I wanted to make available for the players. These features may be released in future updates:

-  Add a player grid to display the ships,
-  Add different ship lengths and allow different directions for ship placement,

## Data Model
 

## Testing

- PEP8
    - No problems were identified from [PEP8 Online Check]

### User goals
Users should be able to have the following goals

- On opening the game I should have clear instructions on how the game works.
- The rules of the game should be explained.
- The game should tell me how and what co-ordinates I can choose.
- I should be told if I enter invalid co-ordinates.
- I should be told if I have already selected those co-ordinates.
- I should be told how many tries I have left.
- I should be told the results of each round.
- At the end of the game I want to be notified of the winner/ looser of the game.

**Goal**                               
The above user goals are listed the following are the outcomes for the user goals.

- the instructions on who the game works are listed at the start of the game.
- the rules are also explained at the start of the game.
- The game informs the user of the number of rows and the number of columns on the play board
- If an invalid row or colunm number is entered the player will be presented with a invalid data selection messageed and will be asked to re-enter a correct value.
- after each selection the player will be informed if their attempt was a hit or a miss 
- after each selection the player will be informed of the computers attempt if it was a hit or a miss.
- the player will be informed of how many remaining attemptys they have in the game.
- at the end of the game the player will be notified that this is the end of the game and will be told of the result of the game.

### Technology

The code is passing the PEP8 linter validation. No errors were identified. 

## Bugs

### Fixed Bug
- Board not working for computer (incorect spelling)
- Error in code to validate player hit.(incorect indenting)

### Validator testing

- PEP8
    - No problems were identified from [PEP8 Online Check]![testing](Assets/images/Testing.png)

## Deployment

This project was deployed using Code Institute's mock terminal for Heroku.

  - Steps for deployment:
    - Create a copy of the [Python Essentials Template](https://github.com/Code-Institute-Org/python-essentials-template) repository
    - Freeze the requirements.txt
    - Create a new [Heroku](https://dashboard.heroku.com/apps) app.
    - Set the buildbacks to `Python` and `NodeJS` in that order.
    - Link the Heroku app to the repository (in the read.me)
    - Click on `__Deploy__`.

## Credits

- Several ressources were identified in helping creating the Battleship game. 
- code institute love sandwiches was used to form the basic structure of this code.
- youtube content - https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=124s
- My good friend Tom who sat with me and helped me review code and assisted me through out this project with out who this project would not have been 
- My mentor, Martina. Always looking after me with helpful resources and comments.
- [Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game)) for the rules and history of the Battleships game