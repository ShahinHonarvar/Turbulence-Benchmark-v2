def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]
    substr = s[15:95]
    palindromes = set()
    for i in range(len(substr)):
        for j in range(i + 18, min(i + 74, len(substr) + 1)):
            candidate = substr[i:j]
            if candidate.isalpha() and is_palindrome(candidate.lower()):
                palindromes.add(candidate)
    return palindromes