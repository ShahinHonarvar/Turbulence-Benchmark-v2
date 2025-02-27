def palindromes_between_indices(s):
    indices = s[2:9]
    candidates = set([indices.lower()])
    palindromes = set()
    for length in range(4, len(candidates) + 1):
        for candidate in candidates:
            for i in range(len(candidate) - length + 1):
                sub = candidate[i:i + length]
                if sub == sub[::-1]:
                    palindromes.add(sub)
    return palindromes