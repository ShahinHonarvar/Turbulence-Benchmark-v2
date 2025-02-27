def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = {s[i:i + 116] for i in range(len(s) - 115) if s[i:i + 116] == s[i:i + 116][::-1]}
    return {p for p in palindromes if p.isalpha()}