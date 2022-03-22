class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            chk = {}
            max = 0

            for i in range(0, len(s)):
                chk.clear()
                if len(s) - i <= max :
                    break

                for j in range(i, len(s)):
                    if s[j] in chk :
                        if j - i > max:
                            max = j - i
                        break
                    elif j == len(s) - 1 :
                        if j - i + 1 > max :
                            max = j - i + 1
                    else:
                        chk[s[j]] = 0

            return max