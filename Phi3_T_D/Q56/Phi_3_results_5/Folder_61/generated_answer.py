def all_substring_of_size_n(s):
    return_list = set()
    for i in range(len(s) - 38):
        substr = s[i:i + 39]
        if len(set(substr)) == 39:
            return_list.add(substr)
    return list(return_list)