def palindromes_between_indices(s):
    letters = s[4:7]
    letters = letters.lower()
    result = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters) + 1):
            for k in range(len(letters)):
                for l in range(k + 1, len(letters) + 1):
                    for m in range(len(letters)):
                        for n in range(m + 1, len(letters) + 1):
                            for o in range(len(letters)):
                                for p in range(o + 1, len(letters) + 1):
                                    for q in range(len(letters)):
                                        for r in range(q + 1, len(letters) + 1):
                                            subletters = letters[i:j] + letters[k:l] + letters[m:n] + letters[o:p] + letters[q:r]
                                            if len(subletters) >= 3 and subletters == subletters[::-1]:
                                                result.add(subletters)
    return result