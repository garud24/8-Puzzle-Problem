# 8-Puzzle-Problem
Problem Statement: 8-Puzzle Problem
Implement A* search algorithm for solving the 8-Puzzle problem.
8-puzzle Problem Formulation
The problem: The 8-puzzle problem is a puzzle invented by Noyes Palmer Chapman. It is played on a 3-by-3 grid with 8 square blocks labeled 1 through 8 and a blank square. The goal is to rearrange the blocks so that they are in order. We are permitted to slide blocks horizontally or vertically into the blank square. The following shows a sequence of legal moves from an initial board position to the goal position.
A* Algorithm
The A* Algorithm is a flexible pathfinding and search technique aimed at identifying the most efficient path from an initial state to a target state, taking into account the cost associated with each path. It employs a heuristic function to choose an allowable heuristic value, which is then used to ascertain the next most favorable successor state for exploration.
Heuristic Evaluation Function: f(n) = g(n) + h(n),
where:
- f(n) represents the projected total cost of the path leading to the goal state. - g(n) denotes the cost incurred to reach the current state.
- h(n) is the estimated cost from the current state to the goal state.
Heuristic Functions
In solving the 8-Puzzle problem with the A* Algorithm, two popular heuristic functions are utilized to guide the search, represented as h(n) in the A* evaluation function. These functions are:
Manhattan Distance: This heuristic computes the total distance that each tile is from its target location, but only accounts for moves along vertical and horizontal paths.
Misplaced Tiles: This heuristic tallies up the tiles that are not situated in their designated goal positions.
Program Structure
Classes:
Class EightPuzzle – Initializes a new node in the 8-puzzle graph
Functions:
● __lt__: Less than comparison for prioritizing nodes in a priority queue. Compares the total cost (f) of this node to another node.
● __eq__: Checks if this node's state is equal to another node's state.
● __hash__: Generates a hash value for the node based on its state.
● h_manhattan: Heuristic function: Manhattan distance
● h_misplaced: Heuristic function: Misplaced tiles
● get_suc: Get possible next states from the current state. This function identifies the blank space (represented by 0) and attempts to move it in all four possible directions (up, down, left, right) to generate new states.
● aStar: Implements the A* search algorithm to find the shortest path from an initial state to a goal state in a 8-puzzle

Sample Input and Output

Using Manhattan Distance Heuristic
Enter the initial state (3 rows, each row containing 3 numbers separated by spaces): Enter row 1: 0 1 3
Enter row 2: 4 2 5
Enter row 3: 7 8 6
Enter the goal state (3 rows, each row containing 3 numbers separated by spaces): Enter row 1: 1 2 3
Enter row 2: 4 5 6
Enter row 3: 7 8 0
1. Manhattan Distance
2. Misplaced Tiles
3. exit
Enter the heuristic:1
Solution path:
[[0 1 3]
[4 2 5]
[7 8 6]] g:0, h:4, f:4 --------------- [[1 0 3]
[4 2 5]
[7 8 6]] g:1, h:3, f:4 --------------- [[1 2 3]
[4 0 5]
[7 8 6]] g:2, h:2, f:4 --------------- [[1 2 3]
[4 5 0]
[7 8 6]] g:3, h:1, f:4 --------------- [[1 2 3]
[4 5 6]
[7 8 0]]
g:4, h:0, f:4
---------------
Nodes generated: 12
Nodes expanded: 5
Using Misplaced Tile Heuristic 1. Manhattan Distance
2. Misplaced Tiles
3. exit
Enter the heuristic:2
Solution path:
[[0 1 3]
[4 2 5]
[7 8 6]] g:0, h:4, f:4 --------------- [[1 0 3]
[4 2 5]

[7 8 6]] g:1, h:3, f:4 --------------- [[1 2 3]
[4 0 5]
[7 8 6]] g:2, h:2, f:4 --------------- [[1 2 3]
[4 5 0]
[7 8 6]] g:3, h:1, f:4 --------------- [[1 2 3]
[4 5 6]
[7 8 0]]
g:4, h:0, f:4 ---------------
Nodes generated: 12 Nodes expanded: 5


Observations:
• It is evident by comparing the Manhattan Distance Heuristic (MDH) and the Misplaced Tile Heuristic (MTH) in the aforementioned scenarios that MDH, in most cases, produces and extends fewer nodes than MTH. This demonstrates that, generally speaking, MDH is a more sensible and effective heuristic for directing the A* search process.
• MDH and MTH are acceptable heuristics because, depending on when a solution is possible, they both result in optimal solutions at the same cost.
• The "NO SOLUTION" outcomes denote situations in which neither MDH nor MTH are able to find a solution. The Manhattan Distance Heuristic is generally the best option for an 8-Puzzle issue, as it can significantly impact the A* algorithm's performance and efficiency.
