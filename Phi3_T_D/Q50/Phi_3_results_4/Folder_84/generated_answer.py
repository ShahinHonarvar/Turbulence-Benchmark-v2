def if_contains_anagrams(str_list):
    sorted_words = [''.join(sorted(word.lower())) for word in str_list if len(word) >= 3]
    count_anagrams = {}
    for word in sorted_words:
        count_anagrams[word] = count_anagrams.get(word, 0) + 1
    return sum((value * (value - 1) // 2 for value in count_anagrams.values())) >= 108