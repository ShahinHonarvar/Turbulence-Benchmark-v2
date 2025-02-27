def palindrome_of_length_n(s):
    length = 464
    result = set()
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if substring == substring[::-1]:
            if all((c.isalpha() for c in substring)):
                result.add(substring)
    return result