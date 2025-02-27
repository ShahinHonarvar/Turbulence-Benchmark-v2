def if_contains_anagrams(string_list):

    def normalize(s):
        return sorted(s.lower())
    count = 0
    checked = set()
    for i in range(len(string_list)):
        for j in range(i + 1, len(string_list)):
            if len(string_list[i]) >= 3 and len(string_list[j]) >= 3:
                if normalize(string_list[i]) == normalize(string_list[j]) and (string_list[i], string_list[j]) not in checked:
                    count += 1
                    checked.add((string_list[i], string_list[j]))
                    checked.add((string_list[j], string_list[i]))
            if count > 5:
                return False
    return True