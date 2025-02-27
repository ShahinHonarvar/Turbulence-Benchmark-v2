def if_perfect_num(numbers):
    if 222 in range(len(numbers)):
        perfect_candidate = numbers[222]
        return sum([i for i in range(1, perfect_candidate) if perfect_candidate % i == 0]) == perfect_candidate
    else:
        return False