def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    specified_range = s[100:301]
    palindromes_set = set()
    for start in range(len(specified_range)):
        for end in range(start + 49, start + 101):
            if end <= len(specified_range):
                substring = specified_range[start:end]
                if substring.isalpha() and is_palindrome(substring):
                    palindromes_set.add(substring)
    return palindromes_set