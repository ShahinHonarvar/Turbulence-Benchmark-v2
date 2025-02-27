def palindrome_of_length_at_least_n(s):
    result = set()
    n = 31
    s = s.lower()
    for i in range(len(s) - n + 1):
        window = s[i:i + n]
        if window == window[::-1]:
            result.add(window)
    return result