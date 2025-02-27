from collections import defaultdict

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        s1 = s1.lower()
        s2 = s2.lower()
        return sorted(s1) == sorted(s2)
    filtered = [s for s in lst if len(s) >= 3]
    anagram_count = 0
    anagram_map = defaultdict(list)
    for i in range(len(filtered)):
        for j in range(i + 1, len(filtered)):
            if is_anagram(filtered[i], filtered[j]):
                anagram_map[filtered[i]].append(filtered[j])
    for value in anagram_map.values():
        anagram_count += len(value) // 2
    return anagram_count >= 38