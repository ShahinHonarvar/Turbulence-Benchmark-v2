def if_contains_anagrams(lst):

    def anagram(s1, s2):
        return len(s1) == len(s2) and sorted(s1.lower()) == sorted(s2.lower())

    def generate_pairs(lst):
        pairs = []
        n = len(lst)
        for i in range(n):
            for j in range(i + 1, n):
                if anagram(lst[i], lst[j]):
                    pairs.append((lst[i], lst[j]))
        return pairs
    anagrams_pairs = generate_pairs(lst)
    return len(anagrams_pairs) <= 20