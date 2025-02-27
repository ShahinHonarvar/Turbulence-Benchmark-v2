def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]
    subset = s[27:78]
    valid_palindromes = set()
    for length in [18, 19]:
        for start in range(len(subset) - length + 1):
            candidate = subset[start:start + length].lower()
            if candidate.isalpha() and is_palindrome(candidate):
                valid_palindromes.add(candidate)
    return valid_palindromes