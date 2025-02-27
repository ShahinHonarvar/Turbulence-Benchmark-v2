def palindromes_between_indices(s):
    substring = s[1:3].lower()
    if len(set(substring)) < 2:
        return set()
    palindromes = set()
    for i in range(97, 123):
        char = chr(i)
        if substring.count(char) > 1:
            for j in range(97, 123):
                middle_char = chr(j)
                if substring.count(middle_char) > 0:
                    palindrome = f'{char}{middle_char}{char}'
                    palindromes.add(palindrome)
    return palindromes