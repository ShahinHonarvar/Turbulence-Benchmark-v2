def palindromes_of_specific_lengths(s):
    s = s[35:89]
    relevant_substrings = [s[i:i + length] for length in range(24, 34) for i in range(len(s) - length + 1)]
    palindromes = set()
    for sub in relevant_substrings:
        sub = sub.lower()
        if sub.isalpha() and sub == sub[::-1]:
            palindromes.add(sub)
    return palindromes