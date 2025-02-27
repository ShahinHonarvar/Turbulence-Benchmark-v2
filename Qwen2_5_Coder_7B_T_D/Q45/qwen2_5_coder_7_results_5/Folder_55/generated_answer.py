def palindromes_between_indices(s):
    s = s[:3].lower()
    letters = set(s)
    result = set()
    for i in range(len(s)):
        for j in range(i + 3, len(s) + 1):
            for perm in set(permutations(letters, j - i)):
                word = ''.join(perm)
                if word == word[::-1]:
                    result.add(word)
    return result