def palindromes_of_specific_lengths(s):
    start, end = (16, 77)
    res = set()
    for length in range(43, 48):
        for i in range(start, end - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and substring.lower() == substring[::-1].lower():
                res.add(substring.lower())
    return res