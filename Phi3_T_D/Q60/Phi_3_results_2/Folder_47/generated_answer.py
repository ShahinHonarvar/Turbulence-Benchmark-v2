def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[49]
    truncatable_primes = []

    def is_circular_prime(num):
        rotations = {num}
        rotation = num
        while True:
            rotation = int(str(rotation)[1:] + str(rotation)[0])
            if rotation in rotations:
                return all((is_prime(rotation % 10 ** i) for i in range(2, len(str(rotation)) + 1)))
            rotations.add(rotation)
    for num in range(11, x + 1, 2):
        if is_prime(num) and is_circular_prime(num):
            truncatable_primes.append(num)
    return truncatable_primes