def return_binary_or_hexa(numbers):
    a = numbers[40]
    b = numbers[200]
    present_numbers = set(numbers[41:200])
    missing_sum = sum(set(range(a + 1, b)) - present_numbers)
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_function():
    example_input = tuple(range(1000))
    print(return_binary_or_hexa(example_input))
    example_input = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500)
    print(return_binary_or_hexa(example_input))