class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        half = len(s)//2
        a = s[:half]
        b = s[half:]
        
        count_a = a.count('a') + a.count('e') + a.count('i') + a.count('o') + a.count('u') + a.count('A') + a.count('E') + a.count('I') + a.count('O') + a.count('U')
        
        count_b = b.count('a') + b.count('e') + b.count('i') + b.count('o') + b.count('u') + b.count('A') + b.count('E') + b.count('I') + b.count('O') + b.count('U')
        
        if count_a==count_b:
            return True
        return False
