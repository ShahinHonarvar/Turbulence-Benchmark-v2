def all_substring_of_size_n(s):
    substrings = set()
    length = len(s)
    for i in range(length):
        if length - i < 78:
            break
        temp_set = set()
        temp_str = ''
        for j in range(i, i + 78):
            char = s[j]
            if char in temp_set:
                break
            temp_set.add(char)
            temp_str += char
            if len(temp_str) == 78:
                substrings.add(temp_str)
                break
    return list(substrings)