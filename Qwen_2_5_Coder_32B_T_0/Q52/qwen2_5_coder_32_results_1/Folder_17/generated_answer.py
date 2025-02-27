def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    n = 289
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if substring.isalpha() and substring == substring[::-1]:
            result.add(substring)
    return result