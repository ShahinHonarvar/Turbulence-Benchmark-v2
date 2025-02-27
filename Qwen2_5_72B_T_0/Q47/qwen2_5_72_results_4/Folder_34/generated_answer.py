def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    valid_palindromes = set()
    s = s[200:301]
    for i in range(len(s)):
        for j in range(i + 10, i + 51):
            if j <= len(s):
                candidate = s[i:j]
                if candidate.isalpha() and is_palindrome(candidate):
                    valid_palindromes.add(candidate.lower())
    return valid_palindromes