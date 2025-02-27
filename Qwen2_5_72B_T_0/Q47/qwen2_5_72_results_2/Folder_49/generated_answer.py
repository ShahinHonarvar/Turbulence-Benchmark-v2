def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    valid_palindromes = set()
    for start in range(10, 101):
        for end in range(start + 10, min(102, start + 51)):
            substring = s[start:end]
            if substring.isalpha() and is_palindrome(substring):
                valid_palindromes.add(substring.lower())
    return valid_palindromes