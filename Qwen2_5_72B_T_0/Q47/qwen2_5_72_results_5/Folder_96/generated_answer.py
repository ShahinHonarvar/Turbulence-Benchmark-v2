def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    valid_palindromes = set()
    for start in range(100, 201):
        for end in range(start + 50, min(301, start + 101)):
            substring = s[start:end]
            if substring.isalpha() and is_palindrome(substring):
                valid_palindromes.add(substring)
    return valid_palindromes