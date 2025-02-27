def palindromes_between_indices(s):
    substr = s[4:10]
    letters = set(substr.lower())
    if len(letters) < 3:
        return set()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            for k in range(j + 1, len(letters)):
                for a in letters:
                    for b in letters:
                        for c in letters:
                            if a == b or b == c or a == c:
                                continue
                            word = a + b + c
                            if word == word[::-1]:
                                palindromes.add(word)
    return palindromes