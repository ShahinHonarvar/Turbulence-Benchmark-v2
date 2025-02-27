def palindromes_of_specific_lengths(s):
    subset = s[26:91].lower()
    palindromes = set()
    for length in range(27, 59):
        for i in range(len(subset) - length + 1):
            sub = subset[i:i + length]
            if sub.isalpha() and sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes