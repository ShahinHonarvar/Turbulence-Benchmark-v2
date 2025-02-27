def all_substring_of_size_n(text):
    length = 146
    seen = set()
    result = set()
    for i in range(len(text) - length + 1):
        substring = text[i:i + length]
        if len(set(substring)) == length:
            if substring not in seen:
                seen.add(substring)
                result.add(substring)
    return list(result)