def all_substring_of_size_n(s):
    seen = set()
    length = len(s)
    for i in range(length - 86):
        substr = s[i:i + 87]
        if len(set(substr)) == 87:
            if substr not in seen:
                seen.add(substr)
    return list(seen)