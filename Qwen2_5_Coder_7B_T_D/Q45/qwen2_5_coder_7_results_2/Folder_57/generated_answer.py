def palindromes_between_indices(s):
    letters = s[2:6].lower()
    letters_set = set(letters)
    if len(letters_set) < 5:
        return set()
    palindromes = set()
    for i in range(len(letters_set)):
        for j in range(i, len(letters_set)):
            for k in range(j, len(letters_set)):
                for l in range(k, len(letters_set)):
                    for m in range(l, len(letters_set)):
                        candidate = ''.join(sorted([letters_set[i], letters_set[j], letters_set[k], letters_set[l], letters_set[m]]))
                        if candidate == candidate[::-1]:
                            palindromes.add(candidate)
    return palindromes