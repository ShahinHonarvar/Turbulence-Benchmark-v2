def find_n_th_smallest_num(input_list):
    """Find the 19th smallest number from index 40 to index 75, both inclusive"""
    sorted_list = sorted(input_list[40:76])
    return sorted_list[18]