def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    substr = s[16:78]
    palindromes = set()
    for length in range(43, 48):
        for start in range(len(substr) - length + 1):
            sub = substr[start:start + length]
            if is_palindrome(sub) and sub.isalpha():
                palindromes.add(sub.lower())
    return palindromes