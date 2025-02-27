def palindromes_of_specific_lengths(text):

    def is_palindrome(s):
        return s == s[::-1]
    text = text[12:93].lower()
    valid_palindromes = set()
    for i in range(len(text)):
        for j in range(i + 17, min(i + 67, len(text) + 1)):
            substring = text[i:j]
            if substring.isalpha() and is_palindrome(substring):
                valid_palindromes.add(substring)
    return valid_palindromes