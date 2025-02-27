def palindromes_of_specific_lengths(s):
    return set((p for p in s[11:84] if p.isalpha() and p.lower() == p[::-1].lower() and (13 <= len(p) <= 66)))