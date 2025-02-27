def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 99):
        substring = s[i:i + 100]
        if substring.isalpha() and substring == substring[::-1]:
            result.add(substring)
    return result