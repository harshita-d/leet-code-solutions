class Solution:
    def isValid(self, s: str) -> bool:
        while len(s) > 0:
            l = len(s)
            print("l",l)
            print("before",s)
            s = s.replace('()','').replace('{}','').replace('[]','')
            print("after",s)
            if l==len(s): return False
        return True
        