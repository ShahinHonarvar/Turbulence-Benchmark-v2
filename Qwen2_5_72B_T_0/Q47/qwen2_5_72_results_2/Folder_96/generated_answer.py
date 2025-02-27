def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    valid_palindromes = set()
    for start in range(100, 201):
        for end in range(start + 50, min(301, start + 101)):
            candidate = s[start:end]
            if candidate.isalpha() and is_palindrome(candidate):
                valid_palindromes.add(candidate)
    return valid_palindromes