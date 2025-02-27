def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    substr = s[15:90]
    palindromes = set()
    for i in range(len(substr)):
        for j in range(i + 40, i + 73):
            if j <= len(substr):
                candidate = substr[i:j]
                if candidate.isalpha() and is_palindrome(candidate):
                    palindromes.add(candidate)
    return palindromes