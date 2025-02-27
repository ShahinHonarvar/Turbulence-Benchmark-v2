def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    valid_range = s[26:91]
    palindromes = set()
    for start in range(len(valid_range)):
        for end in range(start + 1, len(valid_range) + 1):
            if 27 <= end - start <= 58 and valid_range[start:end].isalpha() and is_palindrome(valid_range[start:end]):
                palindromes.add(valid_range[start:end])
    return palindromes