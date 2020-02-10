#****************************************************************************************
#    Name:      Angad Pal Singh                                                         *                                                                 *                    
#                                                                                       *
#    Program:   8-Puzzle Solver                                                         *
#                                                                                       *
#**************************************************************************************** 
import copy
import sys
import heapq
from queue import PriorityQueue

goalState = [[1,2,3],[4,5,6],[7,8,0]]

class Puzzle():
    def __init__(self, state):
        self.state = state

    #find postion of the blank tile in the puzzle    
    def find_zero_tile(self, state):
        for i in range(0, 3):
            for j in range(0, 3):
                if state[i][j] == 0:
                    x = j
                    y = i
        return (x,y)

    #hashing state to the uid
    def hash_uid(self, state):
        uid = 0
        mult = 1
        for i in range(0,3):
            for j in range(0,3):
                uid += state[i][j] * mult
                mult *= 9
        return uid
    
    #moves the zero tile to possible neighboring tiles
    def neighbors(self, state):
        #Returns the new states, tiles resulting from the move
        neighbors = []
        idx = self.find_zero_tile(state)
        row = idx[0]
        col = idx[1]
        
        if row > 0:
            #move right
            r = copy.deepcopy(state)
            r[col][row] = r[col][row-1]
            r[col][row-1] = 0
            neighbors.append((r,str(r[col][row])))
        if row < 2:
            #move left
            l = copy.deepcopy(state)
            l[col][row] = l[col][row+1]
            l[col][row+1] = 0
            neighbors.append((l,str(l[col][row])))
        if col > 0:
            #move down
            d = copy.deepcopy(state)
            d[col][row] = d[col-1][row]
            d[col-1][row] = 0
            neighbors.append((d,str(d[col][row])))
        if col < 2:
            #move right
            u = copy.deepcopy(state)
            u[col][row] = u[col+1][row]
            u[col+1][row] = 0
            neighbors.append((u,str(u[col][row])))
        return neighbors

    #calculates the manhattan distance heuristic
    def manhattanDist(self, state):
        distSum = 0
        size  = len(state)
        for i in range(size):
            for j in range(size):
                x, y = divmod(state[i][j], size)
                distSum += abs(x-i) + abs(y-j)
        return distSum

    #implementation of the A* algorithm for best first path
    def astar_search(self, state):
        start_uid = self.hash_uid(state) 
        goal_uid = self.hash_uid(goalState)
        visited_states = set()   #set of visited states
        frontier = PriorityQueue()   #priority queue to return the lowest value first
        start_path = ""
        initial_cost = 0
        h_cost = self.manhattanDist(state)
        f_cost = initial_cost + h_cost
        startNode = (f_cost, initial_cost, start_path, start_uid, state)
        
        frontier.put(startNode)
    
        while not frontier.empty():
            #frontier expands into the unexplored nodes until a goal node is encountered
            current = frontier.get()
            current_cost, current_path, current_uid, current_state = current[1:]
            if current_uid == goal_uid:
                return ("Move tiles: " + current_path)
            if current_uid in visited_states:
                continue
            visited_states.add(current_uid)
            
            #exploring the neighboring states
            #expand it by looking at its neighbors. Any neighbors we haven’t visited yet we add to the frontier
            for (next_state, next_nbr) in self.neighbors(current_state):
                new_cost = current_cost + 1
                f_cost = new_cost + self.manhattanDist(next_state)
                new_path = current_path + next_nbr + "  "
                next_uid = self.hash_uid(next_state)
                nextNode = (f_cost, new_cost, new_path, next_uid, next_state)
                frontier.put(nextNode)
        return "No Path"

    #checks if the puzzle is solvable using parity
    def checkSolvable(self, state):
        inversions = 0;
        #flatten the 2-d list into a 1-d list
        flatten = [j for sub in state for j in sub] 
        for i in range(8):
            for j in range(i+1, 9):
                if flatten[j] and flatten[i] and flatten[i] > flatten[j]:
                    inversions += 1
        return(inversions % 2 == 0)

    #prints out the current state
    def print_state(self, state):
        print("\nCurrent State")
        for row in (state):
            print("{}  {}  {} ".format(*row))

def main():           
    file = open("program_1_data.txt", "r")
    #parsing the input file
    result =[]
    sub =[]
    for line in file.readlines():
        if line.strip():
            sub.append([int(x) for x in line.split()])
        else:
            result.append(sub)
            sub=[]
          
    #print possible path using astar search        
    for board in result:
       puzzle = Puzzle(board)
       orig_stdout = sys.stdout
       puzzle.print_state(board)
       if(puzzle.checkSolvable(board)):
           print("\nSolvable")
           print(puzzle.astar_search(board))
           print("-" * 60)
       else:
           print("\nNot solvable")
           print("-" * 60)
           
if __name__ == '__main__':
    main()
