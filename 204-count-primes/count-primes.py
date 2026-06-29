class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        # Create a boolean array, initialize all as True (meaning prime)
        is_prime = [True] * n
        is_prime[0] = False
        is_prime[1] = False
        
        # Sieve of Eratosthenes
        p = 2
        while p * p < n:
            if is_prime[p]:
                # Mark all multiples of p as False starting from p*p
                for i in range(p * p, n, p):
                    is_prime[i] = False
            p += 1
            
        # The number of True values is the count of prime numbers
        return sum(is_prime)
