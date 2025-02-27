def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    valid_palindromes = set()
    s = s[11:84]
    for i in range(len(s)):
        for j in range(i + 37, min(i + 61, len(s) + 1)):
            if s[i:j].isalpha() and is_palindrome(s[i:j]):
                valid_palindromes.add(s[i:j])
    return valid_palindromes