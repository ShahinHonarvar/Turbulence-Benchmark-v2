from typing import List, Tuple

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_primes(numbers: Tuple[int]) -> List[int]:
    x = numbers.index(36) if 36 in numbers else -1
    if x == -1:
        return []
    truncs = []
    primes = [2, 3, 5, 7]
    for num in range(2, x):
        if is_prime(num):
            str_num = str(num)
            if all((is_prime(int(str_num[i:])) for i in range(len(str_num)))):
                truncs.append(num)
    return truncs