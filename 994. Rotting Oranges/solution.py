class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        grid_copy = deepcopy(grid)
        fresh_count = 0
        directions = [[0,-1], [-1, 0], [0, 1], [1, 0]]

        for i in range(rows):
            for j in range(cols):
                if grid_copy[i][j] == 2:
                    queue.append((i,j))
                elif grid_copy[i][j] == 1:
                    fresh_count += 1

        minutes = 0
        while len(queue) != 0 and fresh_count > 0:
            minutes += 1
            total_rotten = len(queue)

            for _ in range(total_rotten):
                i, j = queue.popleft()
                for dr, dc in directions:
                    new_i, new_j = i + dr, j + dc
                    if new_i < 0 or new_i >= rows or new_j < 0 or new_j >= cols:
                        continue
                    if grid[new_i][new_j] == 2 or grid[new_i][new_j] == 0:
                        continue
                    fresh_count -= 1
                    grid[new_i][new_j] = 2
                    queue.append((new_i, new_j))
        
        if fresh_count > 0:
            return -1
        return minutes

            



        