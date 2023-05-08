# 1964. Find the Longest Valid Obstacle Course at Each Position


class Solution:
  def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
    result = []
    # dp[i] := the length of longest increasing subseq ending at i
    dp = []

    for obstacle in obstacles:
      if not dp or obstacle >= dp[-1]:
        dp.append(obstacle)
        result.append(len(dp))
      else:
        index = bisect_right(dp, obstacle)
        dp[index] = obstacle
        result.append(index + 1)

    return result
