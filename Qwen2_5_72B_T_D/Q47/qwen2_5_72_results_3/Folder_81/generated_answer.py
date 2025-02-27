def palindromes_of_specific_lengths(text):

    def is_palindrome(s):
        return s == s[::-1]
    text = text[12:123].lower()
    palindromes = set()
    for start in range(len(text)):
        for end in range(start + 12, min(len(text), start + 221)):
            candidate = text[start:end]
            if candidate.isalpha() and is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes