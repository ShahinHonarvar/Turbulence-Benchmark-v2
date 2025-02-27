def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    valid_range = s[11:98]
    palindromes = set()
    for start in range(len(valid_range)):
        for end in range(start + 29, start + 63):
            if end <= len(valid_range):
                sub = valid_range[start:end]
                if sub.isalpha() and is_palindrome(sub):
                    palindromes.add(sub)
    return palindromes