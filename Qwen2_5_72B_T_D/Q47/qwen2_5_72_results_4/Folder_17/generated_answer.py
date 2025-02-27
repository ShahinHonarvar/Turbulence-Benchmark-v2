def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    valid_range = s[22:96]
    palindromes = set()
    for length in range(52, 56):
        for i in range(len(valid_range) - length + 1):
            substring = valid_range[i:i + length]
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes