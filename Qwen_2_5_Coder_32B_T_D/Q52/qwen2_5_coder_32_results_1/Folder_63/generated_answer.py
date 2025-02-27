def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    n = len(s)
    for i in range(n - 17):
        substring = s[i:i + 18]
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    return result