def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_truncatable(number, prime_set):
    str_num = str(number)
    for i in range(1, len(str_num)):
        if not is_prime(int(str_num[i:])) or not is_prime(int(str_num[:i])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    input_range = range(2, numbers[32] + 1)
    result = []
    prime_set = set(input_range)
    for num in sorted(input_range):
        if num in prime_set and is_truncatable(num, prime_set):
            result.append(num)
            for prime in range(2 * 10 ** (len(str(num)) - 1), 10 * num, 10):
                if prime in prime_set:
                    prime_set.remove(prime)
    return result