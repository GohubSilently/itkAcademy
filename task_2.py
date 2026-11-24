from collections.abc import Iterable


class CycleList:
    def __init__(self, items: Iterable):
        self._items = list(items)
        if not self._items:
            raise ValueError('Пустой список невозможен')

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        return self._items[index % len(self._items)]

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return f'CycleList({self._items})'


if __name__ == '__main__':
    cl = CycleList([1, 2, 3])
    assert len(cl) == 3
    assert cl[0] == 1
    assert cl[3] == 1
    assert cl[5] == 3
    assert cl[-1] == 3
    assert list(cl) == [1, 2, 3]
    assert str(cl) == 'CycleList([1, 2, 3])'
