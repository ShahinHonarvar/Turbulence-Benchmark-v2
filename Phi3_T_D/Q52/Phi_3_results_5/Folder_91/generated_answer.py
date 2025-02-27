def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    length = 7
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if substring == substring[::-1]:
            result.add(substring.upper())
    return result