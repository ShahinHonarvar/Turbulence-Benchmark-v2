def palindromes_of_specific_lengths(s: str) -> set:

    def is_palindrome(word):
        return word == word[::-1]
    substr = s[27:96]
    palindromes = {substr[i:j + 1] for i in range(len(substr)) for j in range(i + 48, min(i + 52, len(substr))) if substr[i:j + 1].isalpha() and is_palindrome(substr[i:j + 1].lower())}
    return palindromes