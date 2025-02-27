def palindromes_of_specific_lengths(s):

    def is_valid_letter(char):
        return 'a' <= char <= 'z' or 'A' <= char <= 'Z'

    def find_palindromes(start, length, palindromes):
        for i in range(start, len(sub_str) - length + 1):
            substr = sub_str[i:i + length]
            if substr.lower() == substr[::-1].lower():
                if all((is_valid_letter(c) for c in substr)):
                    palindromes.add(substr.lower())
    sub_str = s[15:87]
    palindromes = set()
    for length in range(51, 61):
        find_palindromes(0, length, palindromes)
    return palindromes