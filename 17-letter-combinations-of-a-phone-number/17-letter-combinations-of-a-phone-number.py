def combination(t, d, idx, str, ans):
    if len(d) == 0:
        return
    
    if idx == len(d):
        ans.append(str)
        return

    for c in t[int(d[idx])]:
        combination(t, d, idx+1, str+c, ans)
            
class Solution:    
        
    def letterCombinations(self, digits: str) -> List[str]:
        t = [(),(),('a','b','c'),('d','e','f'),('g','h','i'),('j','k','l'),('m','n','o'),('p','q','r','s'),('t','u','v'),('w','x','y','z')]
        digits_n = ""
        for c in digits:
            if int(c) == 0 or int(c) == 1:
                continue
            digits_n = digits_n+c

        ans = []

        combination(t, digits_n, 0, "", ans)

        return ans