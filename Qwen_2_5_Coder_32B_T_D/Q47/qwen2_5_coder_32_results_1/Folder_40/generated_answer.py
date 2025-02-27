def palindromes_of_specific_lengths(s):
    s = s[:6].lower()
    result = set()
    for i in range(len(s) - 2):
        for j in range(i + 2, min(i + 6, len(s) + 1)):
            w = s[i:j]
            if w.isalpha() and w == w[::-1]:
                result.add(w)
    return result