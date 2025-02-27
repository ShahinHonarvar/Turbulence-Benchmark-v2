def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[88]
    left_truncatable_primes = []

    def check_left_truncatable(number, index=0):
        if index == len(str(number)):
            return True
        if not is_prime(int(str(number)[index:])):
            return False
        return check_left_truncatable(number, index + 1)
    for number in range(x - 1, 1, -1):
        if is_prime(number) and check_left_truncatable(number):
            left_truncatable_primes.append(number)
    return left_truncatable_primes