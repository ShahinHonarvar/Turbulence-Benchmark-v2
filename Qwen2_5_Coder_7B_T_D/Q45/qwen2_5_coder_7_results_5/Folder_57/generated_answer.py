def palindromes_between_indices(s):
    subset = s[2:6]
    subset = subset.lower()
    unique_chars = set(subset)
    palindromes = set()
    for i in range(len(unique_chars)):
        for j in range(i, len(unique_chars)):
            for k in range(j, len(unique_chars)):
                for l in range(k, len(unique_chars)):
                    for m in range(l, len(unique_chars)):
                        for n in range(m, len(unique_chars)):
                            word = unique_chars[i] + unique_chars[j] + unique_chars[k] + unique_chars[l] + unique_chars[m] + unique_chars[n]
                            if word == word[::-1] and len(word) >= 5:
                                palindromes.add(word)
    return palindromes