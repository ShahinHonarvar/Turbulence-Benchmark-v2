def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()

    def is_valid_palindrome(pal):
        return 119 <= len(pal) <= 141 and pal.isalpha()
    specified_range = s[127:289]
    palindromes = set()
    for start in range(len(specified_range)):
        for end in range(start + 119, start + 142):
            if end > len(specified_range):
                break
            substring = specified_range[start:end]
            if is_palindrome(substring) and is_valid_palindrome(substring):
                palindromes.add(substring)
    return palindromes