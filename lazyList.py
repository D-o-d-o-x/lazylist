from math import inf

class LazyList(list):
    def __init__(self, iterable):
        self._iter = iterable
        self._length = inf
        self._n = 0

    def __setitem__(self, index, item):
        self._requireLen(index)
        super().__setitem__(index, item)

    def __len__(self):
        return self._length

    def __repr__(self):
        if super().__len__() == 0:
            return '[...]'
        l = []
        for i in range(super().__len__()):
            l.append(str(self[i]))
        if self._length != inf:
            return '[' + ', '.join(l) + ']'
        else:
            return '[' + ', '.join(l) + ', ...]'

    def __str__(self):
        return repr(self)

    def _requireLen(self, length):
       if length==-1:
            num = inf
       else:
            num = length - super().__len__() + 1
       if num > 0:
           i = 0
           while i < num:
               try:
                   super().append(self._iter.__next__())
               except StopIteration as e:
                   self._length = super().__len__()
                   if length!=-1:
                       raise e
                   return
               i+=1

    def __iter__(self):
        self._n = 0
        return self

    def __next__(self):
        ret = self[self._n]
        self._n += 1
        return ret

    def peak(self, offset=0):
        return self[self._n - 1 + offset]

    def curIndex(self):
        return self._n - 1

    def nextIndex(self):
        return self._n

    def __getitem__(self, index):
        self._requireLen(index)
        return super().__getitem__(index)

    def insert(self, index, item):
        self._requireLen(index-1)
        super().insert(index, item)

    def append(self, item):
        self._requireLen(-1)
        super().append(item)

    def extend(self, other):
        # TODO: Don't force expand second?
        self._requireLen(-1)
        super().extend(other)
