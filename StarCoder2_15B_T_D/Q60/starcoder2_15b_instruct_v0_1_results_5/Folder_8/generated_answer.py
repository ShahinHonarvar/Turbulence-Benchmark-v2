def all_left_right_truncatable_prime(numbers):

    def is_left_truncatable_prime(number, primes):
        if number < 10:
            return number in primes
        return is_left_truncatable_prime(number % 10 ** len(str(number)) // 10, primes) and number in primes

    def is_right_truncatable_prime(number, primes):
        if number < 10:
            return number in primes
        return is_right_truncatable_prime(number // 10, primes) and number in primes

    def is_one_or_two_digit_prime(number, primes):
        if number < 10:
            return number in primes
        return number in primes
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    left_right_truncatable_primes = []
    for number in numbers:
        if is_one_or_two_digit_prime(number, primes) and is_left_truncatable_prime(number, primes) and is_right_truncatable_prime(number, primes):
            left_right_truncatable_primes.append(number)
    return sorted(left_right_truncatable_primes, reverse=True)