def palindromes_between_indices(s):
    s = s[1:4].lower()
    letters = set(s)
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            for k in range(j, len(letters)):
                for l in range(k, len(letters)):
                    for m in range(l, len(letters)):
                        for n in range(m, len(letters)):
                            for o in range(n, len(letters)):
                                for p in range(o, len(letters)):
                                    for q in range(p, len(letters)):
                                        for r in range(q, len(letters)):
                                            for s in range(r, len(letters)):
                                                candidate = ''.join(sorted(letters[i:j + k + l + m + n + o + p + q + r + s]))
                                                if candidate == candidate[::-1] and len(candidate) >= 4:
                                                    palindromes.add(candidate)
    return palindromes