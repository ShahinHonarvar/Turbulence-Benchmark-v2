def all_substring_of_size_n(s):
    length = 10
    set_count = set()
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if len(set(substring)) == length:
            set_count.add(substring)
    return list(set_count)