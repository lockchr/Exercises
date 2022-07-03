from hmac import digest
from this import d
from turtle import left


def build_root(self, iterable):
    collection = list(iterable)
    assert (len(collection) != 0)
    if len(collection) % 2 != 0:
        collection.append(collection[-1])
    collection = [self.__Node(self.digest(x)) for x in collection]
    return self.__build_root(collection)


def __build_root(self, collection):
    size = len(collection)
    if size == 1:
        return collection[0]
    if size % 2 == 0:
        collection.append(self.__Node(collection[-1].value, left=collection[-1].left, right=collection[-1].right))
    next_level = []
    for i in range(0, size - 1, 2):
        digest = self.digest(collection[i].value + collection[i + 1].value)
        node = self.__Node(digest, left=collection[i], right=collection[i + 1])
        next_level.append(node)
    return self.__build_root(next_level)
