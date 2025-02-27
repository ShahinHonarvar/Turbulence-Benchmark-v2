def if_perfect_num(numbers):
    if len(numbers) > 20:
        sum = 0
        for i in range(1, numbers[20]):
            if numbers[20] % i == 0:
                sum += i
        if sum == numbers[20]:
            return True
        else:
            return False
    else:
        return False