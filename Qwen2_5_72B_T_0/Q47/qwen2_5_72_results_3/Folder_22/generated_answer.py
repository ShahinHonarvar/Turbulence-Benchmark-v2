def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    valid_palindromes = set()
    for i in range(100, 201):
        for j in range(i + 5, min(202, i + 11)):
            substring = s[i:j]
            if substring.isalpha() and is_palindrome(substring):
                valid_palindromes.add(substring.lower())
    return valid_palindromes