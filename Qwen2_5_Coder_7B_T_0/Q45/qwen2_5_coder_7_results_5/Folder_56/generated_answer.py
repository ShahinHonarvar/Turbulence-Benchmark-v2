def palindromes_between_indices(s):
    letters = s[5:10].lower()
    unique_letters = set(letters)
    palindromes = set()
    for i in range(len(unique_letters)):
        for j in range(i, len(unique_letters)):
            for k in range(j, len(unique_letters)):
                for l in range(k, len(unique_letters)):
                    for m in range(l, len(unique_letters)):
                        for n in range(m, len(unique_letters)):
                            for o in range(n, len(unique_letters)):
                                for p in range(o, len(unique_letters)):
                                    for q in range(p, len(unique_letters)):
                                        for r in range(q, len(unique_letters)):
                                            for s in range(r, len(unique_letters)):
                                                word = ''.join(sorted(unique_letters[i:j] + unique_letters[k:l] + unique_letters[m:n] + unique_letters[o:p] + unique_letters[q:r] + unique_letters[s:]))
                                                if word == word[::-1] and len(word) >= 5:
                                                    palindromes.add(word)
    return palindromes