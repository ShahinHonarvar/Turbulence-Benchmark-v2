def palindromes_of_specific_lengths(s):

    def is_letter(c):
        return 'a' <= c <= 'z'
    substring = s[10:76]
    palindromes = set()
    for length in range(10, 21):
        for i in range(len(substring) - length + 1):
            substring_part = substring[i:i + length]
            if all((is_letter(c) for c in substring_part)):
                if substring_part.lower() == substring_part[::-1].lower():
                    palindromes.add(substring_part)
    return palindromes