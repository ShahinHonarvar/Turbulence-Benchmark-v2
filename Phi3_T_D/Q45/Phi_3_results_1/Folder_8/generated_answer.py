def palindromes_between_indices(s):
    importance = set(s[1:6].lower())
    length_required = 5
    required_set = {''.join(p) for p in itertools.permutations(importance, length_required) if p == tuple(reversed(p))}
    return required_set