def palindrome_of_length_n(s):
    result = set()
    s = s.lower()
    for i in range(len(s) - 422):
        substring = s[i:i + 423]
        if substring == substring[::-1]:
            result.add(substring.upper())
    return result