def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    target_substring = s[1:9]
    palindromes = set()
    for length in range(3, 5):
        for start in range(len(target_substring) - length + 1):
            substring = target_substring[start:start + length]
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes