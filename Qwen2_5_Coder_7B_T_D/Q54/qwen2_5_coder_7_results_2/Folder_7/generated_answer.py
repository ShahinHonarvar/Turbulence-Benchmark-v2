def all_right_truncatable_prime(numbers):
    x = numbers[803]
    primes = [2, 3, 5, 7]
    right_truncatable_primes = [2, 3, 5, 7]
    for num in range(8, x):
        if all((int(num) % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            primes.append(num)
            for prime in right_truncatable_primes[:]:
                new_num = int(str(prime) + str(num))
                if all((int(new_num) % i != 0 for i in range(2, int(new_num ** 0.5) + 1))):
                    right_truncatable_primes.append(new_num)
    return sorted(right_truncatable_primes)