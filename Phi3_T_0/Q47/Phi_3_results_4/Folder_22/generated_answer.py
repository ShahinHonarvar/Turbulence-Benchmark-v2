def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]

    def valid_palindrome(word):
        return len(word) >= 5 and len(word) <= 10 and word.isalpha()
    palindromes = set()
    for i in range(100, 201):
        for j in range(i + 4, min(i + 11, 201)):
            substring = s[i:j + 1].lower()
            if is_palindrome(substring) and valid_palindrome(substring):
                palindromes.add(substring)
    return palindromes