def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    substr = s[:8]
    found_palindromes = set()
    for i in range(len(substr)):
        for length in range(4, 6):
            if i + length <= len(substr):
                candidate = substr[i:i + length]
                if candidate.isalpha() and is_palindrome(candidate):
                    found_palindromes.add(candidate.lower())
    return found_palindromes