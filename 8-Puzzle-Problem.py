import heapq
import numpy as np

class EightPuzzle:

    """Initializes a new node in the 8puzzle graph."""


    def __init__(self, state, parent=None, move=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.g = g  # Cost from start node to current node
        self.h = h  # Heuristic cost from current node to goal node
        self.f = g+h # Total cost (g + h)

    def __lt__(self, ot):
        """ Less than comparison for prioritizing nodes in a priority queue.
          Compares the total cost (f) of this node to another node."""

        return (self.g + self.h) < (ot.g + ot.h)

    def __eq__(self, ot):
        """Checks if this node's state is equal to another node's state."""

        return np.array_equal(self.state, ot.state)

    def __hash__(self):
        """Generates a hash value for the node based on its state."""

        return hash(str(self.state))


if __name__ == '__main__':

    def h_manhattan(state, goal_state):
        """Heuristic function: Manhattan distance""" 
        # Initialize the total Manhattan distance to 0
        total_distance = 0  
    
    # Iterate over each box number from 1 to 8
        for num in range(1, 9):
        # Find the current position of the box in the state
            current_pos = np.argwhere(state == num)[0]
        # Find the goal position of the box in the goal_state
            goal_pos = np.argwhere(goal_state == num)[0]
        
        # Calculate the Manhattan distance for this box and add it to the total distance
            total_distance += np.sum(np.abs(current_pos - goal_pos))
    
        return total_distance   


    def h_misplaced(state, goal_state):
        """Heuristic function: Misplaced tiles"""
        # misplaced_count: The number of tiles that are in incorrect positions, excluding the blank space
        misplaced_count = np.sum((state != goal_state) & (state != 0))

        return misplaced_count

    def get_suc(state):
        """Get possible next states from the current state. This function identifies the blank space (represented by 0) and attempts to move it
        in all four possible directions (up, down, left, right) to generate new states."""

        # Initialize an empty list to hold the successor states.
        suc = []

        # Find the position of the blank space (0) in the current state.
        zero_pos = np.argwhere(state == 0)[0]

        # Define possible moves for the blank space: right, left, down, up.
        for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            
            # Calculate the new position of the blank space after the move
            new_pos = zero_pos + move
            if 0 <= new_pos[0] < 3 and 0 <= new_pos[1] < 3:

                #copy current state to create new state
                new_state = state.copy()
                new_state[zero_pos[0], zero_pos[1]], new_state[new_pos[0], new_pos[1]] = \
                    new_state[new_pos[0], new_pos[1]], new_state[zero_pos[0], zero_pos[1]]
                
                #add newly generated state to the list of successor
                suc.append(new_state)

        return suc

    def aStar(initial_state, goal_state, heuristic):
        '''Implements the A* search algorithm to find the shortest path from an initial state to a goal state in a  8puzzle'''

        # Open list as a priority queue to store nodes yet to be explored, prioritized by f value.
        o_list = []
        # Closed set to store hashes of explored states to avoid revisiting them.
        c_set = set()

        # Created a start node with initial state that calculates it's heuristic cost
        start_node = EightPuzzle(initial_state, None, None, 0, heuristic(initial_state, goal_state))

        # Add start node to the open list
        heapq.heappush(o_list, start_node)

        nodes_generated = 0
        nodes_expanded = 0

        while o_list:

            # The node with the lowest f value is poped
            current_node = heapq.heappop(o_list)
            nodes_expanded += 1

            # Checked if the current node is the goal state
            if np.array_equal(current_node.state, goal_state):
                path = []
                while current_node:
                    path.append((current_node.state, current_node.g, current_node.h, current_node.f))
                    current_node = current_node.parent
                return path[::-1], nodes_generated, nodes_expanded

            # Add the current state to the closed set to mark it as explored.
            c_set.add(hash(str(current_node.state)))

            for successor_state in get_suc(current_node.state):
                nodes_generated += 1

                # Create a node for each successor.
                successor_node = EightPuzzle(successor_state, current_node, None, current_node.g + 1, heuristic(successor_state, goal_state))

                # Check if the successor has already been explored.
                if hash(str(successor_node.state)) in c_set:
                    continue

                # If this is a new state, add it to the open list.
                if successor_node not in o_list:
                    heapq.heappush(o_list, successor_node)

        return None, nodes_generated, nodes_expanded

    initial_state_rows = []
    goal_state_rows = []
    # Ask the user to input each row of the array
    print("Enter the initial state (3 rows, each row containing 3 numbers separated by spaces):")
    for i in range(3):
        row = input("Enter row {}: ".format(i + 1))
        # Split the input string into individual numbers and convert them to integers
        numbers = [int(x) for x in row.split()]
        initial_state_rows.append(numbers)
    initial_state = np.array(initial_state_rows)

    print("Enter the goal state (3 rows, each row containing 3 numbers separated by spaces):")
    for i in range(3):
        row = input("Enter row {}: ".format(i + 1))
        # Split the input string into individual numbers and convert them to integers
        numbers = [int(x) for x in row.split()]
        goal_state_rows.append(numbers)
    goal_state = np.array(goal_state_rows)    
    


    while True:

        # The menu options for the users

        print("1. Manhattan Distance")
        print("2. Misplaced Tiles")
        print("3. exit")
        choice = int(input("Enter the heuristic:"))
    
        # Run the A* algorithm using the Manhattan Distance heuristic.
        if choice == 1:
            path, nodes_generated, nodes_expanded = aStar(initial_state, goal_state, h_manhattan)

            # If the solution path is found 
            if path:
                print("Solution path:")
                for state, g, h, f in path:
                    # Print each state in the solution path
                    print(state)
                    # Print the cost metrics for each state.
                    print(f"g:{g}, h:{h}, f:{f}")
                    print('---------------')

                # Print the Nodes generated and Nodes expanded    
                print("Nodes generated:", nodes_generated)
                print("Nodes expanded:", nodes_expanded)
                print(" ")
            else:
                print("No solution found")

        # Run the A* algorithm using the Misplaced Tiles heuristic.        
        elif choice == 2:
            path, nodes_generated, nodes_expanded = aStar(initial_state, goal_state, h_misplaced)

            # If the solution path is found 
            if path:
                print("Solution path:")
                for state, g, h, f in path:

                    # Print each state in the solution path
                    print(state)
                    # Print the cost metrics for each state.
                    print(f"g:{g}, h:{h}, f:{f}")
                    print('---------------')

                # Print the Nodes generated and Nodes expanded     
                print("Nodes generated:", nodes_generated)
                print("Nodes expanded:", nodes_expanded)
                print("")
            else:
                print("No solution found")

        # To exit the Menu        
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please enter a valid option.")