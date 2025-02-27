def palindromes_of_specific_lengths(s):
    start, end = (13, 99)
    potential_palindromes = set((s[start:end + 1].lower()[i:j] for i in range(start, end - 24) for j in range(i + 26, min(i + 30, end + 1) + 1)))
    return {p for p in potential_palindromes if p == p[::-1] and p.isalpha()}