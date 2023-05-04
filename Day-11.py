# Problem - "649. Dota2 Senate"

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant_count = sum([1 for c in senate if c == 'R'])
        dire_count = n - radiant_count
        banned = [False] * n

        while radiant_count > 0 and dire_count > 0:
            for i in range(n):
                if banned[i]:
                    continue
                if senate[i] == 'R':
                    j = (i+1) % n
                    while j != i:
                        if not banned[j] and senate[j] == 'D':
                            banned[j] = True
                            dire_count -= 1
                            break
                        j = (j+1) % n
                    if j == i:
                        return "Radiant"
                else:
                    j = (i+1) % n
                    while j != i:
                        if not banned[j] and senate[j] == 'R':
                            banned[j] = True
                            radiant_count -= 1
                            break
                        j = (j+1) % n
                    if j == i:
                        return "Dire"

        return "Radiant" if radiant_count > 0 else "Dire"
