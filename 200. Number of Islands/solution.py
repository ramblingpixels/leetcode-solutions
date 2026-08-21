class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows  = len(grid)
        cols = len(grid[0])
        queue = deque()
        directions = [[0,-1], [-1,0], [0,1], [1,0]]
        visited = set()
        island_count = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "0" or (r,c) in visited:
                    continue
                
                island_count += 1
                queue.append((r,c))
                visited.add((r,c))

                while len(queue) > 0:
                    i, j = queue.popleft()

                    for dr, dc in directions:
                        new_i, new_j = i + dr, j + dc

                        if new_i < 0 or new_i >= rows or new_j < 0 or new_j >= cols:
                            continue
                        if grid[new_i][new_j] == "0":
                            continue
                        if (new_i, new_j) in visited:
                            continue

                        visited.add((new_i, new_j))
                        queue.append(((new_i, new_j)))
        
        return island_count
