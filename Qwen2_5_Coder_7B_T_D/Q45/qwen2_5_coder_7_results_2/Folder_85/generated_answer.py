def palindromes_between_indices(s):
    sub_str = s[2:9].lower()
    letters = sorted(set(sub_str))
    length = 7
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            for k in range(j, len(letters)):
                for l in range(k, len(letters)):
                    for m in range(l, len(letters)):
                        for n in range(m, len(letters)):
                            for o in range(n, len(letters)):
                                word = letters[i] + letters[j] + letters[k] + letters[l] + letters[m] + letters[n] + letters[o]
                                if word == word[::-1]:
                                    palindromes.add(word)
    return palindromes