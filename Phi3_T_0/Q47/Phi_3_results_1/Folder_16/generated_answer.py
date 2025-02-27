def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]

    def valid_palindrome(word):
        return is_palindrome(word) and 51 <= len(word) <= 60 and word.isalpha()
    return {s[i:j] for i in range(15, 87) for j in range(i + 51, i + 61) if valid_palindrome(s[i:j].lower())}