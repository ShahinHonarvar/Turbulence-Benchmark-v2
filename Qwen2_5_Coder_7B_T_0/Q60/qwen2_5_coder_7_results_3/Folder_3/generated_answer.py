def all_left_right_truncatable_prime(numbers):
    x = numbers[100]
    primes = [2, 3, 5, 7]
    for num in range(11, x + 1, 2):
        if all((int(digit) != 0 for digit in str(num))) and all((int(str(num)[:i]) in primes for i in range(1, len(str(num))))) and all((int(str(num)[-i:]) in primes for i in range(1, len(str(num))))):
            primes.append(num)
    return sorted(primes)