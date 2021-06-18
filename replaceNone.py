def replaceNone(ls):
    prev = None
    if ls is None:
        return None
    if not ls:
        return []
    for i in range(len(ls)):
        if ls[i] is not None:
            prev = ls[i]
        else:
            ls[i] = prev
    return ls

assert replaceNone(None) == None
assert replaceNone([]) == []
assert replaceNone([None, 8, None]) == [None, 8, 8]
assert replaceNone([1, None, 2]) == [1, 1, 2]
assert replaceNone([5, None, None]) == [5, 5, 5]
assert replaceNone([1, None, 2, 3, None, None, 5, None]) == [1, 1, 2, 3, 3, 3, 5, 5]
print("passed")
