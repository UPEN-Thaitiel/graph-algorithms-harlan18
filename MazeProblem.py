""" CESAR ALONSO LOPEZ ANGUIANO ISOFT8 
Insert your code bellow 

our task is to implement an algorithm that can find the way out of a maze.

The maze representation is like this:

    [
      [1,1,1,1,1],
      [1,0,0,1,1],
      [1,1,0,1,1],
      [1,1,0,0,0],
      [1,1,1,1,1],
    ]

So we have a map like this

    integer 0 represents walls

    integer 1 represents valid cells

    cell (0,0) is the starting point (it is the top left corner)

    the bottom right cell is the destination (so this is what we are looking for)

So the solution should be something like this (S represents the states in the solution set):

    [
      [S,-,-,-,-],
      [S,-,-,-,-],
      [S,-,-,-,-],
      [S,-,-,-,-],
      [S,S,S,S,S],
    ]

Good luck!


"""
def solve_maze(maze):
    rows = len(maze)
    cols = len(maze[0])
    
    solution = [['-' for _ in range(cols)] for _ in range(rows)]
    
    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols and maze[r][c] == 1
    
    def dfs(r, c):
        if r == rows - 1 and c == cols - 1:
            solution[r][c] = 'S'
            return True
        
        if is_valid(r, c) and solution[r][c] == '-':
            solution[r][c] = 'S'
            
            if dfs(r + 1, c):
                return True
            if dfs(r, c + 1):
                return True
            if dfs(r - 1, c):
                return True
            if dfs(r, c - 1):
                return True
            
            solution[r][c] = '-'
        
        return False
    
    print("Maze solution:")
    if dfs(0, 0):
        for row in solution:
            print(row)
    else:
        print("No solution found.")
    print()

if __name__ == '__main__':
    ### Your code must succesfully solve the following mazes:
    
    m = [[1, 0, 0, 1],
         [1, 0, 0, 1],
         [1, 0, 0, 1],
         [1, 1, 1, 1]
         ]

    easy_maze = [
        [1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 0, 0, 1],
        [0, 1, 1, 1, 1]
    ]

    medium_maze = [
        [1, 1, 0, 1, 1, 0],
        [0, 1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1],
        [0, 0, 1, 0, 0, 1]
    ]   
    hard_maze = [
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 1, 1, 0, 1, 1, 1],
        [0, 0, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1]
    ]


solve_maze(m)
solve_maze(easy_maze)
solve_maze(medium_maze)
solve_maze(hard_maze)

