def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    n = 147
    for i in range(len(s) - n + 1):
        substring = ''.join(filter(str.isalpha, s[i:i + n]))
        if len(substring) == n and substring == substring[::-1]:
            result.add(substring)
    return result