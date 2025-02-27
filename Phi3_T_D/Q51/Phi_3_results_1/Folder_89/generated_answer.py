from collections import defaultdict

def if_contains_anagrams(lst):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    count, considered_length = (0, 0)
    anagrams_dict = defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            considered_length += 1
            word_lower = word.lower()
            for anagrams in anagrams_dict:
                if is_anagram(word_lower, anagrams):
                    count += 1
                    break
            anagrams_dict[word_lower] += 1
    return count <= 73