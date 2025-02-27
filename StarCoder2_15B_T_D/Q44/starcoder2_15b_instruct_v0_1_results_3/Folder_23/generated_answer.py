import math

def composite_nums_between_indices(lst):
    composite_nums = set()
    for i, num in enumerate(lst):
        if i >= 20 and i <= 30:
            is_composite = False
            for j in range(2, int(math.sqrt(num)) + 1):
                if num % j == 0:
                    is_composite = True
                    break
            if is_composite:
                composite_nums.add(num)
    return composite_nums