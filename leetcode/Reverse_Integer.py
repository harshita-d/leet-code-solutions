class Solution:
    def reverse(self, x: int) -> int:
        f=0
        num=x
        sum1=0
        if num>=2147483647 or num <= -2147483648:
            return 0
        
        if (num < 0):
            f=1
            num *= -1
	        
        while(num!=0):
            r=num%10
            num= num//10
            sum1=(sum1*10)+r
        
        if f==1:
            sum1*=-1
        
        if sum1>=2147483647 or sum1 <= -2147483648:
            return 0
    
        return sum1