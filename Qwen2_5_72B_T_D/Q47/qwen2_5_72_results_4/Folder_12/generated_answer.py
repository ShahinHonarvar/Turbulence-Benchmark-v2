def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    substring = s[62:89]
    palindromes_set = set()
    for length in range(18, 22):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if is_palindrome(candidate) and candidate.isalpha():
                palindromes_set.add(candidate.lower())
    return palindromes_set