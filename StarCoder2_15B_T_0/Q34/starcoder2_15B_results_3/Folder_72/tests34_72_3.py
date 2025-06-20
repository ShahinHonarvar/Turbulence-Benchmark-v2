from Q34.starcoder2_15B_results_3.Folder_72.generated_answer import find_original_set


def test_one_element_similar_sets():
    l = []
    for i in range(87):
        l.append({1})
    assert find_original_set(*l) == {1}


def test_distinct_one_element_sets():
    l = []
    for i in range(87):
        l.append({i})
    assert find_original_set(*l) == set(range(87))


def test_similar_sets():
    l = []
    for i in range(87):
        l.append(set(range(10)))
    assert find_original_set(*l) == set(range(10))


def test_distinct_sets():
    l = []
    for i in range(0, 87*87, 87):
        l.append(set(range(i, i + 87)))
    assert find_original_set(*l) == set(range(87*87))


def test_several_subsets():
    l = []
    for i in range(87):
        l.append(set(range(i+1)))
    assert find_original_set(*l) == set(range(87))
