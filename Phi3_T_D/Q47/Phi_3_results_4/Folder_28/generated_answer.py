def palindromes_of_specific_lengths(s):
    return {s[i:j] for i in range(32, 72) for j in range(i + 20, 72) if s[i:j] == s[i:j][::-1] and all((c.isalpha() for c in s[i:j].lower()))}