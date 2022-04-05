def combination(N,lcnt,rcnt,s,answer):
    if lcnt == N and rcnt ==N:
        answer.append(s)
        return

    
    if lcnt != N:
        combination(N,lcnt+1,rcnt,s+'(', answer)
        
    if lcnt>=rcnt+1:
        combination(N,lcnt,rcnt+1,s+')', answer)    
        

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        lcnt, rcnt = 0, 0
        answer=[]
        
        combination(n,lcnt,rcnt,"", answer)
        
        return answer
        