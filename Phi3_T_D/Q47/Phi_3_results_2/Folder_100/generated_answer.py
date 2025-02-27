from collections import defaultdict

def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s == s[::-1]

    def collect_palindromes(substr, length, palindromes):
        for i in range(len(substr) - length + 1):
            if is_palindrome(substr[i:i + length]):
                clean_palindrome = ''.join(filter(str.isalpha, substr[i:i + length])).lower()
                palindromes.add(clean_palindrome)
    start, end = (29, 96)
    palindromes = set()
    substr = s[start:end + 1]
    for length in range(12, 19):
        collect_palindromes(substr, length, palindromes)
    return palindromes