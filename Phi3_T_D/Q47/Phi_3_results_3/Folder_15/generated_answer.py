def palindromes_of_specific_lengths(s):
    s = s[:7].lower()
    return {s[i:j] for i in range(3, 7) for j in range(i + 3, 8) if s[i:j].isalpha() and s[i:j] == s[i:j][::-1]}