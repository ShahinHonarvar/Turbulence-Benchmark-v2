def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    valid_palindromes = set()
    substring = s[20:75]
    for i in range(len(substring)):
        for j in range(i + 36, i + 43):
            if j <= len(substring):
                candidate = substring[i:j]
                if candidate.isalpha() and is_palindrome(candidate):
                    valid_palindromes.add(candidate.lower())
    return valid_palindromes