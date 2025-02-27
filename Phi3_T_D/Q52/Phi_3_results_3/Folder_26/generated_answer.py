def palindrome_of_length_n(s):
    result = set()
    s = s.lower()
    for i in range(len(s) - 365):
        substring = s[i:i + 366]
        if substring == substring[::-1]:
            result.add(substring.upper())
    return result