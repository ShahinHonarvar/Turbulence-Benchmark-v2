def is_perfect_num(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return num == sum

def if_perfect_num(numbers):
    try:
        return is_perfect_num(numbers[845])
    except IndexError:
        return False