def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    substr = s[16:61]
    palindromes = set()
    for i in range(len(substr)):
        for j in range(i + 16, i + 40):
            if j <= len(substr):
                candidate = substr[i:j]
                if candidate.isalpha() and is_palindrome(candidate):
                    palindromes.add(candidate.lower())
    return palindromes