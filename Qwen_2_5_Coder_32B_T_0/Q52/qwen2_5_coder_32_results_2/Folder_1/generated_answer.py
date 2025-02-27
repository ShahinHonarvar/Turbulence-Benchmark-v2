def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 26):
        substring = s[i:i + 27]
        if substring.isalpha() and substring == substring[::-1]:
            result.add(substring)
    return result