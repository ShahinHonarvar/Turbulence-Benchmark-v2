def all_left_right_truncatable_prime(numbers):
    x = numbers[767]
    primes = []
    for num in range(2, x + 1):
        if all((int(digit) != 0 and all((int(digit) != 0 for digit in str(num)[:i])) and all((int(digit) != 0 for digit in str(num)[-i:])) for i in range(1, len(str(num))))) and all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            primes.append(num)
    return sorted(primes, reverse=True)