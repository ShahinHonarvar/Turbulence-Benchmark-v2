def palindromes_between_indices(s):
    subset = s[5:9].lower()
    chars = sorted(set(subset))
    length = len(chars)
    palindromes = set()
    for i in range(length):
        for j in range(i, length):
            for k in range(j, length):
                for l in range(k, length):
                    for m in range(l, length):
                        for n in range(m, length):
                            for o in range(n, length):
                                for p in range(o, length):
                                    word = chars[i] + chars[j] + chars[k] + chars[l] + chars[m] + chars[n] + chars[o] + chars[p]
                                    if word == word[::-1] and len(word) >= 3:
                                        palindromes.add(word)
    return palindromes