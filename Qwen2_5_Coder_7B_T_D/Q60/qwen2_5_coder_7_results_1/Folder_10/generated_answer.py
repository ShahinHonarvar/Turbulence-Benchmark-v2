def all_left_right_truncatable_prime(numbers):
    x = numbers[38]
    primes = [2, 3, 5, 7]
    left_right_truncatable_primes = []
    for num in range(11, x + 1):
        if all((int(digit) != 0 for digit in str(num))) and all((int(str(num)[0:i]) in primes for i in range(1, len(str(num))))) and all((int(str(num)[-i:]) in primes for i in range(1, len(str(num))))):
            left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes, reverse=True)