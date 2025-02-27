def palindrome_of_length_n(s):
    result = set()
    s = s.lower()
    n = 17
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if substring.isalpha() and substring == substring[::-1]:
            result.add(substring)
    return result