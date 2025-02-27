def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    substring = s[103:277]
    valid_palindromes = set()
    for start in range(len(substring)):
        for end in range(start + 99, start + 170):
            if end < len(substring):
                candidate = substring[start:end + 1]
                if candidate.isalpha() and is_palindrome(candidate):
                    valid_palindromes.add(candidate.lower())
    return valid_palindromes