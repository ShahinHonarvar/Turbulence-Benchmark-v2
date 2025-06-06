def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result = set()
    length = len(s)
    for start in range(length):
        for end in range(start + 3, length + 1):
            substring = s[start:end]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result