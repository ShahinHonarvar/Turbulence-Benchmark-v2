def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 17):
        substr = s[i:i + 18]
        if substr == substr[::-1]:
            result.add(substr)
    return result