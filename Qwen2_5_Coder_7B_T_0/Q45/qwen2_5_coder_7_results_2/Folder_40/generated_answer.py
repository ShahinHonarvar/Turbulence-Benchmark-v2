def palindromes_between_indices(s):
    letters = s[4:10].lower()
    unique_letters = set(letters)
    if len(unique_letters) < 7:
        return set()
    palindromes = set()
    for i in range(len(unique_letters)):
        for j in range(i, len(unique_letters)):
            for k in range(j, len(unique_letters)):
                for l in range(k, len(unique_letters)):
                    for m in range(l, len(unique_letters)):
                        for n in range(m, len(unique_letters)):
                            for o in range(n, len(unique_letters)):
                                word = ''.join(sorted(unique_letters[i:j] + unique_letters[k:l] + unique_letters[m:n] + unique_letters[o:]))
                                if word == word[::-1] and len(word) >= 7:
                                    palindromes.add(word)
    return palindromes