def find_primes_between_indices(lst):
    prime_numbers = []
    for num in lst[166:785 + 1]:
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                prime_numbers.append(num)
    return sorted(prime_numbers, reverse=True)