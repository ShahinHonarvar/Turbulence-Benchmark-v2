def find_n_th_smallest_num(numbers):
    if 19 <= len(numbers) <= 190:
        return sorted(numbers)[18]
    raise ValueError('List of numbers is not within the expected range of indices')