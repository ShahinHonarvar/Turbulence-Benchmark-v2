def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    valid_palindromes = set()
    for length in [20, 21]:
        for start in range(12, 57 - length + 1):
            sub = s[start:start + length]
            if sub.isalpha() and is_palindrome(sub):
                valid_palindromes.add(sub)
    return valid_palindromes