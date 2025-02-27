def palindromes_between_indices(s):
    indices = s[1:6].lower()
    letters = set(indices)
    if len(letters) < 3:
        return set()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            for k in range(j + 1, len(letters)):
                for l in range(k + 1, len(letters)):
                    for m in range(l + 1, len(letters)):
                        for n in range(m + 1, len(letters)):
                            word = ''.join(sorted(letters[i:j] + letters[j:k] + letters[k:l] + letters[l:m] + letters[m:n] + letters[n:]))
                            if word == word[::-1] and len(word) >= 6:
                                palindromes.add(word)
    return palindromes