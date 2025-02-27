def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 84):
        substring = s[i:i + 92]
        if substring == substring[::-1]:
            result.add(substring.upper())
    return result