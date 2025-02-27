from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for word in strings:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagram_dict[sorted_word].append(word)
    count = 0
    for words_list in anagram_dict.values():
        for i in range(len(words_list)):
            for j in range(i + 1, len(words_list)):
                count += 1
                if count >= 14:
                    return True
    return False