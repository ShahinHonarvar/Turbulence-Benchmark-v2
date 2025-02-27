def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]

    def valid_characters(word):
        return all(('a' <= c <= 'z' for c in word.lower()))
    palindromes = set()
    for i in range(29, 99):
        for length in range(6, 10):
            if i + length > len(s):
                break
            substring = s[i:i + length]
            if is_palindrome(substring) and valid_characters(substring):
                palindromes.add(substring.lower())
    return palindromes