def palindrome_of_length_n(text):
    n = 475
    res = set()
    for i in range(len(text) - n + 1):
        substring = text[i:i + n]
        if substring == substring[::-1]:
            if all((ch.isalpha() for ch in substring)):
                res.add(substring)
    return res