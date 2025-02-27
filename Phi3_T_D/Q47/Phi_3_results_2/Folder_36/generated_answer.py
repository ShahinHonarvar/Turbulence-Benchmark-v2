def palindromes_of_specific_lengths(s):

    def is_english_letter(c):
        return 'a' <= c <= 'z' or 'A' <= c <= 'Z'

    def is_palindrome(sub):
        return sub == sub[::-1] and all((is_english_letter(c) for c in sub.lower()))
    valid_palindromes = set()
    start_index = min(124, len(s))
    end_index = min(283, len(s))
    for length in range(115, 135):
        for i in range(start_index, end_index - length + 1):
            if is_palindrome(s[i:i + length]):
                valid_palindromes.add(s[i:i + length].lower())
    return valid_palindromes