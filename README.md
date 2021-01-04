# PacMan-A1-Search

### For details, please see `PacManSearch-Introduction.pdf` under `/A1-Search`

## Question 1: Finding a Fixed Food Dot using Depth First Search

Implement the depth-first search (DFS) algorithm in the `depthFirstSearch` function in `search.py`. To ensure that DFS does not run around in circles, implement path checking to prune cyclic paths during search. No full cycle checking for DFS



Implementation will produce a quick solution for:

`python pacman.py -l tinyMaze -p SearchAgent`

`python pacman.py -l mediumMaze -p SearchAgent`

`python pacman.py -l bigMaze -z .5 -p SearchAgent`



## Question 2: Breadth First Search

Implement the breadth-first search (BFS) algorithm in the `breadthFirstSearch` function in `search.py` with full cycle checking.



Implementation will produce a quick solution for:

`python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs`

`python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5`

`python eightpuzzle.py`

## Question 3: Varying the Cost Function

Implement the uniform-cost search algorithm with full cycle checking in the `uniformCostSearch` function in `search.py`



Implementation will produce a quick solution for:

`python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs`

`python pacman.py -l mediumDottedMaze -p StayEastSearchAgent`

`python pacman.py -l mediumScaryMaze -p StayWestSearchAgent`

## Question 4: A* search

Implement A* search with full cycle checking in the empty function `aStarSearch` in `search.py`. A* takes a heuristic function as an argument. Heuristics take two arguments: a state in the search problem (the main argument), and the problem itself (for reference information). The `nullHeuristic` heuristic function in `search.py` is a trivial example.



A* implementation can be tested on the original problem of finding a path through a maze to a fixed position using the Manhattan distance heuristic (implemented already as `manhattanHeuristic` in `searchAgents.py`).

`python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic`

## Question 5: Finding All the Corners

In *corner mazes*, there are four dots, one in each corner. A new search problem is to find the shortest path through the maze that touches all four corners (whether the maze actually has food there or not). 



Implementation will able to solve: 

`python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem`

`python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem`

## Question 6: Corners Problem: Heuristic

Implement a non-trivial, admissible heuristic for the `CornersProblem` in `cornersHeuristic`



Implementation can solve the medium Corners Problem with at most 900 nodes expanded

```
python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5
```

*Note:*  ` AStarCornersAgent` is a shortcut for

`-p SearchAgent -a fn=aStarSearch,prob=CornersProblem,heuristic=cornersHeuristic`

## Question 7: Eating All The Dots

A solution is defined to be a path that collects all of the food in the Pacman world. For the present assignment, solutions do not take into account any ghosts or power pellets; solutions only depend on the placement of walls, regular food and Pacman. 

Fill in `foodHeuristic` in `searchAgents.py` with an admissible heuristic for the `FoodSearchProblem`

Implementation can solve:

`python pacman.py -l trickySearch -p AStarFoodSearchAgent` with at most 7000 nodes expanded

`python pacman.py -l oneDotFocus -p AStarFoodSearchAgent` with at most 70 nodes expanded

`python pacman.py -l largeGrid -z 0.25 -p AStarFoodSearchAgent` with at most 360 nodes expanded



## Question 8: Suboptimal Search

Implement the function `findPathToClosestDot` in `searchAgents.py`. The agent solves this maze (suboptimally!) in under a second with a path cost of 350:

`python pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5 `



#### Run all questions with auto grader, please go to `/A1-Search` and run `python autograder.py`

 





# PacMan-A2-Game Tree Search

### For details, please see `PacManSearch-GameTreeSearch.pdf` under `/A2-GameTreeSearch`



### Question 1: Reflex Agent

Improve the `ReflexAgent` in `multiAgents.py` to play respectably. The provided reflex agent code provides some helpful examples of methods that query the `GameState` for information. A capable reflex agent will have to consider both food locations and ghost locations to perform well.



Implementation will easily and reliably clear `testClassic` layout and `mediumClassic` layout

`python3 pacman.py -p ReflexAgent -l testClassic`

`python3 pacman.py --frameTime 0 -p ReflexAgent -k 1`

`python3 pacman.py --frameTime 0 -p ReflexAgent -k 2`



The agent will be able to get an average more than 1000 points over 10 winining games



### Question 2: Minimax

Write an adversarial search agent in the provided `MinimaxAgent` class stub in `multiAgents.py`. The minimax search will work with any number of ghosts. In particular, for every max layer (where the pacman moves) the minimax tree will have multiple min layers, one for each ghost.

Run`python autograder.py -q q2`

### Question 3: Alpha-Beta Pruning

Make a new agent that uses alpha-beta pruning to more efficiently explore the minimax tree, in `AlphaBetaAgent`

Run`python autograder.py -q q3`

### Question 4: Expectimax

Implement the `ExpectimaxAgent`, which is useful for modeling probabilistic behavior of agents who may make suboptimal choices.

Run`python autograder.py -q q4`

### Question 5: Evaluation Function

Write a better evaluation function for pacman in the provided function `betterEvaluationFunction`. 

The implementation will win 10 times and get an average score of at least 1000.

Run`python autograder.py -q q5`



#### Run all questions with auto grader, please go to `/A2-GameTreeSearch` and run `python autograder.py`



# PacMan-A3-CSPs

### For details, please see `PacManSearch-CSPs` under `/A3-CSPs`

### Question 1: Implementing a Table Constraint

`backtracking.py` already contains an implementation of BT (plain backtracking search) while `csp_problems.py` contains an implementation of the nQueens problem. Try running

`python nqueens.py 8`

to solve the 8 queens problem using BT. If you run

`python nqueens.py -c 8`

the program will find all solutions to the 8-Queens problem. Try

`python nqueens.py --help`

to see the other arguments you can use. (However, you haven't implemented FC nor GAC yet, so you can't use these algorithms yet.) Try some different small numbers with the '-c' option, to see how the number of solutions grows with the number of Queens. Also observe that even numbered queens are generally faster to solve, and the time to find a single solution for 'BT' grows quite quickly. Observe the number of nodes explored. Later once you have FC and GAC implemented you will see that they explore fewer nodes.

For this question look at `constraint.py`. There you will find the class `QueensTableConstraint` that you have to implement for this question. This class creates a table constraint to capture the nQueens constraint. Once you have that implemented you can run

`python nqueens.py -t 8`

to solve the nQueens CSP using your table constraint implementation. Check a number of sizes and '-c' options: you should get the same solutions returned irrespective of whether or not you use '-t'. That is, your table constraint should yield the same behavior as the original `QueensConstraint`

### Question 2: Forward Checking

In `backtracking.py` you will find the unfinished function `FC`. You have to complete this function. Note that the essential subroutine `FCCheck` has already been implemented for you. Note that your implementation must deal correctly with finding one or all solutions. Check how this is done in the already implemented `BT` algorithm...just be sure that you restore all pruned values even if `FC` is terminating after one solution.

After implementing `FC` you will be able to run

`python nqueens.py -a FC 8`

to solve 8-Queens with forward checking. Solve some different sizes and check how the number of nodes explored differs from when `BT` is used.

Also try solving sudoku using the command

`python sudoku.py 1`

Which will solve board #1 using Forward Checking. Try other boards (1 to 7). Use

`python sudoku.py --help`

to see the other arguments you can use.

Also try

`python sudoku.py -a 'BT' 1`

to see how BT performs compared to FC. Finally try

`python sudoku.py -a 'FC' -c 1`

To find all solutions using FC. Check if any of the boards 1-7 have more than one solution.

Note also that if you have a sudoku board you would like to solve, you can easily add it into `sudoku.py` and solve it. Look at the code in this file to see how input boards are formatted and placed in the list `boards`. Once a new board is added to the list `boards` it can be solved with the command `python sudoku.py -a 'FC' k` where `k` is the position of the new board in the list `boards`

### Question 3: GacEnforce and GAC

In `backtracking.py` you will find unfinished `GacEnforce` and `GAC` routines. Complete these functions.

After finishing these routines you will be able to run

`python nqueens.py -a GAC 8`

Try different numbers of Queens and see how the number of nodes explored differs from when you run `FC`.

Does `GAC` also take less time than `FC` on `sudoku`? What about on `nqueens`?

Now try running

`python sudoku.py -e 1`

which will not do any backtracking search, it will only run `GacEnforce` at the root.

Try running only `GacEnforce` on each board to see which ones are solved by only doing `GacEnforce`.

### Question 4: AllDiff for Sudoku

In `csp_problems.py` you will find the function `sudokuCSP`. This function takes a `model` parameter that is either `'neq'` or `'alldiff'`. When `model == 'neq'` the returned CSP contains many binary not-equals constraints. But when `model == 'alldiff'` the model should contain 27 allDifferent constraints.

Complete the implementation of `sudokuCSP` so it properly handles the case when `model == 'alldiff'` using allDifferent constraints instead of binary not-equals.

------

### Question 5: NValues Constraint

The `NValues` Constraint is a constraint over a set of variables that places a lower and an upper bound on the number of those variables taking on value from a specified set of values.

In `constraints.py` you will find an incomplete implementation of `class NValuesConstraint`. In particular, the function `hasSupport` has not yet been implemented. Complete this implementation.

------

### Question 6: Plane Scheduling

Implement a solver for the following plane scheduling problem by encoding the problem as a CSP and using your already developed code to find solutions.

#### Run all questions with auto grader, please go to `/A3-CSPs` and run `python autograder.py`

