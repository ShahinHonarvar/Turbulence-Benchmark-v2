def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    substring = s[125:284]
    palindromes = set()
    for length in range(109, 127):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate.isalpha() and is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes