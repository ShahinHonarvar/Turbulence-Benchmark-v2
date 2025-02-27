def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    valid_palindromes = set()
    substring = s[:11]
    for i in range(len(substring)):
        for j in range(i + 3, min(i + 6, len(substring) + 1)):
            candidate = substring[i:j]
            if candidate.isalpha() and is_palindrome(candidate) and (3 <= len(candidate) <= 5):
                valid_palindromes.add(candidate.lower())
    return valid_palindromes