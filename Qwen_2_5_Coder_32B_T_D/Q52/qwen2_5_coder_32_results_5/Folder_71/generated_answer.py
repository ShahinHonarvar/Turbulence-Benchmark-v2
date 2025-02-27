def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    length = len(s)
    for i in range(length - 77):
        substring = s[i:i + 78]
        if substring.isalpha() and substring == substring[::-1]:
            result.add(substring)
    return result