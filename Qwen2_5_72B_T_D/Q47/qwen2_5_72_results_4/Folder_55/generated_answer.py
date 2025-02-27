def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    valid_palindromes = set()
    for start in range(10, 76):
        for end in range(start, 76):
            substring = s[start:end + 1]
            if 10 <= len(substring) <= 20 and substring.isalpha() and is_palindrome(substring):
                valid_palindromes.add(substring.lower())
    return valid_palindromes