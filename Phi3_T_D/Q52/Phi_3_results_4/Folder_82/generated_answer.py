def palindrome_of_length_n(s):
    s = s.lower()

    def is_palindrome(word):
        return word == word[::-1]
    substrings = {s[i:i + 28] for i in range(len(s) - 27)}
    palindromes = {sub for sub in substrings if len(sub) == 28 and all((ch.isalpha() for ch in sub)) and is_palindrome(sub)}
    return palindromes