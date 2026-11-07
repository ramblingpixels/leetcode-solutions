class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        n = len(intervals)
        
        intervals.sort(key = lambda x:( x[1]))
        result = [intervals[0]]

        for i in range(1, n):
            if intervals[i][0] >= result[-1][1]:
                result.append(intervals[i])
        
        
        return len(intervals) - len(result)