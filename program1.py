class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
       if not grid:
          return 0

       def  dfs(i,j):
            if i<0 or i >= len(grid) or j<0 or j>=len(grid[0]) or grid[i][j] !='L':
               return 
               grid[i][j] = 'W' 
               dfs(i+1, j )
               dfs(i-1, j)
               dfs(i , j+1)
               dfs(i, j-1)

       count = 0
       for i in range(len(grid)):
          for j in range (len([0])):
              if grid[i][j] == 'L':
                 count+=1
                 dfs(i,j)
                 
        return count
