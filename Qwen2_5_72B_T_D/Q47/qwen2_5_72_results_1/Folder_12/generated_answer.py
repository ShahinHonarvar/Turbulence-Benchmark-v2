def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    substr = s[62:89]
    palindromes = set()
    for i in range(len(substr)):
        for j in range(i + 18, i + 22):
            if j <= len(substr):
                candidate = substr[i:j]
                if candidate.isalpha() and is_palindrome(candidate.lower()):
                    palindromes.add(candidate)
    return palindromes