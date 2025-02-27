def prime_factors(numbers):
    prime_list = set()
    num = numbers[24]
    while num % 2 == 0:
        prime_list.add(2)
        num = num // 2
    for i in range(3, int(num ** 0.5) + 1, 2):
        while num % i == 0:
            prime_list.add(i)
            num = num // i
    if num > 2:
        prime_list.add(num)
    return prime_list