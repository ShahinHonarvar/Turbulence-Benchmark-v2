def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    valid_palindromes = set()
    s = s[10:71]
    for i in range(len(s)):
        for j in range(i + 24, min(i + 53, len(s) + 1)):
            if s[i:j].isalpha() and is_palindrome(s[i:j]):
                valid_palindromes.add(s[i:j].lower())
    return valid_palindromes