def palindrome_of_length_n(s):
    s = s.lower()
    length = 181
    potential_palindromes = [s[i:i + length] for i in range(len(s) - length + 1)]
    palindromes = {p for p in potential_palindromes if p == p[::-1] and p.isalpha()}
    return palindromes