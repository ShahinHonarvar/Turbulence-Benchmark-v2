def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    s = s[13:100]
    palindromes = set()
    for length in range(26, 30):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes