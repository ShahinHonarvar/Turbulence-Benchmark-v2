def palindromes_between_indices(s):
    letters = s[6:9].lower()
    letters = set(letters)
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            for k in range(j, len(letters)):
                for l in range(k, len(letters)):
                    for m in range(l, len(letters)):
                        for n in range(m, len(letters)):
                            word = ''.join(sorted(letters[i:j] + letters[k:l] + letters[m:n] + letters[l:m] + letters[n:m] + letters[n + 1:]))
                            if word == word[::-1] and len(word) >= 3:
                                palindromes.add(word)
    return palindromes