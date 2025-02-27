def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    valid_palindromes = set()
    for i in range(16, 77):
        for j in range(i + 43, min(78, i + 48)):
            if j > 77:
                break
            candidate = s[i:j]
            if candidate.isalpha() and is_palindrome(candidate):
                valid_palindromes.add(candidate.lower())
    return valid_palindromes