def all_left_truncatable_prime(numbers):
    x = numbers[10]
    is_prime = lambda n: all((n % d != 0 for d in range(2, int(n ** 0.5) + 1))) and n > 1
    left_truncatable = lambda n: all((is_prime(int(str(n)[i:])) for i in range(len(str(n)))))
    return sorted([n for n in range(2, x) if str(n).isdigit() and '0' not in str(n) and left_truncatable(n)], reverse=True)