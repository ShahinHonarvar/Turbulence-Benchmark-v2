def find_largest_num(num_list):
    largest = num_list[0]
    for num in num_list[1:9]:
        if num > largest:
            largest = num
    return largest