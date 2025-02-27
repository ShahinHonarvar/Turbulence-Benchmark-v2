def palindrome_of_length_n(s):
    s = s.lower().replace(' ', '')
    result = set()
    for i in range(len(s) - 14):
        substring = s[i:i + 15]
        if substring == substring[::-1]:
            result.add(substring)
    return result