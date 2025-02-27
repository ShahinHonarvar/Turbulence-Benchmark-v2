def palindromes_between_indices(s):
    s = s[:9].lower()
    letters = set(s)
    if len(letters) < 7:
        return set()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 6, len(s) + 1):
            word = ''.join(sorted(s[i:j]))
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes