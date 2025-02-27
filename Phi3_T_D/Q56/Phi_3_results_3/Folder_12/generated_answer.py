def all_substring_of_size_n(input_str):
    n = 47
    seen = set()
    substrings = []
    for i in range(len(input_str) - n + 1):
        substring = input_str[i:i + n]
        if len(set(substring)) == n:
            if substring not in seen:
                seen.add(substring)
                substrings.append(substring)
    return substrings