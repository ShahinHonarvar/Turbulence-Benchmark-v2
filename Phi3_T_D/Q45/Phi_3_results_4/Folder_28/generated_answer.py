from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:6].lower()
    middle_char = [char for char in substring if substring.count(char) % 2 != 0]
    if middle_char and len(middle_char) > 1:
        return set()
    middle_char = '' if not middle_char or len(middle_char) == 1 else middle_char[0]
    possible_chars = ''.join([char if char not in middle_char else char * 2 for char in substring])
    permutations_list = [''.join(p) for p in permutations(possible_chars)]
    palindromes_set = set()
    for p in permutations_list:
        for length in range(4, len(p) + 1, 2):
            for i in range(len(p) - length + 1):
                if p[i:i + length] == p[i:i + length][::-1]:
                    param_order = p[i:i + int(length / 2)] + middle_char + p[i + int(length / 2):i + length][::-1]
                    palindromes_set.add(param_order)
    return palindromes_set