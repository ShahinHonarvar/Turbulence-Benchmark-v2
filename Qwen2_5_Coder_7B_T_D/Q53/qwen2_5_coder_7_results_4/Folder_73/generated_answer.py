def palindrome_of_length_at_least_n(s):
    s = s.lower()
    length = len(s)
    result = set()
    for start in range(length):
        for end in range(start + 94, length + 1):
            substring = s[start:end]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result