from collections import Counter

def if_contains_anagrams(lst):
    lst = [word.lower() for word in lst if len(word) >= 3]
    anagram_counter = 0
    word_count = Counter((''.join(sorted(word)) for word in lst))
    for count in word_count.values():
        anagram_counter += count * (count - 1) // 2
    return anagram_counter <= 91