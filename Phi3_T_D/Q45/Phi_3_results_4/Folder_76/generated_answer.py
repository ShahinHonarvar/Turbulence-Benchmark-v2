from itertools import permutations

def palindromes_between_indices(s):
    sub_string = s[1:5].lower()
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    letters_in_range = set(sub_string) & alphabet
    if len(letters_in_range) < 4:
        return set()
    possible_palindromes = set()
    for l in range(4, len(letters_in_range) + 1):
        for perm in permutations(letters_in_range, l):
            prefix = ''.join(perm[:l // 2])
            if l % 2 == 0:
                possible_palindromes.add(prefix + prefix[::-1])
            else:
                for m in range(len(prefix)):
                    possible_palindromes.add(prefix[:m] + 'a' + prefix[m:] + prefix[:m][::-1])
    return possible_palindromes