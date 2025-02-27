def palindromes_between_indices(s):
    subset = s[4:9]
    subset = subset.lower()
    letters = list(subset)
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            for k in range(j, len(letters)):
                for l in range(k, len(letters)):
                    for m in range(l, len(letters)):
                        candidate = letters[i] + letters[j] + letters[k] + letters[l] + letters[m]
                        if candidate.lower() == candidate.lower()[::-1] and len(candidate) >= 5:
                            palindromes.add(candidate)
    return palindromes