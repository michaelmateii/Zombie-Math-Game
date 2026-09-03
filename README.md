# Zombie Math Game

A small Python terminal game I built as part of my programming studies.

The player answers math questions and chooses between doors while trying to avoid zombies.

## Features

- Multiplication, integer division and modulo questions
- Randomized math questions
- Randomized zombie doors
- Input validation
- Adjustable number of questions
- Replay system
- Keeps the same game settings after a loss
- Lets the player choose new settings after completing the game

## How It Works

The player first chooses the number of questions and a mathematical operation.

For each round, the player must answer a math question correctly and then choose a door. One of the doors contains zombies. Choosing the wrong door or answering a question incorrectly ends the game.

The number of doors decreases as the player progresses.

## How to Run

Make sure Python 3 is installed.

```bash
python3 zombie_math_game.py
```

No external Python packages are required.

## What I Practiced

This project gave me practice with:

- Functions
- Loops and conditionals
- User input and validation
- Dictionaries
- Randomization
- Error handling
- Basic game state