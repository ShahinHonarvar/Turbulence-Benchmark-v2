def all_left_right_truncatable_prime(numbers):
    x = numbers[14]
    primes = [2, 3, 5, 7]
    for num in range(11, x + 1, 2):
        if all((int(digit) not in '024568' for digit in str(num))) and all((int(str(num)[:i]) in primes for i in range(2, len(str(num)) + 1))) and all((int(str(num)[-i:]) in primes for i in range(2, len(str(num)) + 1))):
            primes.append(num)
    primes.sort(reverse=True)
    return primes