def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    palindromes = set()
    lower, upper = (1, 299)
    min_len, max_len = (3, 10)
    for start in range(lower, upper + 1):
        for end in range(start + min_len - 1, min(start + max_len, upper + 1)):
            substring = s[start:end + 1]
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring.lower())
    return palindromes