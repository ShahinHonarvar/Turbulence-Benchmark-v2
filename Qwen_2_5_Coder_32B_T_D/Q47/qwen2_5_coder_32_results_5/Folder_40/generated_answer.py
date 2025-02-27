def palindromes_of_specific_lengths(s):
    s = s[:6].lower()
    a = set()
    for i in range(5):
        for j in range(i + 2, 6):
            b = s[i:j + 1]
            if b == b[::-1] and b.isalpha():
                a.add(b)
    return a