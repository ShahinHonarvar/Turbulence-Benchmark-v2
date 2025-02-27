def palindromes_of_specific_lengths(s):
    return {s[i:j] for i in range(301) for j in range(i + 50, min(i + 61, 301)) if s[i:j].lower() == s[i:j][::-1] and s[i:j].isalpha()}