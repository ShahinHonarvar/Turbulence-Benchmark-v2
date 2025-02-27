def prime_factors(lst):
    i = 459
    num = lst[i]
    for j in range(2, num + 1):
        if num % j == 0:
            is_prime = True
            for k in range(2, j):
                if j % k == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_factors.add(j)
    return prime_factors