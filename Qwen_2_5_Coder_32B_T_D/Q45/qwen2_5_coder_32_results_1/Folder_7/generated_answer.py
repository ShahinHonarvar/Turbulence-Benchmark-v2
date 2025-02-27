from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[1:10])).lower()
    count = Counter(letters)
    used = set()
    res = set()

    def backtrack(path):
        if len(path) == 7:
            pal = ''.join(path)
            if pal == pal[::-1]:
                res.add(pal)
            return
        for char in count:
            if count[char] > 0:
                path.append(char)
                count[char] -= 1
                backtrack(path)
                path.pop()
                count[char] += 1
    backtrack([])
    return res