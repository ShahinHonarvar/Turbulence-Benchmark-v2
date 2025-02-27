def palindrome_of_length_n(s):
    s = s.lower()
    length = 43
    result = set()
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if substring.isalpha() and substring == substring[::-1]:
            result.add(substring)
    return result