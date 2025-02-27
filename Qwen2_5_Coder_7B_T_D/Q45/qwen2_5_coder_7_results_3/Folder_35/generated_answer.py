def palindromes_between_indices(s):
    result = set()
    for i in range(2, 5):
        for j in range(i + 1, 5):
            for k in range(j + 1, 5):
                sub = s[i:j + 1] + s[j:k + 1] + s[k:]
                for p in set(permutations(sub)):
                    word = ''.join(p)
                    if word.lower() == word.lower()[::-1] and len(word) >= 4:
                        result.add(word.lower())
    return result