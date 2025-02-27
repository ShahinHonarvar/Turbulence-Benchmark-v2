def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]
    return {word.lower() for word in (s[index:index + length] for length in range(57, 61) for index in range(13, 96 - length + 1)) if word.isalpha() and is_palindrome(word)}