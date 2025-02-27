def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result = set()
    for center in range(len(s)):
        for offset in range(78):
            if center - offset < 0 or center + offset >= len(s):
                continue
            substr = s[center - offset:center + offset + 1]
            if substr == substr[::-1]:
                result.add(substr)
    return result