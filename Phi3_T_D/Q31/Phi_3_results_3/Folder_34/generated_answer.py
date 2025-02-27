def is_perfect_num(int_list):
    if 97 < len(int_list) and is_perfect(int_list[97]):
        return True
    return False

def is_perfect(number):
    if number < 2:
        return False
    return sum((i for i in range(1, number) if number % i == 0)) == number