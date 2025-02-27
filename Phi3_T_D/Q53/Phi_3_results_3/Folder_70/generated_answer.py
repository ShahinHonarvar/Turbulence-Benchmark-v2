def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s.lower()
    letter_index = {letter: [] for letter in set(s) if letter.isalpha()}
    for index, letter in enumerate(s):
        if letter.isalpha():
            letter_index[letter].append(index)
    palindromes = set()
    for letter, indices in letter_index.items():
        for start in indices:
            for end in indices[indices.index(start):]:
                if end - start + 1 >= 11:
                    substring = s[start:end + 1]
                    if is_palindrome(substring):
                        palindromes.add(substring)
    return palindromes