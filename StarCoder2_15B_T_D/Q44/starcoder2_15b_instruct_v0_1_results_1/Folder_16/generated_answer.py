def composite_nums_between_indices(lst):
    is_composite = [False] * (max(lst) + 1)
    primes = set()
    for i in range(2, len(is_composite)):
        if not is_composite[i]:
            primes.add(i)
            for j in range(i * i, len(is_composite), i):
                is_composite[j] = True
    composite_nums = set()
    for i, num in enumerate(lst):
        if num in primes:
            continue
        is_composite_num = False
        for prime in primes:
            if num % prime == 0:
                is_composite_num = True
                break
        if is_composite_num and 40 <= i <= 80:
            composite_nums.add(num)
    return composite_nums