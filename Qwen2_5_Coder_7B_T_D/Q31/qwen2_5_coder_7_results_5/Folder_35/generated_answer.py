def if_perfect_num(numbers):
    if len(numbers) > 993:
        num = numbers[993]
        sum = 1
        i = 2
        while i * i <= num:
            if num % i:
                i += 1
            else:
                if i * (num // i) == num:
                    sum = sum + i + num // i
                else:
                    sum = sum + i
                i += 1
        if sum == num and num != 1:
            return True
        else:
            return False
    else:
        return False