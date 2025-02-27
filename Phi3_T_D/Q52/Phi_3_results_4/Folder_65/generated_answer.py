def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = {string[i:i + 35][::-1] for i in range(len(string) - 34)}
    return {s for s in palindromes if s.isalpha() and s == s[::-1]}