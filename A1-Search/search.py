# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    # this does not return the solution with the least cost
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()
    from util import Stack

    currentState = problem.getStartState()
    openStack = Stack()
    openStack.push(([currentState], [],0))
    while not openStack.isEmpty():
        currStates, currPath, currCost = openStack.pop()
        stateToExpand = currStates[-1]
        if problem.isGoalState(stateToExpand):
            return currPath
        for successor, direction, stepCost in problem.getSuccessors(stateToExpand):
            if successor not in currStates:
                # if the successor is not in the currPath
                newPath = currPath + [direction]
                newStates = currStates + [successor]
                openStack.push((newStates, newPath, currCost + stepCost))
    return []

"""
def breadthFirstSearch(problem):
    # Search the shallowest nodes in the search tree first.
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()
    from util import Queue
    
    openStack = Queue()
    startState = problem.getStartState()
    seenStates = {startState: 0}
    expandedStates = set()
    openStack.push(([startState], [],0))
    while not openStack.isEmpty():
        currStates, currPath, cost = openStack.pop()
        stateToExpand = currStates[-1]
        # stateToExpand must be in the seenStates
        if stateToExpand not in expandedStates or seenStates[stateToExpand] > cost:
            seenStates[stateToExpand] = cost
            expandedStates.add(stateToExpand)
            for successor, direction, stepCost in problem.getSuccessors(stateToExpand):
                if problem.isGoalState(successor):
                    # if the successor is the goal state
                    currPath.append(direction)
                    return currPath
                # if the successor is not the goal state
                if successor not in seenStates or seenStates[successor] > cost + stepCost:
                    seenStates[successor] = cost + stepCost
                    newStates = currStates + [successor]
                    newPath = currPath + [direction]
                    openStack.push((newStates, newPath, cost + stepCost))
    return []
"""            


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    from util import Queue
    openQueue = Queue()
    startState = problem.getStartState()
    openQueue.push(([startState], [], 0))
    seenStates = {startState: 0}
    while not openQueue.isEmpty():
        currStates, currPath, cost = openQueue.pop()
        stateToExpand = currStates[-1]
        if cost <= seenStates[stateToExpand]:
            # update the minimum cost to the stateToExpand
            seenStates[stateToExpand] = cost
            if problem.isGoalState(stateToExpand):
                return currPath
            for successor, direction, stepCost in problem.getSuccessors(stateToExpand):
                if successor not in seenStates or stepCost + cost < seenStates[successor]:
                    newPath = currPath + [direction]
                    newStates = currStates + [successor]
                    openQueue.push((newStates, newPath, cost + stepCost))
                    seenStates[successor] = cost + stepCost
    return []



def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()
    from util import PriorityQueue
    
    openPriQue = PriorityQueue()
    startState = problem.getStartState()
    openPriQue.push(([startState], [], 0), 0)
    seenStates = {startState: 0}
    while not openPriQue.isEmpty():
        currStates, currPath, cost = openPriQue.pop()
        stateToExpand = currStates[-1]
        if cost <= seenStates[stateToExpand]:
            # update the minimum cost to the stateToExpand
            seenStates[stateToExpand] = cost
            if problem.isGoalState(stateToExpand):
                return currPath
            for successor, direction, stepCost in problem.getSuccessors(stateToExpand):
                if successor not in seenStates or stepCost + cost < seenStates[successor]:
                    newPath = currPath + [direction]
                    newStates = currStates + [successor]
                    openPriQue.push((newStates, newPath, cost + stepCost), cost + stepCost)
                    seenStates[successor] = cost + stepCost
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()
    
    from util import PriorityQueue
    openAStar = PriorityQueue()
    startState = problem.getStartState()
    # currStates, currPath, currPathCost
    # priority : (f(n), h(n), c(n))
    openAStar.push(([startState], [], 0), (0 + heuristic(startState, problem),heuristic(startState, problem),0))
    seenStates = {startState : 0}
    while not openAStar.isEmpty():
        currStates, currPath, currPathCost = openAStar.pop()
        stateToExpand = currStates[-1]
        if currPathCost <= seenStates[stateToExpand]:
            seenStates[stateToExpand] = currPathCost
            if problem.isGoalState(stateToExpand):
                return currPath
            for successor, direction, stepCost in problem.getSuccessors(stateToExpand):
                if successor not in seenStates or currPathCost + stepCost < seenStates[successor]:
                    newPath = currPath + [direction]
                    newStates = currStates + [successor]
                    openAStar.push((newStates, newPath, currPathCost + stepCost), (currPathCost + stepCost + heuristic(successor, problem), heuristic(successor, problem), currPathCost + stepCost))
                    seenStates[successor] = currPathCost + stepCost
    return []
    

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
