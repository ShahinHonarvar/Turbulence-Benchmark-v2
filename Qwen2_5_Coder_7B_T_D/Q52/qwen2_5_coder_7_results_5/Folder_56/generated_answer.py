def palindrome_of_length_n(s):
    s = s.lower()
    n = len(s)
    result = set()
    for i in range(n):
        for j in range(i + 95, n + 1):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result