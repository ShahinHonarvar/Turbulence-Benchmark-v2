def palindromes_between_indices(s):
    s = s[1:6].lower()
    letters = list(s)
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            for k in range(j, len(letters)):
                for l in range(k, len(letters)):
                    for m in range(l, len(letters)):
                        word = ''.join(letters[i:j]) + ''.join(letters[k:l]) + ''.join(letters[m:])
                        if word == word[::-1] and len(word) >= 5:
                            palindromes.add(word)
    return palindromes