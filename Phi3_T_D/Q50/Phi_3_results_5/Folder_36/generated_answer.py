def if_contains_anagrams(word_list):
    filtered_list = [word.lower() for word in word_list if len(word) >= 3]
    sorted_words = [''.join(sorted(word)) for word in filtered_list]
    count = {}
    for word in sorted_words:
        count[word] = count.get(word, 0) + 1
    return sum((v for v in count.values() if v >= 2)) >= 312