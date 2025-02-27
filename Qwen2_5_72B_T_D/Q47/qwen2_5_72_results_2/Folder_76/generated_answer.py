def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    substr = s[101:293]
    palindromes = set()
    for i in range(len(substr)):
        for j in range(i + 154, min(i + 183, len(substr) + 1)):
            candidate = substr[i:j]
            if candidate.isalpha() and is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes