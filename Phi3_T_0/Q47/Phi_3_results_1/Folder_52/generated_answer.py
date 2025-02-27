def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]

    def valid_palindrome(word):
        return is_palindrome(word) and 13 <= len(word) <= 42 and word.isalpha()
    return {s[i:j] for i in range(44, 100) for j in range(i + 13, min(i + 43, 100)) if valid_palindrome(s[i:j].lower())}