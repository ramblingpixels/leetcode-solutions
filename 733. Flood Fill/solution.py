class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        queue = deque()
        queue.append((sr,sc))
        directions = [[0, -1], [-1, 0], [0, 1], [1, 0]]
        grid_copy = deepcopy(image)
        rows = len(image)
        cols = len(image[0])
        grid_copy[sr][sc] = color
        starting_color = image[sr][sc]

        while len(queue) != 0:
            n = len(queue)

            for _ in range(n):
                i, j = queue.popleft()
                for dr, dc in directions:
                    new_i, new_j = i + dr, j + dc

                    if new_i < 0 or new_i >= rows or new_j < 0 or new_j >= cols:
                        continue
                    if grid_copy[new_i][new_j] == color or grid_copy[new_i][new_j] != starting_color:
                        continue
                    grid_copy[new_i][new_j] = color
                    queue.append((new_i, new_j))

        return grid_copy


