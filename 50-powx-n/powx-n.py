class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Base case: Any number to the power of 0 is 1
        if n == 0:
            return 1.0
        
        # Handle negative exponents: x^(-n) is equivalent to (1/x)^n
        if n < 0:
            x = 1 / x
            n = -n
            
        # Recursive Binary Exponentiation
        half = self.myPow(x, n // 2)
        
        # If n is even: x^n = (x^(n/2)) * (x^(n/2))
        if n % 2 == 0:
            return half * half
        # If n is odd: x^n = x * (x^(n/2)) * (x^(n/2))
        else:
            return x * half * half
