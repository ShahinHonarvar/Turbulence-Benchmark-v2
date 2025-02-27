from itertools import permutations

def palindromes_between_indices(text):
    start, end = (2, 7)
    substr = text[start:end + 1].lower()
    char_list = [char for char in substr if char.isalpha()]
    possible_palindromes = set()
    length = end - start + 1
    for i in range(length, 2, -1):
        for perm in permutations(char_list, i):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                possible_palindromes.add(candidate)
    return possible_palindromes