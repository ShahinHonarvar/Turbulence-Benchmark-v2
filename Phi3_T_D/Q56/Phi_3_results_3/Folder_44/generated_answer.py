def all_substring_of_size_n(s):
    substrings = set()
    max_len = len(s)
    for i in range(max_len):
        for j in range(i + 1, max_len):
            if j - i + 1 == 90:
                temp_str = s[i:j + 1]
                if len(set(temp_str)) == 90:
                    substrings.add(temp_str)
    return list(substrings)