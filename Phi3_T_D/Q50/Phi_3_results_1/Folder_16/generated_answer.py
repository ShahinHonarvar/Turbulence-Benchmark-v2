from collections import defaultdict

def if_contains_anagrams(word_list):
    sorted_word_list = [''.join(sorted(word.lower())) for word in word_list if len(word) >= 3]
    anagram_count = defaultdict(int)
    for word in sorted_word_list:
        anagram_count[word] += 1
    return sum((count * (count - 1) // 2 for count in anagram_count.values())) >= 155