def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    specified_substring = s[11:88]
    palindromes_set = set()
    for length in range(4, 6):
        for start in range(len(specified_substring) - length + 1):
            candidate = specified_substring[start:start + length]
            if candidate.isalpha() and is_palindrome(candidate):
                palindromes_set.add(candidate.lower())
    return palindromes_set