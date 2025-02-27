def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    substring = s[63:71]
    palindromes = set()
    for length in range(4, 6):
        for i in range(len(substring) - length + 1):
            part = substring[i:i + length]
            if is_palindrome(part) and part.isalpha():
                palindromes.add(part)
    return palindromes