class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []
        tot = 0
        for c in operations:
            if c == "+":
                tot += ans[-1]+ans[-2]
                ans.append(ans[-1]+ans[-2])
            elif c == "D":
                tot += ans[-1]*2
                ans.append(ans[-1]*2)
            elif c == "C":
                tot -= ans.pop()
            else:
                tot += int(c)
                ans.append(int(c))

        return tot

        