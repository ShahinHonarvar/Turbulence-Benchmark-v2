def palindromes_between_indices(s):
    subset = s[4:8]
    subset = subset.lower()
    unique_chars = set(subset)
    palindromes = set()
    for i in range(len(unique_chars)):
        for j in range(i, len(unique_chars)):
            for k in range(j, len(unique_chars)):
                for l in range(k, len(unique_chars)):
                    for m in range(l, len(unique_chars)):
                        candidate = ''.join(sorted([unique_chars[i], unique_chars[j], unique_chars[k], unique_chars[l], unique_chars[m]]))
                        if candidate == candidate[::-1]:
                            palindromes.add(candidate)
    return palindromes