def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]
    substring = s[40:95]
    palindromes = set()
    for length in range(45, 52):
        for start in range(len(substring) - length + 1):
            part = substring[start:start + length]
            if part.isalpha() and is_palindrome(part.lower()):
                palindromes.add(part)
    return palindromes