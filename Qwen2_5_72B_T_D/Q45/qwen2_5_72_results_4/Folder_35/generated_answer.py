from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:5]
    char_list = [char.lower() for char in substring if char.isalpha()]
    found_palindromes = set()
    for perm in permutations(char_list, len(char_list)):
        word = ''.join(perm)
        if word == word[::-1]:
            for length in range(4, len(word) + 1):
                if word[:length] == word[:length][::-1]:
                    found_palindromes.add(word[:length])
    return found_palindromes