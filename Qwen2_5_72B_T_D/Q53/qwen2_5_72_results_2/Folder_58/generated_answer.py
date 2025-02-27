def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = 147
    length = len(s)
    result = set()
    for i in range(length):
        for j in range(i + n, length + 1):
            substr = s[i:j]
            if substr == substr[::-1]:
                result.add(substr)
    return result