from collections import defaultdict

def if_contains_anagrams(word_list):
    count = 0
    length_filtered_words = [''.join(sorted(word.lower())) for word in word_list if len(word) >= 3]
    sorted_word_dict = defaultdict(list)
    for word in length_filtered_words:
        sorted_word_dict[word].append(word)
    for anagrams in sorted_word_dict.values():
        if len(anagrams) > 1:
            count += len(anagrams) * (len(anagrams) - 1) // 2
    return count >= 219