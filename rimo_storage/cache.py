import json
import signal
import pickle
import hashlib

from typing import Dict

from . import 好dict, 超dict, _cf, _序列化


_ext = {
    'pickle': 'pkl',
    'json': 'json',
}


def disk_cache(path=None, compress=None, serialize='json'):
    ext = _ext.get(serialize, '_')
    dump = _cf(serialize, _序列化)[0]
    def q(func):
        nonlocal path
        name = func.__name__
        if path is None:
            path = f'./_rimocache_{name}_{serialize}'
        map = 超dict(path, serialize=serialize, compress=compress)
        def 假func(*li, **d):
            i = [name, li, d]
            md5 = hashlib.md5(dump(i)).hexdigest()
            名字 = f'{md5}.{ext}'
            if 名字 in map:
                i, o = map[名字]
                return o
            else:
                o = func(*li, **d)
                s = [i, o]
                map[名字] = s
                return o
        return 假func
    return q
