def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    n = len(s)
    for i in range(n - 254):
        substring = s[i:i + 255]
        if substring == substring[::-1]:
            result.add(substring)
    return result