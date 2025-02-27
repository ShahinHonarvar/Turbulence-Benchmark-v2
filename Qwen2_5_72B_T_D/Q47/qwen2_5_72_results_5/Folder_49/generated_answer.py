def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    valid_palindromes = set()
    for start in range(10, 101):
        for end in range(start + 9, 101):
            substr = s[start:end + 1]
            if 10 <= len(substr) <= 50 and substr.isalpha() and is_palindrome(substr):
                valid_palindromes.add(substr.lower())
    return valid_palindromes