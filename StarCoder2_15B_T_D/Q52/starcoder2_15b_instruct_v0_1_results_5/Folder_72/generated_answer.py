def palindrome_of_length_n(s):
    n = 16
    result = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if substring == substring[::-1]:
            if all((c.isalpha() for c in substring)):
                result.add(substring)
    return result