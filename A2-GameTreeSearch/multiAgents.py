# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        
        "*** YOUR CODE HERE ***"    
        # minimum distance from the pacman position to food
        minFoodDistance = min(manhattanDistance(newPos, food) for food in newFood.asList()) if newFood.count() != 0 else 1
        # minimum distance form the pacman position to ghost
        nearestDistanceToGhost = min(manhattanDistance(newPos, ghost.getPosition()) for ghost in newGhostStates) if len(newGhostStates) != 0 else 1
        # food should be more attractive to the pacman
        # + 1 avoid zero division error
        return successorGameState.getScore() + 3 / float(minFoodDistance+1) - 2 / float(nearestDistanceToGhost+1) 

     
def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """
    def getAction(self, gameState):
        """
        GET ACTION FOR THE PACMAN
        MultiAgentSearchAgent provides action decision for the PACMAN not the GHOSTS

        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        
        def getGhostMin(gameState, depth, agentIndex):
            nextActions = gameState.getLegalActions(agentIndex)
            if depth == self.depth or len(nextActions) == 0:
                return self.evaluationFunction(gameState)
            
            minVal = 9999999999999
            for action in nextActions:
                successorGameState = gameState.generateSuccessor(agentIndex, action)
                if agentIndex == successorGameState.getNumAgents() - 1:
                    # we are visiting the last ghost
                    # the last ghost cares about the pacman's next move 
                    value = getPacmanMax(successorGameState, depth + 1, 0)
                else:
                    # the next ghost, still on the same depth since all ghosts are at the same depth
                    value = getGhostMin(successorGameState, depth, agentIndex + 1)
                if value < minVal:
                    minVal = value

            return minVal
                    

        def getPacmanMax(gameState, depth, agentIndex):
            nextActions = gameState.getLegalActions(agentIndex)
            if depth == self.depth or len(nextActions) == 0:
                return self.evaluationFunction(gameState)
            maxVal = -9999999999
            for action in nextActions:
                successorGameState = gameState.generateSuccessor(agentIndex, action)
                # for pacman, it only cares about the movement of the adjcent ghost (ONLY ONE GHOST)
                value = getGhostMin(successorGameState, depth, 1)
                if value > maxVal:
                    maxVal = value
            return maxVal
            

        maxVal = -9999999999
        bestAction = None

        # get actions that are legal for the PACMAN
        nextActions = gameState.getLegalActions(0)
        if 0 == self.depth or len(nextActions) == 0 or gameState.isLose() or gameState.isWin():
                return self.evaluationFunction(gameState)
        for action in nextActions:
            # iterate the game state after the PACMAN takes action
            successorGameState = gameState.generateSuccessor(0, action)
            
            # no early return of winning state, since there maybe more than one wining states
            # if successorGameState.isWin():
            #     return action

            # successorGameState mimics the game state after the PACMAN takes action
            # now is the GHOST turn
            # the first GHOST action is defined by the rest ghosts
            value = getGhostMin(successorGameState, 0, 1)
            if value > maxVal:
                maxVal = value
                bestAction = action
        return bestAction
    


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        def getGhostMin(gameState, alpha, beta, depth, agentIndex):
            # get next actions for the ghost
            nextActions = gameState.getLegalActions(agentIndex)
            
            if depth == self.depth or len(nextActions) == 0:
                return self.evaluationFunction(gameState)
            
            minVal = 9999999999999
            for action in nextActions:
                successorGameState = gameState.generateSuccessor(agentIndex, action)
                if agentIndex == successorGameState.getNumAgents() - 1:
                    # we are visiting the last ghost
                    value = getPacmanMax(successorGameState, alpha, beta, depth + 1, 0)
                else:
                    value = getGhostMin(successorGameState, alpha, beta, depth, agentIndex + 1)
                
                # update beta
                if value < beta:
                    beta = value
                if value < minVal:
                    minVal = value
                # MIN node Pruning
                if value <= alpha:
                    # return the value we find that is less than alpha right away
                    # instead of self.evaluationFunction(successorGameState)
                    return value
            return minVal 
        
        def getPacmanMax(gameState, alpha, beta, depth, agentIndex):
            # get next actions for the ghost
            nextActions = gameState.getLegalActions(agentIndex)
            
            if depth == self.depth or len(nextActions) == 0:
                return self.evaluationFunction(gameState)
            
            maxVal = -9999999999999
            for action in nextActions:
                successorGameState = gameState.generateSuccessor(agentIndex, action)
                value = getGhostMin(successorGameState, alpha, beta, depth, 1)

                # update alpha
                if value > alpha:
                    alpha = value
                if value > maxVal:
                    maxVal = value
                # MAX node Pruning
                if value >= beta:
                    # return the value we find that is greater than beta right away
                    # instead of self.evaluationFunction(successorGameState)
                    return value
            return maxVal


        alpha, beta = -9999999999999, 9999999999999
        bestMove = None
        # get actions that are legal for the pacman
        nextActions = gameState.getLegalActions(0)
        if self.depth == 0 or len(nextActions) == 0 or gameState.isLose() or gameState.isWin():
            # reach to a terminal node
            return self.evaluationFunction(gameState)
        for action in nextActions:
            # generate the successor state after the pacman takes action
            successorGameState = gameState.generateSuccessor(0, action)

            # now is the ghost's turn
            value = getGhostMin(successorGameState, alpha, beta, 0, 1)
            # update alpha 
            if value > alpha:
                alpha = value
                bestAction = action
        return bestAction

        


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        def getGhostExp(gameState, depth, agentIndex):
            nextActions = gameState.getLegalActions(agentIndex)
            if depth == self.depth or len(nextActions) == 0:
                return self.evaluationFunction(gameState)
            
            sumOfValue = 0
            for action in nextActions:
                successorGameState = gameState.generateSuccessor(agentIndex, action)
                if agentIndex == successorGameState.getNumAgents() - 1:
                    value = getPacmanMax(successorGameState, depth + 1, 0)
                else:
                    value = getGhostExp(successorGameState, depth, agentIndex + 1)
                sumOfValue += value
            return sumOfValue / len(nextActions)
        
        def getPacmanMax(gameState, depth, agentIndex):
            nextActions = gameState.getLegalActions(agentIndex)
            if depth == self.depth or len(nextActions) == 0:
                return self.evaluationFunction(gameState)
            maxVal = -9999999999
            for action in nextActions:
                successorGameState = gameState.generateSuccessor(agentIndex, action)
                value = getGhostExp(successorGameState, depth, 1)
                if value > maxVal:
                    maxVal = value
            return maxVal

            
        maxVal = -9999999999
        bestAction = None

        # get actions that are legal for the PACMAN
        nextActions = gameState.getLegalActions(0)
        if 0 == self.depth or len(nextActions) == 0 or gameState.isLose() or gameState.isWin():
            return self.evaluationFunction(gameState)
        
        for action in nextActions:
            # iterate the game state after the PACMAN takes action
            successorGameState = gameState.generateSuccessor(0, action)

            expectGhost = getGhostExp(successorGameState, 0, 1)
            if expectGhost > maxVal:
                maxVal = expectGhost
                bestAction = action
        return bestAction

def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: In A1 I use the distance calculated from the Minimum Spanning Tree Distance for the food heuristic
    Compared to Q1,
    I replace the reciporal of minimum manhattan distance from food to the pacman with
    reciporal the distance of MST
    """
    "*** YOUR CODE HERE ***"
    class UnionFind:
        def __init__(self):
            self.weights = {}
            self.parents = {}
        
        def getRoot(self, obj):
            # find and return the set that contains the obj
            # if the obj is not found, create a set for this obj
            # otherwise, return the root of the obj and then do path compression

            if obj not in self.parents:
                self.parents[obj] = obj
                self.weights[obj] = 1
                return obj
            
            pathToRoot = [obj]
            root = self.parents[obj]
            while root != pathToRoot[-1]:
                # if root == pathToRoot[-1], we find the root itself again
                pathToRoot.append(root)
                root = self.parents[root]
            
            for prevRoot in pathToRoot:
                self.parents[prevRoot] = root
            return root

        def __iter__(self):
            return iter(self.parents)
        
        def union(self, *objs):
            roots = [self.getRoot(x) for x in objs]
            mostWeighted = max([(self.weights[r],r) for r in roots])[1]
            for r in roots:
                if r != mostWeighted:
                    self.weights[mostWeighted] += self.weights[r]
                    self.parents[r] = mostWeighted
    def KruskalMST(G):
        # create a union find set to store all subtrees found
        subtrees = UnionFind()
        mstTreeEdges = []
        mstDistSum = 0
        for W, u, v in sorted((G[u][v],u,v) for u in G for v in G[u]):
            if subtrees.getRoot(u) != subtrees.getRoot(v):
                mstDistSum += W
                mstTreeEdges.append((u,v))
                subtrees.union(u, v)
        return mstDistSum
    
    foodList = currentGameState.getFood().asList().copy()
    foodList.insert(0, currentGameState.getPacmanPosition())
    n = len(foodList)
    graph = {}
    for i in range(n):
        for j in range(n):
            distance = manhattanDistance(foodList[i], foodList[j])
            if i not in graph:
                graph[i] = {j: distance}
            else:
                graph[i].setdefault(j, distance)
            if j not in graph:
                graph[j] = {i: distance}
            else:
                graph[j].setdefault(i, distance)
    
    mstDistance = KruskalMST(graph)
    minFoodDistance = min(manhattanDistance(currentGameState.getPacmanPosition(), food) for food in currentGameState.getFood())
    nearestDistanceToGhost = min(manhattanDistance(currentGameState.getPacmanPosition(), ghost.getPosition()) for ghost in currentGameState.getGhostStates())
    # return currentGameState.getScore() + 3 / float(minFoodDistance+1) - 2 / float(nearestDistanceToGhost+1) + 1/(mstDistance+1)
    # return currentGameState.getScore() - 2 / float(nearestDistanceToGhost+1) + 3/(mstDistance+1)
    # return currentGameState.getScore() - 1 / float(nearestDistanceToGhost+1) + 1 / (mstDistance+1)
    # return currentGameState.getScore() - 1 / float(nearestDistanceToGhost+1) + 3 / (mstDistance+1)
    # return currentGameState.getScore() - 1 / float(nearestDistanceToGhost+1) + 5 / (mstDistance+1)
    # return currentGameState.getScore() + 1 / float(nearestDistanceToGhost+1) + 2.5 / (mstDistance+1)
    return currentGameState.getScore() + 1 / float(nearestDistanceToGhost+1) + 2 / (mstDistance+1)
# Abbreviation
better = betterEvaluationFunction

