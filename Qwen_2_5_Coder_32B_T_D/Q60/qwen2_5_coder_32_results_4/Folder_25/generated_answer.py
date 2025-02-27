def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[92]
    if x < 11:
        return []
    truncatable_primes = []
    for num in range(11, x + 1):
        s = str(num)
        if '0' in s:
            continue
        left_right_prime = True
        while len(s) > 1:
            if not is_prime(int(s)) or not is_prime(int(s[::-1])):
                left_right_prime = False
                break
            s = s[1:-1]
        if left_right_prime and is_prime(int(s)):
            truncatable_primes.append(num)
    return truncatable_primes