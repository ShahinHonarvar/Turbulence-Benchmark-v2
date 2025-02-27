def palindromes_between_indices(s):
    subset = s[2:6].lower()
    chars = set(subset)
    palindromes = set()
    for i in range(len(subset)):
        for j in range(i + 4, len(subset) + 1):
            word = ''.join(sorted(subset[i:j]))
            if word == word[::-1] and len(word) >= 4:
                palindromes.add(word)
    return palindromes