

class Solution:

    #Function to find the number of 'X' total shapes.
    def xShape(self, grid):
    #Code here
    def dfs(arr , i , j , visit , r , c):
        if i < 0 or i > r-1:
            return
        if j < 0 or j > c-1:
            return
        if arr[i][j] == 'O' or visit[i][j]:
            return

        visit[i][j] = True
        dfs(arr , i+1 , j , visit , r , c)
        dfs(arr , i-1 , j , visit , r , c)
        dfs(arr , i , j+1 , visit , r , c)
        dfs(arr , i , j-1 , visit , r , c)
    r = len(grid)
    c = len(grid[0])
    count = 0
    visit = [[False for j in range(c)] for i in range(r) ]
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 'X' and not visit[i][j]:
                dfs(grid , i , j , visit , r , c)
                count += 1
    return count