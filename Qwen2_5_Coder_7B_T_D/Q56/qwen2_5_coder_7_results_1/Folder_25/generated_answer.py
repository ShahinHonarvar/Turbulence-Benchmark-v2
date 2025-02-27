def all_substring_of_size_n(s):
    n = 67
    substrings = set()
    result = []
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == len(substring):
            substrings.add(substring)
    for substring in substrings:
        result.append(substring)
    return result