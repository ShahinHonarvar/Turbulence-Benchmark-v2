def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = {s[i:i + 78] for i in range(len(s) - 77)}
    return {p for p in palindromes if p == p[::-1]}