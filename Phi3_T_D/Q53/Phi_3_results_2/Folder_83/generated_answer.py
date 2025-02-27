def palindrome_of_length_at_least_n(s):

    def is_valid_letter(char):
        return 'a' <= char <= 'z'

    def is_palindrome(word):
        return word == word[::-1]
    s = s.lower()
    palindromes = set((s[i:j] for i in range(len(s)) for j in range(i + 60, len(s) + 1) if all((is_valid_letter(char) for char in s[i:j])) and is_palindrome(s[i:j])))
    return palindromes