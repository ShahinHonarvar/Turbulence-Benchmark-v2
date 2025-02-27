def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result = set()
    n = 100
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    return result