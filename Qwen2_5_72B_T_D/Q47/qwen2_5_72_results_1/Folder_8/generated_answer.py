def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    valid_palindromes = set()
    for length in [50, 51]:
        for start in range(17, 73 - length + 1):
            substring = s[start:start + length]
            if substring.isalpha() and is_palindrome(substring):
                valid_palindromes.add(substring)
    return valid_palindromes