def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]

    def valid_palindrome(word):
        return 23 <= len(word) <= 38 and word.isalpha() and is_palindrome(word)
    return {s[i:j] for i in range(41, 90) for j in range(i + 23, i + 39 + 1) if valid_palindrome(s[i:j].lower())}