def palindromes_of_specific_lengths(s):
    s = s[20:75].lower()
    p = set()
    for l in range(36, 43):
        for i in range(len(s) - l + 1):
            x = s[i:i + l]
            if x.isalpha() and x == x[::-1]:
                p.add(x)
    return p