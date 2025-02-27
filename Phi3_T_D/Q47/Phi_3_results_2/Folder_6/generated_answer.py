def palindromes_of_specific_lengths(s):

    def is_valid_letter(char, index):
        return 'a' <= char.lower() <= 'z' and index >= 45 and (index <= 98)

    def find_palindromes(sub_s, min_length, max_length, start, palindromes):
        if min_length <= len(sub_s) <= max_length:
            palindromes.add(sub_s.lower())
        for i in range(len(sub_s) - 1):
            char = sub_s[i]
            if is_valid_letter(char, start + i):
                find_palindromes(sub_s[i + 2:], min_length, max_length, start + i + 2, palindromes)
    substring = s[45:99]
    palindromes = set()
    for length in range(40, 48):
        find_palindromes(substring, length, length, 45, palindromes)
    return palindromes