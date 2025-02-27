import collections

def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return len(str1) >= 3 and sorted(str1.lower()) == sorted(str2.lower())
    anagrams_count = 0
    checked_pairs = set()
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if (i, j) not in checked_pairs and is_anagram(strings[i], strings[j]):
                anagrams_count += 1
                checked_pairs.add((i, j))
                checked_pairs.add((j, i))
    return anagrams_count >= 17