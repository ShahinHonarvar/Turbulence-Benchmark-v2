def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n, prime_set):
        temp = n
        while temp > 0:
            if temp not in prime_set:
                return False
            temp = temp // 10
        return True
    prime_set = set()
    for number in numbers:
        if is_prime(number) and len(str(number)) >= 5:
            prime_set.add(number)
            i = number
            while i > 0:
                i = i % 10 ** (len(str(i)) - 1)
                if i not in prime_set:
                    prime_set.discard(number)
                    break
    x = numbers[61]
    result = [i for i in range(2, x) if is_truncatable_prime(i, prime_set)]
    return result