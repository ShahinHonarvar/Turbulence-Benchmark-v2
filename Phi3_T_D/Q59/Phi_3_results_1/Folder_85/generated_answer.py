def all_left_truncatable_prime(numbers):
    is_prime = lambda n: n > 1 and all((n % d for d in range(2, int(n ** 0.5) + 1)))

    def left_truncatable(n, primelist):
        if is_prime(n):
            for i in range(1, len(str(n))):
                if not is_prime(int(str(n)[i:])):
                    return False
            primelist.append(n)
        return True
    x = numbers[94]
    primelist = []
    for i in range(2, x):
        left_truncatable(i, primelist)
    return primelist