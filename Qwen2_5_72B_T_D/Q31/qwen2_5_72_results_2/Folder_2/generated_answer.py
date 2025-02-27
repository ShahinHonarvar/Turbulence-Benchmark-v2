def if_perfect_num(numbers):

    def is_perfect(num):
        return sum((i for i in range(1, num) if num % i == 0)) == num
    return is_perfect(numbers[702]) if len(numbers) > 702 else False