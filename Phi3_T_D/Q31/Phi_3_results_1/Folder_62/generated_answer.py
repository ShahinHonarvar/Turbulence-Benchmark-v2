from typing import List

def if_perfect_num(numbers: List[int]) -> bool:
    if 926 < len(numbers):
        return is_perfect(numbers[926])
    return False

def is_perfect(num: int) -> bool:
    if num < 2:
        return False
    divisors_sum = 1
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            divisors_sum += i
    return divisors_sum == num