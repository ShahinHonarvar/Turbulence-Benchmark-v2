def palindromes_between_indices(s):
    s = s[4:10].lower()
    letters = set(s)
    palindromes = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            word = s[i:j + 1]
            if word == word[::-1] and len(word) >= 5:
                palindromes.add(word)
    return palindromes