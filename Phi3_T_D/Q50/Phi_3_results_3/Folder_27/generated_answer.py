def if_contains_anagrams(words):
    words = [word.lower() for word in words]
    sorted_words = [''.join(sorted(word)) for word in words]
    count_dict = {}
    for word in sorted_words:
        count_dict[word] = count_dict.get(word, 0) + 1
    count = 0
    for value in count_dict.values():
        count += value * (value - 1) // 2
    return count >= 86