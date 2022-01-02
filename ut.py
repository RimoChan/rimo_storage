import os
import shutil
import random
import string

import rimo_storage
print(rimo_storage.__file__)

from rimo_storage.cache import disk_cache


def 检查(x, y, q=False):
    if q:
        al = ['zlib']
    else:
        al = [*rimo_storage._压缩, None]
    for 类 in [rimo_storage.好dict, rimo_storage.超dict]: 
        for c in al:
            print(f'类: {类}, 压缩: {c}')
            if os.path.isdir(f'_ut_{c}'):
                shutil.rmtree(f'_ut_{c}')
            d = 类(f'_ut_{c}', compress=c)
            assert len(d) == 0
            真d = {}
            for _ in range(x):
                k = str(random.randint(0, y))
                if 类 is rimo_storage.好dict: 
                    v = (''.join([random.choice(string.ascii_lowercase) for i in range(random.randint(1, 1000))])).encode('utf8')
                else:
                    if random.random() < 0.5:
                        v = ''.join([random.choice(string.ascii_lowercase) for i in range(random.randint(1, 1000))])
                    else:
                        v = random.randint(0, 10000000)

                真d[k] = v
                d[k] = v
                assert 真d[k] == d[k]
            for k in d:
                assert 真d[k] == d[k]
            for k in 真d:
                assert 真d[k] == d[k]
            assert sorted([*真d.items()]) == sorted([*d.items()])

            d = 类(f'_ut_{c}', compress=c)
            assert len(d) == len([*d.items()])
            for k in d:
                assert 真d[k] == d[k]
            for k in 真d:
                assert 真d[k] == d[k]
            assert sorted([*真d.items()]) == sorted([*d.items()])

            shutil.rmtree(f'_ut_{c}')


print('=====检查好dict_1=====')
检查(100, 5)

print('=====检查好dict_2=====')
检查(5, 5000)

print('=====检查好dict_3=====')
检查(1000, 1000, q=True)



print('=====检查cache=====')

for serialize in ['pickle', 'json']:
    print(f'serialize: {serialize}')
    if os.path.isdir(f'_rimocache_f_{serialize}'):
        shutil.rmtree(f'_rimocache_f_{serialize}')

    @disk_cache(serialize=serialize, compress='zlib')
    def f(a, b):
        f.count += 1
        return [f'好{a+b}', 1]
    f.count = 0

    def ff(a, b):
        return [f'好{a+b}', 1]

    for i in range(1000):
        x, y = random.randint(1, 30), random.randint(1, 30)
        assert ff(x, y) == f(x, y)
    assert f.count < 1000

    shutil.rmtree(f'_rimocache_f_{serialize}')