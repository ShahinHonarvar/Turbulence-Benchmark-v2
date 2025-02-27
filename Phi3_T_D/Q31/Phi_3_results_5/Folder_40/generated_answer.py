def if_perfect_num(lst):
    if 7 < len(lst):
        return is_perfect_number(lst[7])
    return False

def is_perfect_number(number):
    sum = 1
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            sum += i
            if i != number // i:
                sum += number // i
    return sum == number