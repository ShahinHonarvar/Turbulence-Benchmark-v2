def palindromes_between_indices(s):
    subset = s[6:10]
    letters = set(subset.lower())
    palindromes = set()
    for i in letters:
        for j in letters:
            for k in letters:
                for l in letters:
                    for m in letters:
                        candidate = i + j + k + l + m
                        if candidate.lower() == candidate[::-1].lower() and len(candidate) >= 5:
                            palindromes.add(candidate)
    return palindromes