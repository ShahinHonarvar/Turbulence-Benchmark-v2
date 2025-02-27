def palindromes_of_specific_lengths(s):
    s = s[1:8].lower()
    result = set()
    for i in range(len(s) - 2):
        for j in range(i + 3, min(i + 5, len(s)) + 1):
            p = s[i:j]
            if p.isalpha() and p == p[::-1]:
                result.add(p)
    return result