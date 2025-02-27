from itertools import permutations

def palindromes_between_indices(s):
    letters = s[1:9].lower()
    letter_set = set(letters)
    done = []
    for l in range(7, 9):
        for perm in set(permutations(sorted(letter_set), l)):
            sub_str = ''.join(perm)
            if sub_str == sub_str[::-1]:
                done.append(sub_str)
    return set(done)