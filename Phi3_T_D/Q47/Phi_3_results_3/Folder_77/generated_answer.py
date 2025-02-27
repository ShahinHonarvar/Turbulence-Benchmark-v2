def palindromes_of_specific_lengths(text):

    def is_palindrome(s):
        return s == s[::-1]

    def extract_palindromes(substr, min_len, max_len):
        palindromes = set()
        for i in range(len(substr)):
            for length in range(min_len, max_len + 1):
                if i + length > len(substr):
                    continue
                candidate = substr[i:i + length]
                if candidate.isalpha() and is_palindrome(candidate.lower()):
                    palindromes.add(candidate.lower())
        return palindromes
    substring = text[103:277]
    return extract_palindromes(substring, 100, 169)