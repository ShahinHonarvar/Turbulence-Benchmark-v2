def palindrome_of_length_n(s):
    n = 90
    result = set()
    s = s.lower()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if substring == substring[::-1]:
            result.add(substring)
    return result