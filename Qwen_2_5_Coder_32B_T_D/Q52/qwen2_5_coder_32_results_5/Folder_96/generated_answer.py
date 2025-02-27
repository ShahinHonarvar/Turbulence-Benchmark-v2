def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    length = len(s)
    for i in range(length - 83 + 1):
        substring = s[i:i + 83]
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    return result