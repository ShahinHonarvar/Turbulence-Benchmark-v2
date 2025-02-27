def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    length = 223
    s_len = len(s)
    for i in range(s_len - length + 1):
        substring = s[i:i + length]
        if len(substring) < 2 or substring != substring[::-1]:
            continue
        if all((c.isalpha() for c in substring)):
            result.add(substring)
    return result