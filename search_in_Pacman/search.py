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

def depthFirstSearch(problem: SearchProblem):
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
    fringe = util.Stack()                                 # use stack for DFS
    visited = set()                                       # keep track of visited nodes
    actions = []                                          # list of actions
    start_state = problem.getStartState()
    fringe.push((start_state, actions))                   # push starting state and actions to fringe

    while not fringe.isEmpty():
        current_state, current_path = fringe.pop()        # parent node
        if current_state not in visited:                  # pass through if already visited
            visited.add(current_state)
            if problem.isGoalState(current_state):
                return current_path
            else:
                children = problem.getSuccessors(current_state)
                for next_state, action, _ in children:
                    next_path = current_path + [action]   # update actions for child node
                    fringe.push((next_state, next_path))  # push child node onto fringe
    util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    fringe = util.Queue()                                 # use queue for BFS
    visited = set()                                       # keep track of visited nodes
    actions = []                                          # list of actions
    start_state = problem.getStartState()
    fringe.push((start_state, actions))                   # push starting state and actions to fringe

    while not fringe.isEmpty():
        current_state, current_path = fringe.pop()        # parent node
        if current_state not in visited:                  # pass through if already visited
            visited.add(current_state)
            if problem.isGoalState(current_state):
                return current_path
            else:
                children = problem.getSuccessors(current_state)
                for next_state, action, _ in children:
                    next_path = current_path + [action]   # update actions for child node
                    fringe.push((next_state, next_path))  # push child node onto fringe
    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    fringe = util.PriorityQueue()                                               # use priority queue for UCS
    visited = set()                                                             # keep track of visited nodes
    actions = []                                                                # list of actions
    start_state = problem.getStartState()
    cost = 0                                                                    # initial cost
    fringe.push((start_state, actions, cost), cost)
    while not fringe.isEmpty():
        current_state, current_path, current_cost = fringe.pop()                # parent node
        if current_state not in visited:                                        # pass through if already visited
            visited.add(current_state)
            if problem.isGoalState(current_state):
                return current_path
            else:
                children = problem.getSuccessors(current_state)
                for next_state, action, cost in children:
                    next_path = current_path + [action]                         # update actions for child node
                    next_cost = current_cost + cost                             # update cost for child node
                    fringe.push((next_state, next_path, next_cost), next_cost)  # push child node onto fringe
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    fringe = util.PriorityQueue()                                                                     # use priority queue for A* search
    visited = set()                                                                                   # keep track of visited nodes 
    actions = []                                                                                      # list of actions
    start_state = problem.getStartState()
    cost = 0                                                                                          # initial cost
    heuristic_cost = heuristic(start_state, problem)                                                  # initial heuristic cost
    fringe.push((start_state, actions, cost), cost + heuristic_cost)

    while not fringe.isEmpty():
        current_state, current_path, current_cost = fringe.pop()                                      # parent node
        if current_state not in visited:                                                              # pass through if already visited
            visited.add(current_state)
            if problem.isGoalState(current_state):
                return current_path
            else:
                children = problem.getSuccessors(current_state)
                for next_state, action, cost in children:
                    next_path = current_path + [action]                                               # update actions for child node
                    next_cost = current_cost + cost                                                   # update cost for child node
                    next_heuristic_cost = heuristic(next_state, problem)                              # update heuristic cost for child node
                    fringe.push((next_state, next_path, next_cost), next_cost + next_heuristic_cost)  # push child node onto fringe

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
