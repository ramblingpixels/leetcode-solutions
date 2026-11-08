class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        n = len(points)
        points.sort(key=lambda x:x[1])
        
        result = [points[0]]

        for i in range(1, n):
            if points[i][0] <= result[-1][1]:
                temp = result.pop()
                val1 = max(temp[0], points[i][0])
                val2 = min(temp[1], points[i][1])
                result.append([val1,val2])

            else:
                result.append(points[i])


        return len(result)
        
        
            