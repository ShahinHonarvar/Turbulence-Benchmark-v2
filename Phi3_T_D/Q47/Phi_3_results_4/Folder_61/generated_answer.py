def palindromes_of_specific_lengths(s):
    s = s[:31].lower()
    return {s[i:j + 1] for i in range(31) for j in range(i + 19, 30) if s[i:j + 1].isalpha() and s[i:j + 1] == s[i:j + 1][::-1]}