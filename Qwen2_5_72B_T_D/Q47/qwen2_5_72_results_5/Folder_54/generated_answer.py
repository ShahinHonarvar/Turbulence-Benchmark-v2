def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    substr = s[27:78]
    palindromes = set()
    for length in [18, 19]:
        for i in range(len(substr) - length + 1):
            sub = substr[i:i + length]
            if sub.isalpha() and is_palindrome(sub):
                palindromes.add(sub)
    return palindromes