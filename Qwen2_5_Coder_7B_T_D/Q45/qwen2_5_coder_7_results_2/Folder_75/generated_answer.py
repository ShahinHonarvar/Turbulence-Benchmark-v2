def palindromes_between_indices(s):
    result = set()
    letters = s[2:5]
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            for k in range(j, len(letters)):
                for l in range(k, len(letters)):
                    for m in range(l, len(letters)):
                        for n in range(m, len(letters)):
                            word = letters[i] + letters[j] + letters[k] + letters[l] + letters[m] + letters[n]
                            if word.lower() == word.lower()[::-1] and len(word) >= 3:
                                result.add(word.lower())
    return result