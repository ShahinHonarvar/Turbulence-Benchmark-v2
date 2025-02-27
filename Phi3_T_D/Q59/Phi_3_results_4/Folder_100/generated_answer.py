def is_left_truncatable_prime(n, index):
    prime_numbers = [2, 3, 5, 7]
    str_n = str(n)
    for i in range(index, len(str_n)):
        if int(str_n[i]) % 2 == 0 or int(str_n[i]) % 3 == 0 or int(str_n[i]) % 5 == 0:
            return False
    return all((n // 10 ** i % 10 in prime_numbers for i in range(len(str_n))))

def all_left_truncatable_prime(numbers):
    x = numbers[26]
    return [n for n in range(7, x) if is_left_truncatable_prime(n, 0)]