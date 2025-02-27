def palindromes_of_specific_lengths(text):

    def is_palindrome(s):
        return s == s[::-1]
    text = text[:101]
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 3, min(i + 16, len(text) + 1)):
            substring = text[i:j]
            if substring.isalpha() and is_palindrome(substring.lower()):
                palindromes.add(substring)
    return palindromes