class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        queue = deque()
        visited = set()
        directions = [[0,-1], [-1, 0], [0, 1], [1, 0]]

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "X" or (r,c) in visited:
                    continue

                visited.add((r,c))
                queue.append((r,c))
                queue_visited = set()
                queue_visited.add((r,c))
                surrounded = True
                while queue:
                    i, j = queue.popleft()                
                    for dr, dc in directions:
                        new_i, new_j = i + dr, j + dc

                        if new_i < 0 or new_i >= rows or new_j < 0 or new_j >= cols:
                            surrounded = False
                            continue
                        if board[new_i][new_j] == "X":
                            continue
                        if (new_i, new_j) in visited:
                            continue

                        visited.add((new_i, new_j))
                        queue.append((new_i, new_j))
                        queue_visited.add((new_i, new_j))

                if surrounded:
                    for i, j in queue_visited:
                        board[i][j] = "X"

        return board
                        


        
                        
        