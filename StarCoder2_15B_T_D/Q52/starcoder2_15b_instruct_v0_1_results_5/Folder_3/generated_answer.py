def palindrome_of_length_n(text):
    result = set()
    n = 100
    for i in range(len(text) - n + 1):
        substring = text[i:i + n]
        if substring == substring[::-1]:
            if all((c.isalpha() for c in substring)):
                result.add(substring)
    return result