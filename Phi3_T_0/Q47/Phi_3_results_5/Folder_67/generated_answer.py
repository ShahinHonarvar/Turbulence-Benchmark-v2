def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]

    def valid_palindrome(word):
        return 26 <= len(word) <= 33 and word.isalpha() and is_palindrome(word)
    return {s[i:j] for i in range(65, 100) for j in range(i + 26, min(i + 34, 100)) if valid_palindrome(s[i:j].lower())}