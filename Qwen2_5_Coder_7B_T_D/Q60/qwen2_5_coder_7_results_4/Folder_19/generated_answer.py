from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[67]
    primes = [2, 3, 5, 7]
    for i in range(10, x + 1):
        if all((isprime(int(str(i)[:j])) for j in range(1, len(str(i))))) and all((isprime(int(str(i)[j:])) for j in range(0, len(str(i)) - 1))) and ('0' not in str(i)):
            primes.append(i)
    return sorted(primes, reverse=True)