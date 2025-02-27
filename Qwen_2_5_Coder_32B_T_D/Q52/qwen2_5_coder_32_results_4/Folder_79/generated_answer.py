def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    n = len(s)
    for i in range(n - 63):
        substring = s[i:i + 64]
        if substring.isalpha() and substring == substring[::-1]:
            result.add(substring)
    return result