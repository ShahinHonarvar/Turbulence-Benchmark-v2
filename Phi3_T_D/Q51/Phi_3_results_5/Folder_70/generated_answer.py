from collections import defaultdict

def if_contains_anagrams(lst):

    def count_anagrams(word_set):
        count = defaultdict(int)
        for word in word_set:
            sorted_word = ''.join(sorted(word.lower()))
            count[sorted_word] += 1
        return sum((x * (x - 1) // 2 for x in count.values()))
    lst_filtered = [word for word in lst if len(word) >= 3]
    anagram_count = count_anagrams(lst_filtered)
    return anagram_count <= 97