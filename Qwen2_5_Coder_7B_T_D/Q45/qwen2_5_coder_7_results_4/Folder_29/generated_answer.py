def palindromes_between_indices(s):
    s = s[2:10]
    s = s.lower()
    letters = list(set(s))
    length = len(letters)
    result = set()
    for i in range(length):
        for j in range(i, length):
            for k in range(i, length):
                for l in range(i, length):
                    for m in range(i, length):
                        for n in range(i, length):
                            word = letters[i] + letters[j] + letters[k] + letters[l] + letters[m] + letters[n]
                            if word == word[::-1]:
                                result.add(word)
    return result