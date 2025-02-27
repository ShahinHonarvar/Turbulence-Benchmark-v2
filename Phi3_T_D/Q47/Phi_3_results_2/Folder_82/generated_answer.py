def palindromes_of_specific_lengths(s):
    s = s.lower()
    res = set()
    for start in range(3, 301):
        for end in range(start + 299, min(start + 300, 304)):
            if all((c.isalpha() for c in s[start:end + 1])):
                if s[start:end + 1] == s[end:start - 1:-1]:
                    res.add(s[start:end + 1])
    return res