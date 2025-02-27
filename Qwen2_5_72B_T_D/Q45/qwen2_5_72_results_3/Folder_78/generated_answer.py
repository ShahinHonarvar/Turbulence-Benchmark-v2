def palindromes_between_indices(s):
    substring = s[6:9].lower()
    chars = set(substring)
    palindromes = set()
    for c1 in chars:
        for c2 in chars:
            if c1 != c2 and c1 + c2 + c1 == (c1 + c2 + c1)[::-1]:
                palindromes.add(c1 + c2 + c1)
            if c1 == c2 and c1 * 3 == (c1 * 3)[::-1]:
                palindromes.add(c1 * 3)
    return palindromes