def palindromes_between_indices(s):
    subset = s[4:9]
    subset = subset.lower()
    chars = list(subset)
    unique_chars = set(chars)
    palindromes = set()
    for i in range(len(unique_chars)):
        for j in range(i, len(unique_chars)):
            for k in range(j, len(unique_chars)):
                for l in range(k, len(unique_chars)):
                    for m in range(l, len(unique_chars)):
                        for n in range(m, len(unique_chars)):
                            for o in range(n, len(unique_chars)):
                                for p in range(o, len(unique_chars)):
                                    for q in range(p, len(unique_chars)):
                                        for r in range(q, len(unique_chars)):
                                            for s in range(r, len(unique_chars)):
                                                word = ''.join(sorted(unique_chars[i] + unique_chars[j] + unique_chars[k] + unique_chars[l] + unique_chars[m] + unique_chars[n] + unique_chars[o] + unique_chars[p] + unique_chars[q] + unique_chars[r] + unique_chars[s]))
                                                if word == word[::-1] and len(word) >= 3:
                                                    palindromes.add(word)
    return palindromes