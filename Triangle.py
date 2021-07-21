'''Description: Greatest Path Sum in Triangle.
Find the greatest path sum starting at the top of the triangle and moving
only to ADJACENT numbers on the row below applying four different approaches:
exhaustive search, greedy, divide and conquer, and dynamic programming.
   3
  7 4
 2 4 6
8 5 9 3
max path sum = 3 + 7 + 4+ 9 = 23

Student's Name: Sayuri Monarrez Yesaki
Student's UT EID: sdm3465
Course Name: CS 313E Elements of Software design
Unique Number: 51335
Date Created: 03/7/2018
Date Last Modified: 03/9/2018
'''import time

def next_path(my_grid):
   my_grid[-1] += 1
   for i in range(len(my_grid) - 1, 0, -1):
      if abs(my_grid[i] - my_grid[i - 1]) > 1:
         my_grid[i - 1] += 1

         for j in range(i,len(my_grid)):
            val = my_grid[j - 1]
            my_grid[j] = val
   return my_grid

def div_conquer(grid, row, idx_row):
   # Base case: row is the last row of the grid.
   if row == (len(grid) - 1):
      return grid[row][idx_row]
   # Recursive case:
   else:
      return grid[row][idx_row] + max(div_conquer( grid, row + 1, idx_row), div_conquer( grid, row + 1, idx_row + 1) )

def dynamic_sum_grids(row_original, row_dyn_grid):
   sum_columns = 0
   new_row = []
   for i in range(len(row_original)):
      if row_dyn_grid[i] >= row_dyn_grid[i + 1]:
         val = row_original[i] + row_dyn_grid[i]
      elif row_dyn_grid[i] < row_dyn_grid[i + 1]:
         val = row_original[i] + row_dyn_grid[i + 1]
      new_row.append(val)
   return new_row

def ordering_dyn_grid(new_row, dynamic_grid):
   ordered_grid = []
   ordered_grid.append(new_row)
   for rows in dynamic_grid:
      ordered_grid.append(rows)
   return ordered_grid

# returns the greatest path sum using exhaustive search
def exhaustive_search(grid):
   exhaustive_sum = 0
   path_sum = 0
   path = [0] * len(grid)
   while path[0] == 0:
      path_sum = 0
      for j in range(len(path)):
         path_sum += grid[j][path[j]]
      if path_sum > exhaustive_sum:
         exhaustive_sum = path_sum
      path = next_path(path)
   return exhaustive_sum

# returns the greatest path sum using greedy approach
def greedy (grid):
   greedy_sum = 0
   j = 0
   for i in range(len(grid)):
      if len(grid[i]) == 1:
         greedy_sum = greedy_sum + grid[i][j]
      else:
         if grid[i][j] >= grid[i][j+1]:
            greedy_sum = greedy_sum + grid[i][j]
         elif grid[i][j] < grid[i][j + 1]:
            greedy_sum = greedy_sum + grid[i][j + 1]
            j = j + 1
   return greedy_sum

# returns the greatest path sum using divide and conquer (recursive) approach
def rec_search (grid):
   recursive_sum = div_conquer(grid, 0, 0)
   return recursive_sum

# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog (grid):
   dynamic_grid = []
   dynamic_grid.append(grid[len(grid) - 1])
   for i in range(len(grid) - 2, -1, -1): # mueve los renglones del grid original
      new_row = dynamic_sum_grids(grid[i], dynamic_grid[0])
      dynamic_grid = ordering_dyn_grid(new_row, dynamic_grid)
   # return dynamic_sum, dynamic_grid
   dynamic_sum = dynamic_grid[0][0]
   return  dynamic_sum, dynamic_grid

# reads the file and returns a 2-D list that represents the triangle
def read_file():
   #open file
   inFile = open("triangle.txt", "r")
   # read number of rows in triangle
   n = int(inFile.readline().strip())
   # read rows of data and make grid
   grid = []
   for i in range(n):
      row = inFile.readline().strip().split()
      for i in range(len(row)):
         row[i] = int(row[i])
      grid.append(row)
   return grid

def main ():
   # read triangular grid from file
   grid = read_file()

   exhaustive_sum = exhaustive_search(grid)
   ti = time.time()
   # output greates path from exhaustive search
   print("The greatest path sum through exhaustive search is ", exhaustive_sum )
   tf = time.time()
   del_t = tf - ti
   # print time taken using exhaustive search
   print("The time taken for exhaustive search is ", del_t, "seconds.")
   print()

   ti = time.time()
   # output greates path from greedy approach
   greedy_sum = greedy(grid)
   print("The greatest path sum through greedy search is ", greedy_sum)
   tf = time.time()
   del_t = tf - ti
   # print time taken using greedy approach
   print("The time taken for greedy approach is ", del_t, " seconds.")
   print()

   ti = time.time()
   # output greates path from divide-and-conquer approach
   recursive_sum = rec_search(grid)
   print("The greatest path sum through recursion search is ", recursive_sum)
   tf = time.time()
   del_t = tf - ti
   # print time taken using divide-and-conquer approach
   print("The time taken for recursive approach is ", del_t, " seconds.")
   print()

   ti = time.time()
   # output greates path from dynamic programming
   dynamic_sum, dynamic_grid = dynamic_prog(grid)
   print("The greatest path sum through dynamic programming is ", dynamic_sum)
   tf = time.time()
   del_t = tf - ti
   # print time taken using dynamic programming
   print("The time taken for dynamic programming is ", del_t, " seconds.")

if __name__ == "__main__":
  main()
