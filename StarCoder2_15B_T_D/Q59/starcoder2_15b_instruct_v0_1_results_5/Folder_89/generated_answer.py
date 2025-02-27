def all_left_truncatable_prime(numbers):
    x = numbers[97]
    result = []
    for i in range(2, x):
        is_left_truncatable_prime = True
        for j in range(len(str(i))):
            if int(str(i)[j:]) < 2 or not is_prime(int(str(i)[j:])):
                is_left_truncatable_prime = False
                break
        if is_left_truncatable_prime:
            result.append(i)
    return sorted(result, reverse=True)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True