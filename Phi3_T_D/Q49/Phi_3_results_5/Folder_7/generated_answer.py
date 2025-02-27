from typing import List

def fibonacci_sequence(n: int) -> List[int]:
    fib_seq = [0, 1]
    while len(fib_seq) < n + 1:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq[n]

def decimal_from_binary(binary_str: str) -> int:
    return int(binary_str, 2)

def if_decimal_is_divisible(binary_str: str) -> bool:
    target_fib_number = fibonacci_sequence(160)
    decimal_num = decimal_from_binary(binary_str)
    return decimal_num % target_fib_number == 0