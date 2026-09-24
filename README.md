# Tic-Tac-Toe Game in Python

This is my first Python project. I built a Tic-Tac-Toe game where a human player can play against the computer.

While making this project, I used the Python concepts that I had learned and gradually improved the computer's decision-making algorithm.

## 1. Things I Used

* Python
* Functions
* Lists
* Loops
* Conditions
* Recursion
* Backtracking
* Minimax algorithm
* Alpha-Beta Pruning
* `copy` module

## 2. How the Game Works

The player uses `X` and the computer uses `O`.

The game checks:

* Whether a player has won
* Whether the game is a draw
* Which positions are available
* Which move the computer should play

For the computer's moves, I used the **Minimax algorithm**.

The computer simulates possible future moves and evaluates the possible results before choosing its move.

## 3. Why I Chose Minimax

I chose Minimax because I wanted to understand how a computer can make decisions by looking at possible future moves.

I also considered approaches such as **Reinforcement Learning (RL)**, but decided not to use RL for this project.

Since Tic-Tac-Toe has a relatively small number of possible game situations, Minimax allows me to directly understand the decision-making process.

Through this, I learned about:

* Recursion
* Game-state evaluation
* Simulating possible moves
* Backtracking
* Decision-making
* Searching through possible future states

I wanted to understand the logic behind the computer's decisions instead of using a pre-trained model or a library that already solves the game.

## 4. Main Parts of the Project

### `display_board()`

Displays the current board to the user.

### `win()`

Checks whether:

* `X` has won
* `O` has won
* The game is still running
* The game is a draw

### `get_available_move()`

Finds all currently empty positions on the board.

### `make_move()`

Places a player's move on the actual game board.

### `score()`

Evaluates the current game state:

* `O` wins → `1`
* `X` wins → `-1`
* Draw → `0`

### `minimax()`

This is the main decision-making function.

It recursively explores possible future game states and determines the best result assuming both players make optimal decisions.

The basic process is:

**Make a move → Explore future moves → Reach an ending → Return the score → Undo the move**

### `best_move()`

Uses Minimax to determine which move the computer should make.

The computer tries to maximize its score while assuming that the human player will try to minimize it.

## 5. Improvements During Development

I did not build the final version all at once. I improved the algorithm step by step.

### Version 1 — Minimax + `deepcopy()`

Initially, I created a separate copy of the board for every simulated move using `copy.deepcopy()`.

This worked, but it required creating many additional board objects.

### Version 2 — Minimax + Backtracking

I changed the implementation to reuse the same board.

The basic pattern became:

**MAKE → RECURSE → UNDO**

Instead of creating a new board for every possible move, the program temporarily changes a position, explores the result, and then restores the position.

This significantly reduced the execution time and extra memory required for creating board copies.

### Version 3 — Alpha-Beta Pruning

I then added **Alpha-Beta Pruning** to Minimax.

Alpha-Beta Pruning avoids exploring branches that cannot affect the final decision.

The important idea is:

* **Alpha** → best result currently available for `O` (MAX)
* **Beta** → best result currently available for `X` (MIN)
* If `alpha >= beta`, further exploration of that branch can be stopped.

This improves the efficiency of Minimax without changing the final Minimax result.

## 6. Challenges I Faced

### Understanding Minimax

The hardest part was understanding recursion inside the game.

At first, it was confusing because the function repeatedly calls itself while creating possible future game situations.

The approach that helped me was:

**Make a possible move → check what can happen next → continue until the game ends → return the result**

### Understanding Backtracking

I initially used `deepcopy()` to simulate moves.

Later, I learned that I could reuse the same board by:

1. Making a temporary move
2. Recursively exploring it
3. Undoing the move

This helped me understand the **Make → Recurse → Undo** pattern.

### Understanding Alpha-Beta Pruning

Another challenge was understanding how Alpha and Beta work together.

I learned that pruning is not about finding a specific score such as `1` or `-1`.

Instead, it uses **bounds** to determine when exploring another branch is unnecessary.

### Finding Bugs

I also encountered several bugs while connecting the functions together, including:

* Returning the correct result from Minimax
* Choosing the correct best move
* Handling tuples returned by `win()`
* Tuple unpacking
* Correctly modifying and restoring the board
* Passing Alpha and Beta through recursive calls
* Testing different game situations

Fixing these bugs helped me understand how data moves between functions and how recursive programs behave.

## 7. What I Learned

While making this project, I became more comfortable with:

* Breaking a problem into functions
* Working with lists
* Recursion
* Backtracking
* Game-state evaluation
* Searching possible future states
* Debugging
* Understanding object references
* Using `deepcopy()`
* Optimizing a recursive algorithm
* Understanding Minimax
* Understanding Alpha-Beta Pruning

Most importantly, I learned that an algorithm can often be improved by understanding **what work is unnecessary**, rather than simply making the computer do the same work faster.

## 8. Current Status

The Tic-Tac-Toe game and computer player are working.

The project currently uses:

* Minimax
* Backtracking
* Alpha-Beta Pruning

I plan to continue improving the project and experimenting with different optimization techniques.

## 9. How to Run

```bash
python tic_tac_toe.py
```
