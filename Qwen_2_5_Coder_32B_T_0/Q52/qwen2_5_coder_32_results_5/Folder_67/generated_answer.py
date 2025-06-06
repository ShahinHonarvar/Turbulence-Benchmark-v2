def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 41):
        substring = s[i:i + 42]
        if substring.isalpha() and substring == substring[::-1]:
            result.add(substring)
    return result