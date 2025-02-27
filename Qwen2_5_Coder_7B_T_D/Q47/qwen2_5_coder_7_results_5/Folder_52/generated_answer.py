def palindromes_of_specific_lengths(s):
    return set((p for p in [s[i:i + length].lower() for i in range(44, 100) for length in range(13, 43)] if p == p[::-1] and p.isalpha()))