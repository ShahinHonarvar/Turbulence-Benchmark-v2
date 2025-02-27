def all_substring_of_size_n(s):
    length = 35
    seen = set()
    result = []
    for i in range(len(s) - length + 1):
        substr = s[i:i + length]
        if len(substr) == length and len(set(substr)) == length:
            if substr not in seen:
                seen.add(substr)
                result.append(substr)
    return result