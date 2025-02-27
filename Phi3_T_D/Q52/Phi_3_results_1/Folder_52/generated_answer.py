def palindrome_of_length_n(s):
    length = 423
    result = set()
    s_lower = s.lower()
    for i in range(len(s_lower) - length + 1):
        substring = s_lower[i:i + length]
        if substring == substring[::-1]:
            result.add(substring)
    return result