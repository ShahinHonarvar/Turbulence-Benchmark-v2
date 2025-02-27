def palindrome_of_length_n(s):
    s = s.lower()
    n = 56
    result = set()
    length = len(s)
    for i in range(length - n + 1):
        substring = s[i:i + n]
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    return result