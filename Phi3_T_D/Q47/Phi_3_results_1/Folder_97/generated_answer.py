def palindromes_of_specific_lengths(s):
    s = s[27:95].lower()
    palindromes = {s[i:i + length] for length in range(38, 50) for i in range(len(s) - length + 1) if s[i:i + length].isalpha()}
    return {p for p in palindromes if p == p[::-1]}