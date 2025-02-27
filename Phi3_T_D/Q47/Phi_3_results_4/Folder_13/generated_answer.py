def palindromes_of_specific_lengths(s):
    endpoint1 = 13
    endpoint2 = 95

    def is_english_letter(char):
        return 'a' <= char <= 'z' or 'A' <= char <= 'Z'

    def is_palindrome(pal):
        return pal == pal[::-1]
    collected_palindromes = set()
    length_range = range(57, 61)
    for length in length_range:
        for i in range(endpoint1, endpoint2 - length + 2):
            substring = s[i:i + length].lower()
            if all((is_english_letter(char) for char in substring)) and is_palindrome(substring):
                collected_palindromes.add(substring)
    return collected_palindromes