def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    valid_palindromes = set()
    for start in range(15, 90):
        for end in range(start + 39, min(90, start + 72) + 1):
            substr = s[start:end]
            if substr.isalpha() and is_palindrome(substr):
                valid_palindromes.add(substr)
    return valid_palindromes