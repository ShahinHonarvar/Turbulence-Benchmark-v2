def palindromes_between_indices(s):
    s = s[2:10].lower()
    letters = set(s)
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 3, len(s) + 1):
            word = ''.join(sorted(s[i:j]))
            if word == word[::-1] and len(word) >= 4:
                palindromes.add(word)
    return palindromes