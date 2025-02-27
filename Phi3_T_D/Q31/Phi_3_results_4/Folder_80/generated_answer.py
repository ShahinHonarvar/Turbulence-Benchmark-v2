def if_perfect_num(numbers):
    try:
        integer = numbers[746]
        divisors = [i for i in range(1, integer) if integer % i == 0]
        return sum(divisors) == integer
    except IndexError:
        return False