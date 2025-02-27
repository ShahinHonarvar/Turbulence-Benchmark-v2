def if_decimal_is_divisible(binary_str):
    fibo_159 = fibonacci_number(159)
    decimal_value = int(binary_str, 2)
    return decimal_value % fibo_159 == 0

def fibonacci_number(n):
    fibo_series = [0, 1]
    for i in range(2, n + 1):
        next_fibo = fibo_series[-1] + fibo_series[-2]
        fibo_series.append(next_fibo)
    return fibo_series[n]