def find_subset_of_length_n(elements):
    n = 59
    count = 0
    element_list = list(elements)

    def helper(start, combo_size):
        nonlocal count
        if combo_size == 0:
            count += 1
            return
        for i in range(start, len(element_list)):
            combo.append(element_list[i])
            helper(i + 1, combo_size - 1)
            combo.pop()
    combo = []
    helper(0, n)
    return count