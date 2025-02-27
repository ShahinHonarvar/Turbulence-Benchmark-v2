def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    substr = s[11:98]
    palindromes = set()
    for i in range(len(substr)):
        for j in range(i + 29, i + 63):
            if j <= len(substr):
                sub = substr[i:j]
                if sub.isalpha() and is_palindrome(sub):
                    palindromes.add(sub)
    return palindromes