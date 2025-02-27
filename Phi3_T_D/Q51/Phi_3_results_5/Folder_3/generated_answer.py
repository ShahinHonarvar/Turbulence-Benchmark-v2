from collections import defaultdict

def if_contains_anagrams(words):

    def are_anagrams(a, b):
        return sorted(a.lower()) == sorted(b.lower())
    length = defaultdict(list)
    count = 0
    for word in words:
        if len(word) >= 3:
            sorted_word = sorted(word.lower())
            length[tuple(sorted_word)].append(word)
    for lst in length.values():
        if len(lst) > 1:
            count += len(lst) * (len(lst) - 1) // 2
    return count <= 66