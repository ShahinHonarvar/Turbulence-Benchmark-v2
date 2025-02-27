def all_left_truncatable_prime(numbers):
    x = numbers[46]

    def is_left_truncatable_prime(num):
        if num < 10:
            return num in [2, 3, 5, 7]
        if '0' in str(num) or not is_prime(num):
            return False
        return all(map(is_left_truncatable_prime, [int(str(num)[i:]) for i in range(1, len(str(num)))]))

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    return sorted(filter(is_left_truncatable_prime, range(2, x)), reverse=True)