def find_primes_between_indices(lst):
    prime_list = []
    for num in lst[19:72]:
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                prime_list.append(num)
    return sorted(prime_list)