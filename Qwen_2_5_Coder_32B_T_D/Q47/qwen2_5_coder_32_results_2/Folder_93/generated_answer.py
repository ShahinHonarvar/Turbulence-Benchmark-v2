def palindromes_of_specific_lengths(s):
    s = s[17:96].lower()
    return {s[i:j] for i in range(len(s) - 12) for j in range(i + 13, min(i + 50, len(s) + 1)) if s[i:j] == s[i:j][::-1] and s[i:j].isalpha()}