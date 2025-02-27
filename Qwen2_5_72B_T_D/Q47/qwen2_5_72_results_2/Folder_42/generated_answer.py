def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    substr = s[43:96]
    palindromes = set()
    for i in range(len(substr)):
        for j in range(i + 18, i + 48):
            if j <= len(substr):
                candidate = substr[i:j]
                if candidate.isalpha() and is_palindrome(candidate):
                    palindromes.add(candidate)
    return palindromes