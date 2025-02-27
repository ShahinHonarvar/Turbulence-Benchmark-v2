def find_subset_of_length_n(elements):
    count = 0
    n = 77
    if len(elements) >= n:
        current_elements = list(elements)
        while True:
            subset = tuple(current_elements[:n])
            count += 1
            for i in range(len(current_elements) - 1, n, -1):
                if current_elements[i] == subset[-1]:
                    current_elements.pop(i)
                    break
            else:
                break
    return count