def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]
    return {s[i:j].lower() for i in range(29, 97) for j in range(12, 19) if is_palindrome(s[i:j]) and s[i:j].isalpha()}