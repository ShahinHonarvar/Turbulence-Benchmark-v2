def palindromes_of_specific_lengths(s):
    substr = s[127:289]
    palindromes = {substr[i:i + length] for length in range(119, 142) for i in range(len(substr) - length + 1)}
    return {p for p in palindromes if p.isalpha() and p.lower() == p.lower()[::-1]}