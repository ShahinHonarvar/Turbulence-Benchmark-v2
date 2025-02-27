def is_perfect_num(perfect_sq):
    return sum((i for i in range(1, int(perfect_sq ** 0.5) + 1) if perfect_sq % i == 0)) == perfect_sq

def if_perfect_num(numbers):
    return is_perfect_num(numbers[222]) if len(numbers) > 222 else False