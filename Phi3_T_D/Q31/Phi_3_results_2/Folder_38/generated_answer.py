def is_perfect_num(num):
    return num == sum((i for i in range(1, num) if num % i == 0))

def if_perfect_num(numbers_list):
    target_index = 38
    try:
        number_at_index = numbers_list[target_index]
        return is_perfect_num(number_at_index)
    except IndexError:
        return False