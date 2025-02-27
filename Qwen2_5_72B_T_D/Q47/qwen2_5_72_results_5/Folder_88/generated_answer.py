def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    substring = s[11:88]
    palindromes = set()
    for length in range(4, 6):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate.isalpha() and is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes