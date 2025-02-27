def palindromes_of_specific_lengths(s):
    s = s[32:80].lower()
    result = set()
    for i in range(len(s) - 34):
        for j in range(i + 35, min(i + 42, len(s)) + 1):
            t = s[i:j]
            if t.isalpha() and t == t[::-1]:
                result.add(t)
    return result