def palindrome_of_length_n(s):
    result = set()
    s = s.lower()
    n = len(s)
    for i in range(n - 474):
        substring = s[i:i + 475]
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    return result