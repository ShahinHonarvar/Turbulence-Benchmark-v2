def is_perfect_num(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if sum == num and num != 0:
        return True
    else:
        return False

def if_perfect_num(numbers):
    try:
        return is_perfect_num(numbers[90])
    except IndexError:
        return False