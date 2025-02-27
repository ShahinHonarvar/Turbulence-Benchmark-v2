from typing import List, Set

def composite_nums_between_indices(numbers: List[int]) -> Set[int]:

    def is_composite(n: int) -> bool:
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    return {num for num in numbers[75:86] if is_composite(num)}