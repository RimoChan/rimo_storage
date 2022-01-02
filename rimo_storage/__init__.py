import os
import sys
import zlib
import lzma
import json
import pickle
from pathlib import Path
from typing import Mapping, Callable, Tuple, Union, Any


_压缩 = {
    'zlib': (
        zlib.compress,
        zlib.decompress,
    ),
    'lzma': (
        lzma.compress,
        lzma.decompress,
    ),
}


_序列化 = {
    'pickle': (
        pickle.dumps,
        pickle.loads,
    ),
    'json': (
        lambda x: json.dumps(x, sort_keys=True, ensure_ascii=False, separators=(',', ':')).encode('utf8'),
        json.loads,
    ),
}


F = Union[str, Tuple[Callable, Callable], None]


def _cf(s: F, d: dict) -> Tuple[Callable, Callable]:
    if s is None:
        return lambda x: x, lambda x: x
    elif isinstance(s, str):
        return d[s]
    else:
        return s


class 好dict(Mapping[str, bytes]):
    def __init__(self, path, compress: F = None):
        self.path = Path(path)
        if self.path.is_file():
            raise Exception('你不对劲')
        self.path.mkdir(parents=True, exist_ok=True)
        self.dirs = set()
        self.compress, self.decompress = _cf(compress, _压缩)

    def __contains__(self, k: str):
        return (self.path/k[:2]/(k[2:]+'_')).is_file()

    def __getitem__(self, k: str):
        with open(self.path/k[:2]/(k[2:]+'_'), 'rb') as f:
            t = f.read()
        return self.decompress(t)

    def __setitem__(self, k: str, v):
        if k[:2] not in self.dirs:
            (self.path/k[:2]).mkdir(exist_ok=True)
            self.dirs.add(k[:2])
        t = self.compress(v)
        with open(self.path/k[:2]/(k[2:]+'_'), 'wb') as f:
            f.write(t)

    def __len__(self):
        return sum([len(os.listdir(self.path/a)) for a in os.listdir(self.path)])

    def __iter__(self):
        for a in os.listdir(self.path):
            for b in os.listdir(self.path/a):
                yield a+b[:-1]


# 它继承了Mapping[str, bytes]，但是其实它是Mapping[str, Any]，但是我也不知道怎么办
class 超dict(好dict):
    def __init__(self, path, compress: F = None, serialize: F = 'json'):
        super().__init__(path, compress)
        self.serialize, self.deserialize = _cf(serialize, _序列化)

    def __getitem__(self, k: str):
        return self.deserialize(super().__getitem__(k))

    def __setitem__(self, k: str, v: Any):
        return super().__setitem__(k, self.serialize(v))
