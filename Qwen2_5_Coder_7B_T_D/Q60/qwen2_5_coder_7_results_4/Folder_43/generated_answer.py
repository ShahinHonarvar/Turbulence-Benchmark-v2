def all_left_right_truncatable_prime(numbers):
    x = numbers[89]
    primes = set()
    for num in range(2, x + 1):
        if all(prime(num)) and '0' not in str(num):
            primes.add(num)
    left_right_truncatable = []
    for num in primes:
        str_num = str(num)
        is_truncatable = True
        for i in range(len(str_num)):
            if not prime(int(str_num[i:])) or not prime(int(str_num[:len(str_num) - i])):
                is_truncatable = False
                break
        if is_truncatable:
            left_right_truncatable.append(num)
    return sorted(left_right_truncatable, reverse=True)

def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True