def palindromes_of_specific_lengths(s):
    res = set()
    for i in range(2, 9):
        for j in range(i + 2, min(i + 5, len(s) + 1)):
            substr = s[i:j]
            if substr.isalpha() and substr.lower() == substr[::-1].lower():
                res.add(substr.lower())
    return res