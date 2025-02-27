def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    if len(s) < 97:
        return set()
    valid_range = s[11:97]
    palindromes = set()
    for start in range(len(valid_range)):
        for end in range(start + 44, start + 53):
            if end < len(valid_range):
                candidate = valid_range[start:end + 1]
                if candidate.isalpha() and is_palindrome(candidate):
                    palindromes.add(candidate)
    return palindromes