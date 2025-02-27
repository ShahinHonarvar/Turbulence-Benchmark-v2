def palindrome_of_length_n(s):
    n = 95
    s = s.lower()
    result = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    return result