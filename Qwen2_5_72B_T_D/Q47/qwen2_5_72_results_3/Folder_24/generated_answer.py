def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    valid_palindromes = set()
    sub_str = s[12:93]
    for start in range(len(sub_str)):
        for end in range(start + 41, start + 78):
            if end < len(sub_str):
                candidate = sub_str[start:end + 1]
                if candidate.isalpha() and is_palindrome(candidate):
                    valid_palindromes.add(candidate)
    return valid_palindromes