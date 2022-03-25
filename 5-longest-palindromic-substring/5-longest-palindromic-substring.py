class Solution:
    def longestPalindrome(self, s: str) -> str:
        max = ""
        for i, c in enumerate(s):
            cnt = 0
            while i-cnt >= 0 and i+cnt < len(s) and s[i-cnt]==s[i+cnt]:
                cnt+=1
            cnt -= 1
            if 2 * cnt + 1 > len(max):
                max = s[i-cnt:i+cnt+1]

            cnt = 0
            while i-cnt+1 >= 0 and i-cnt+1 <len(s) and i+cnt < len(s) and s[i-cnt+1]==s[i+cnt]:
                cnt+=1
            cnt-=1
            if 2 * cnt > len(max):
                if cnt == 0:
                    max = s[i:i+2]
                max = s[i-cnt+1:i+cnt+1]

        return max
