def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[22]
    result = []
    for num in range(11, x + 1):
        s = str(num)
        if '0' not in s:
            all_primes = True
            for i in range(len(s)):
                if not is_prime(int(s[i:])) or not is_prime(int(s[:len(s) - i])):
                    all_primes = False
                    break
            if all_primes:
                result.append(num)
    return sorted(result, reverse=True)