def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring == substring[::-1]

    def extract_palindromes(string, min_length, max_length):
        palindromes = set()
        s = s[17:96]
        for length in range(min_length, max_length + 1):
            for start in range(len(s) - length + 1):
                substring = s[start:start + length]
                if all((c.isalpha() for c in substring)):
                    cleaned_substring = ''.join(filter(str.isalpha, substring)).lower()
                    if cleaned_substring == cleaned_substring[::-1]:
                        palindromes.add(cleaned_substring)
        return palindromes
    return extract_palindromes(s, 13, 49)