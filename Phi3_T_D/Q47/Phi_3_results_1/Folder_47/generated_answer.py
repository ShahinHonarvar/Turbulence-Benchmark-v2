def palindromes_of_specific_lengths(s):
    s = s[39:95]
    palindromes = set()
    for length in range(14, 53):
        for start in range(0, len(s) - length + 1):
            word = s[start:start + length]
            if word.isalpha() and word.lower() == word[::-1].lower():
                palindromes.add(word)
    return palindromes