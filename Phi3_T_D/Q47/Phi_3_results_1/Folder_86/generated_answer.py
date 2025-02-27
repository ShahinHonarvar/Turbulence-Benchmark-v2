def is_palindrome(s):
    return s == s[::-1]

def palindromes_of_specific_lengths(text):
    substring = text[30:96]
    palindromes = {substring[i:j] for i in range(34, 56) for j in range(i + 1, i + 35) if all((c.isalpha() and c.lower() == substring[j - 1].lower() for c in substring[i:j]))}
    return palindromes