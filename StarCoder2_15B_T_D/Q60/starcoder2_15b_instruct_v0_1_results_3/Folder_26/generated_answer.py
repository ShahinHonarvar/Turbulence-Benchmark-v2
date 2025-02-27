def all_left_right_truncatable_prime(numbers):

    def is_truncatable_prime(number):
        if number in [2, 3, 5, 7]:
            return True
        if number < 10:
            return False
        if number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or (number % 7 == 0):
            return False
        while number >= 10:
            number = int(str(number)[1:])
            if number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or (number % 7 == 0):
                return False
        return True
    truncatable_primes = []
    for number in numbers:
        if is_truncatable_prime(number):
            truncatable_primes.append(number)
    return sorted(truncatable_primes, reverse=True)