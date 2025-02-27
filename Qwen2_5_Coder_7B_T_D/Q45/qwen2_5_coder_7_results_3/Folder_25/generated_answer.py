def palindromes_between_indices(s):
    letters = sorted(s[1:5].lower())
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            for k in range(j, len(letters)):
                for l in range(k, len(letters)):
                    for m in range(l, len(letters)):
                        word = ''.join(letters[i:j + 1] + letters[k:l + 1] + letters[m:])
                        if word == word[::-1] and len(word) >= 3:
                            palindromes.add(word)
    return palindromes