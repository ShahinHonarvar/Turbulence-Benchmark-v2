def palindromes_of_specific_lengths(s):
    start, end = (0, 100)
    s = s[start:end].lower()
    palindromes = set()
    for length in range(3, 16):
        for i in range(start + 1, end - length + 2):
            word = s[i:i + length]
            if word.isalpha() and word == word[::-1]:
                palindromes.add(word)
    return palindromes