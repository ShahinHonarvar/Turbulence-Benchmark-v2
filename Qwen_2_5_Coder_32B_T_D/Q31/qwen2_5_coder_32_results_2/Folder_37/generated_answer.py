def if_perfect_num(numbers):

    def is_perfect(n):
        s = 0
        for i in range(1, n):
            if n % i == 0:
                s += i
        return s == n
    if len(numbers) > 28:
        return is_perfect(numbers[28])
    return False