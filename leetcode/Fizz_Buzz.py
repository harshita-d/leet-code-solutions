class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return ["FizzBuzz" if i%15==0 else "Buzz" if i%5==0 else "Fizz" if i%3==0 else str(i) for i in range(1,n+1)]
        
    """
    for i in range(1,n+1):
        if i%15==0:
            l.append("Fizzbuzz")
        elif i%3==0:
            l.append("Fizz")
        elif i%5==0:
            print("Buzz")
        else:
            l.append(str(i))
    """