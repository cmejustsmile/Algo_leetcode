class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chk = {}
        max = 0
        p1 = 0
        p2 = 0

        while p2 != len(s) and p1 != len(s):
            if s[p2] in chk :
                if p2 - p1 > max:
                    max = p2 - p1
                for idx in range(p1, chk[s[p2]]):
                    chk.pop(s[idx])
                p1 = chk[s[p2]] + 1
            elif p2 == len(s)-1:
                if p2 - p1 + 1 > max:
                    max = p2 - p1 + 1

            chk[s[p2]] = p2
            p2 += 1


        return max