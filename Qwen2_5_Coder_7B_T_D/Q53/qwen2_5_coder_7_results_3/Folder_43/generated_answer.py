def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = 49
    result = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if substring == substring[::-1] and substring.isalpha() and (len(substring) >= 49):
            result.add(substring)
    return result