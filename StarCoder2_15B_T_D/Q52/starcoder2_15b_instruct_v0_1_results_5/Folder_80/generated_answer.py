def palindrome_of_length_n(string):
    substrings = [string[i:i + 276] for i in range(len(string) - 275)]
    palindromes = [s for s in substrings if s == s[::-1]]
    palindromes = [p for p in palindromes if p.isalpha()]
    return set(palindromes)