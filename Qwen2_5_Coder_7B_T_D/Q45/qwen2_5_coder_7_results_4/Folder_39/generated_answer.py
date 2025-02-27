def palindromes_between_indices(s):
    subset = s[2:6]
    letters = sorted(set(subset.lower()))
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            for k in range(j, len(letters)):
                for l in range(k, len(letters)):
                    for m in range(l, len(letters)):
                        word = ''.join(letters[i]) * 2 + ''.join(letters[j]) * 2 + ''.join(letters[k]) * 2 + ''.join(letters[l]) * 2 + ''.join(letters[m]) * 2
                        if word == word[::-1] and len(word) >= 3:
                            palindromes.add(word)
    return palindromes