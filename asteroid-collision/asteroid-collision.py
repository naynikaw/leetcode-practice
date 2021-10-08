class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        
        for a in asteroids:
            #top = ans[-1]
            if a>0:
                ans.append(a)
                
            else:
                while ans and ans[-1]>0 and ans[-1]<abs(a):
                    ans.pop()
                
                if not ans or ans[-1]<0:
                    ans.append(a)
                    
                elif ans[-1] == -a:
                    ans.pop()
        return ans