def find_second_smallest_num(num_list):
    if 28 <= len(num_list) <= 32 and len(num_list) > 1:
        target_slice = sorted(num_list[28:33])
        if len(target_slice) > 1:
            return target_slice[1]
    return None