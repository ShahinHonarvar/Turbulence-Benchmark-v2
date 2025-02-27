def palindrome_of_length_n(s):
    result = set()
    s = s.lower()
    for i in range(len(s) - 205):
        substring = s[i:i + 206]
        if substring == substring[::-1]:
            result.add(substring)
    return result