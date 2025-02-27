def all_substring_of_size_n(input_string):
    n = 40
    seen = set()
    results = []
    for i in range(len(input_string) - n + 1):
        substring = input_string[i:i + n]
        if len(set(substring)) == n:
            if substring not in seen:
                results.append(substring)
                seen.add(substring)
    return results