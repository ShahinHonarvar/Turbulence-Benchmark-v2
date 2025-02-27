def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result = set()
    n = 33
    for i in range(len(s) - n + 1):
        for j in range(i + n, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result