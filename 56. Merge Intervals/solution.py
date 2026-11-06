class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        n = len(intervals)
        intervals.sort(key = lambda x: x[0])
        result = [intervals[0]]

        for i in range(1, n):
            if intervals[i][0] <= result[-1][1]:
                if intervals[i][1] > result[-1][1]:
                    temp = result.pop()
                    result.append([temp[0], intervals[i][1]])
            else:
                result.append(intervals[i])
        
        
        return result