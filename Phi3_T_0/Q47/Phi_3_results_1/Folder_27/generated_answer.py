def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]

    def valid_palindrome(word):
        return 26 <= len(word) <= 29 and word.isalpha() and is_palindrome(word)
    return {s[i:j] for i in range(13, 100) for j in range(i + 26, i + 30) if valid_palindrome(s[i:j].lower())}