def all_left_truncatable_prime(numbers):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable_prime(prime):
        if '0' in str(prime):
            return False
        temp = str(prime)
        while len(temp) > 0:
            if not is_prime(int(temp)):
                return False
            temp = temp[1:]
        return True
    x = numbers[792]
    result = []
    for prime in (i for i in range(2, x) if is_prime(i)):
        if is_left_truncatable_prime(prime):
            result.append(prime)
    return result