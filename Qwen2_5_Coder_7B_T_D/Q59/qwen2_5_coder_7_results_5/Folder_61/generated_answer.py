def all_left_truncatable_prime(numbers):
    x = numbers[3]
    primes = [2, 3, 5, 7]
    result = []
    for num in range(10, x):
        num_str = str(num)
        if '0' in num_str:
            continue
        is_prime = True
        for i in range(len(num_str)):
            if int(num_str[i:]) not in primes:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
            result.append(num)
    return sorted(result, reverse=True)