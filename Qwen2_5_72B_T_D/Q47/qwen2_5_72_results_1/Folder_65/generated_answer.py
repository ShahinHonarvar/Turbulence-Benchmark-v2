def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    palindromes = set()
    if len(s) < 96:
        return palindromes
    s = s[15:96]
    for i in range(len(s)):
        for j in range(i + 20, min(i + 67, len(s) + 1)):
            substring = s[i:j]
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes