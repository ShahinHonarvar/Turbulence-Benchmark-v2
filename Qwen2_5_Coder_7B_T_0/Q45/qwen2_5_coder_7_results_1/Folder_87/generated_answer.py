def palindromes_between_indices(s):
    s = s[3:10].lower()
    letters = set(s)
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 2, len(s) + 1):
            word = ''.join(sorted(s[i:j]))
            if word == word[::-1] and len(word) >= 3:
                palindromes.add(word)
    return palindromes