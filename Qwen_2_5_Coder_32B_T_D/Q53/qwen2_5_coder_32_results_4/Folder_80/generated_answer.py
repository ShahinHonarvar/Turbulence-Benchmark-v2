def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 29, n):
            substring = s[i:j + 1]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result