def all_substring_of_size_n(s):
    n = 95
    result = []
    substring_set = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == len(substring):
            substring_set.add(substring)
    for substring in substring_set:
        result.append(substring)
    return result