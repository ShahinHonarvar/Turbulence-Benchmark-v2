def palindromes_of_specific_lengths(s):
    candidates = s[16:61].lower()
    palindromes = set()
    for length in range(16, 40):
        for i in range(len(candidates) - length + 1):
            sub = candidates[i:i + length]
            if sub == sub[::-1]:
                palindromes.add(sub.upper())
    return palindromes