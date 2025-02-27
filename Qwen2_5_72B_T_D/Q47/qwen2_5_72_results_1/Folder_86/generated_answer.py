def palindromes_of_specific_lengths(text):

    def is_palindrome(s):
        return s == s[::-1]
    text = text[30:96]
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 34, min(i + 56, len(text) + 1)):
            substring = text[i:j]
            if substring.isalpha() and is_palindrome(substring.lower()):
                palindromes.add(substring)
    return palindromes