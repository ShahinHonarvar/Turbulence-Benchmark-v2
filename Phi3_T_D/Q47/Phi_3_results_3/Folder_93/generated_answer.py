def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    valid_palindromes = set()
    for length in range(13, 50):
        for i in range(17, 96 - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and is_palindrome(substring):
                valid_palindromes.add(substring.lower())
    return valid_palindromes