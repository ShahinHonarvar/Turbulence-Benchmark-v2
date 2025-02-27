def palindromes_between_indices(s):
    s = s[1:5].lower()
    letters = set(s)
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            for k in range(j, len(letters)):
                for l in range(k, len(letters)):
                    char1, char2, char3, char4 = (letters[i], letters[j], letters[k], letters[l])
                    perm = set()
                    for a in [char1, char2, char3, char4]:
                        for b in [char1, char2, char3, char4]:
                            for c in [char1, char2, char3, char4]:
                                for d in [char1, char2, char3, char4]:
                                    perm.add(a + b + c + d)
                    for p in perm:
                        if p == p[::-1] and len(p) >= 4:
                            palindromes.add(p)
    return palindromes