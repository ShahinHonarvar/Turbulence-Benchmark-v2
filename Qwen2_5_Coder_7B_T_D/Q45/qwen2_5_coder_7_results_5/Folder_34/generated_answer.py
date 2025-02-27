def palindromes_between_indices(s):
    s = s[5:8].lower()
    letters = set(s)
    length = len(letters)
    if length < 2:
        return set()
    result = set()
    for i in range(length):
        for j in range(i + 1, length):
            for k in range(j + 1, length):
                for l in range(k + 1, length):
                    for m in range(l + 1, length):
                        word = ''.join(sorted(letters[i:j] + letters[k:l] + letters[m:]))
                        if word == word[::-1] and len(word) >= 4:
                            result.add(word)
    return result