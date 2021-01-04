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

 