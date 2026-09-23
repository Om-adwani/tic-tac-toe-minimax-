# Tic-Tac-Toe Game in Python

This is my first Python project. I built a Tic-Tac-Toe game where a human player can play against the computer.

While making this project, I used the Python concepts that I had learned and tried to understand how they can be used together in a real project.

## 1. Things I Used While Making It

* Python
* Functions
* Lists
* Loops
* Conditions
* Recursion
* `copy` module
* Minimax algorithm

## 2. How the Game Works

The player uses `X` and the computer uses `O`.

The game checks:

* Whether a player has won
* Whether the game is a draw
* Which positions are available
* Which move the computer should play

For the computer's moves, I used the **Minimax algorithm**. The computer looks at possible moves and tries to choose a good move based on the possible results.

## 3. Why I Chose Minimax

I chose Minimax because I wanted to understand how a computer can make decisions by looking at possible future moves.

I also considered other approaches, such as **Reinforcement Learning (RL)**, but I decided not to use RL for this project.

Since Tic-Tac-Toe has a small and limited number of possible game situations, Minimax is a good way for me to understand the decision-making process directly.

Using Minimax also gave me an opportunity to learn:

* Recursion
* Game-state evaluation
* Simulating possible moves
* Choosing between different possible outcomes
* How an AI can make decisions without simply following fixed moves

I wanted to understand the logic behind the computer's decisions rather than using a pre-trained model or a library that already solves the problem.

## 4. Main Parts of the Project

### 1. `display_board()`

Its job is to display the current board data to the user.

### 2. `win()`

Its job is to check whether the computer or the human has won, whether the game is still running, or whether the game is a draw.

### 3. `get_available_move()`

It is used to find the empty positions on the board.

### 4. `make_move()`

Its job is to take a move from the user or the computer and implement it on the actual board.

### 5. `score()`

Its job is to give a score to the current game:

* If `O` wins → score is `1`
* If `X` wins → score is `-1`
* If the game is a draw → score is `0`

### 6. `minimax()`

This is the **heart of the game**.

Its job is to use the other functions to check possible future game situations and predict the best decision for the computer.

### 7. `best_move()`

Its job is to choose the move with the highest chance of winning.

If the computer cannot win, it tries to choose a move that makes sure the game does not result in a loss and can end in a draw.

## Challenges I Faced

This project was not easy for me, especially because it was one of my first projects.

### 1. Understanding Minimax

The hardest part was understanding how Minimax works.

At first, recursion inside the game was confusing because the function keeps creating new possible game situations and calling itself again.

#### What I Learned From This

The approach that helped me understand Minimax was:

**Make a possible move → check what can happen next → continue until the game ends → give the result back.**

This helped me understand how recursion can be used to look at different possible future situations.

### 2. Working With Copies of the Board

Another challenge was changing the board temporarily while checking possible moves.

I learned that if I directly changed the original board, the simulated moves could affect the actual game.

I used `copy.deepcopy()` to create a separate copy of the board before testing a move.

#### What I Learned From This

This helped me understand how Python handles objects and memory references, and why creating a separate copy of the board is important when simulating moves.

I also learned how and why `deepcopy()` can be useful in this type of problem.

### 3. Finding Bugs

I also faced many bugs while connecting all the functions together.

For example, I had problems with:

* Returning the correct result from `minimax()`
* Choosing the correct best move
* Handling the result returned by `win()`
* Tuple unpacking
* Making sure the computer's move was made on the actual board
* Testing different game situations

#### What I Learned From This

Fixing these problems helped me understand my own code better.

Instead of only looking at the error message, I started checking how the data was moving between different functions and what each function was actually returning.

## 5. What I Learned

While making this project, I learned how different Python concepts can work together in one program.

I also became more comfortable with:

* Breaking a problem into functions
* Working with lists
* Using recursion
* Creating and testing different game states
* Finding and fixing bugs
* Understanding how copies of objects work
* Understanding the basic idea behind the Minimax algorithm
* Thinking about how a computer can make decisions

## 6. Current Status

The basic Tic-Tac-Toe game and computer player are working.

I am continuing to improve the project and understand the Minimax algorithm better.

## 7. How to Run

Clone the repository and run:

```bash
python tic_tac_toe.py
```
