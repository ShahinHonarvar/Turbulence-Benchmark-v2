def palindromes_between_indices(s):
    s = s[3:9].lower()
    chars = sorted(set(s))
    length = len(chars)
    palindromes = set()
    for i in range(length):
        for j in range(i, length):
            for k in range(j, length):
                for l in range(k, length):
                    for m in range(l, length):
                        for n in range(m, length):
                            word = chars[i] + chars[j] + chars[k] + chars[l] + chars[m] + chars[n]
                            if word == word[::-1]:
                                palindromes.add(word)
    return palindromes