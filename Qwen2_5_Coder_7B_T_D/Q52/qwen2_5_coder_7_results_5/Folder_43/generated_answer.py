def palindrome_of_length_n(s):
    s = s.lower()
    n = len(s)
    result = set()
    for i in range(n - 50):
        substring = s[i:i + 51]
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    return result