from itertools import combinations_with_replacement
    from string import ascii_letters

def palindrome_of_length_n(s):
    if len(s) < 210:
        return set()

    def is_palindrome(sub):
        return sub == sub[::-1]
    palindromes = set()
    charset = ascii_letters
    for start_index in range(len(s) - 209):
        substrings = [''.join(chars) for chars in combinations_with_replacement(charset, start_index + 210) if is_palindrome(''.join(chars))]
        for substring in substrings:
            if substring in s.lower():
                palindromes.add(substring)
    return palindromes