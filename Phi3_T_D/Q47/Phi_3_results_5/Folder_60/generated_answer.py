def palindromes_of_specific_lengths(text):

    def is_valid_char(ch):
        return ch.isalpha() and len(ch) == 1

    def is_palindrome(s):
        return s == s[::-1]

    def find_palindromes(s, min_length, max_length):
        palindromes = set()
        for length in range(min_length, max_length + 1):
            for start in range(len(s) - length + 1):
                substring = s[start:start + length]
                if is_palindrome(substring):
                    palindromes.add(substring.lower())
        return palindromes
    target_substring = text[23:83]
    return find_palindromes(target_substring, 32, 34)