def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]

    def valid_palindrome(word):
        return len(word) >= 5 and len(word) <= 10 and word.isalpha() and is_palindrome(word)
    return {word.lower() for word in s[100:201].split() if valid_palindrome(word)}