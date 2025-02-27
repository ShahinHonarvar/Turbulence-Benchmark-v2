def palindromes_of_specific_lengths(text):

    def is_english_letter(char):
        return 'a' <= char <= 'z' or 'A' <= char <= 'Z'

    def find_palindromes(s, k):
        palindromes = set()
        for i in range(len(s) - k + 1):
            substr = s[i:i + k]
            if substr == substr[::-1] and all((is_english_letter(c) for c in substr)):
                palindromes.add(substr)
        return palindromes
    start, end = (2, 8)
    length = (3, 4)
    sliced_text = text[start:end + 1]
    result_set = set()
    for pal_len in length:
        result_set |= find_palindromes(sliced_text, pal_len)
    return result_set