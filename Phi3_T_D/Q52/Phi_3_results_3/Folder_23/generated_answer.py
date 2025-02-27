def palindrome_of_length_n(s):
    set_of_palindromes = {s[i:i + 69].lower() for i in range(len(s) - 68) if s[i:i + 69].lower() == s[i:i + 69].lower()[::-1]}
    return {p for p in set_of_palindromes if p.isalpha()}