def palindromes_between_indices(s):
    subset = s[2:6].lower()
    unique_chars = set(subset)
    if len(unique_chars) < 3:
        return set()
    palindromes = set()
    for a in unique_chars:
        for b in unique_chars:
            for c in unique_chars:
                for d in unique_chars:
                    for e in unique_chars:
                        candidate = ''.join([a, b, c, d, e])
                        if candidate == candidate[::-1]:
                            palindromes.add(candidate)
    return palindromes