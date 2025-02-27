def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    substring = s[65:100]
    palindromes = set()
    for length in range(26, 34):
        for i in range(len(substring) - length + 1):
            part = substring[i:i + length]
            if part.isalpha() and is_palindrome(part):
                palindromes.add(part)
    return palindromes