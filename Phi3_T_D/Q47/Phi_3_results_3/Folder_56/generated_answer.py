def palindromes_of_specific_lengths(s):
    s = s[1:10].lower()
    palindromes = {s[i:i + length] for length in range(3, 8) for i in range(len(s) - length + 1) if s[i:i + length] == s[i:i + length][::-1]}
    return {p for p in palindromes if p.isalpha()}