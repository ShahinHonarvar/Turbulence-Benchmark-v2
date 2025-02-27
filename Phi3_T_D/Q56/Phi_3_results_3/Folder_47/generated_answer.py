def all_substring_of_size_n(s):
    result = set()
    len_s = len(s)
    if len_s < 91:
        return list(result)
    for i in range(len_s - 90):
        temp_set = set()
        for j in range(91):
            if s[i + j] in temp_set:
                break
            temp_set.add(s[i + j])
            if len(temp_set) == 91:
                result.add(''.join(temp_set))
    return list(result)