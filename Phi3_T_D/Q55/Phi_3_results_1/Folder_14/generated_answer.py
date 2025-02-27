def lists_with_product_equal_n(circular_list):
    N = -72
    valid_sublists = []

    def helper(start, current_product):
        while current_product != 1:
            if current_product % circular_list[start] == 0:
                target = N / circular_list[start]
                index = circular_list.index(target, (start + 1) % len(circular_list))
                if helper(index, 1):
                    valid_sublists.append(circular_list[start:index + 1])
                current_product //= circular_list[start]
            start = (start + 1) % len(circular_list)
        return current_product == 1
    for i in range(len(circular_list)):
        if circular_list[i] == 0:
            continue
        elif helper(i, circular_list[i]):
            valid_sublists.append(circular_list[i:])
    return valid_sublists