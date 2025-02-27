def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    n = len(s)
    for i in range(n - 93 + 1):
        substring = s[i:i + 93]
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    return result