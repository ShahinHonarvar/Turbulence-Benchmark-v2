def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[28]
    truncatable_primes = []
    for num in range(23, x + 1):
        if '0' in str(num):
            continue
        left = num
        right = num
        valid = True
        while left > 0 and right > 0:
            if not is_prime(left) or not is_prime(right):
                valid = False
                break
            left = int(str(left)[1:])
            right = int(str(right)[:-1])
        if valid and (left == 2 or left == 3 or left == 5 or (left == 7)) and (right == 2 or right == 3 or right == 5 or (right == 7)):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)