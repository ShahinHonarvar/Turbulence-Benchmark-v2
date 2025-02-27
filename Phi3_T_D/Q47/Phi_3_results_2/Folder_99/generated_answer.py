def find_palindromes(s, start=0, end=None):
    if end is None:
        end = len(s)
    return [s[i:j] for i in range(start, end) for j in range(i + 1, end + 1) if s[i:j] == s[i:j][::-1]]

def palindromes_of_specific_lengths(text):
    English_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    possible_palindromes = set()
    for length in range(119, 142):
        for substring in find_palindromes(text[127:289], 0, length):
            if set(substring).issubset(English_letters) and substring == substring.lower() and (substring == substring[::-1]):
                possible_palindromes.add(substring)
    return possible_palindromes