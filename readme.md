# 莉沫酱存储！

做实验的时候经常要存一些数据，用手写`with open`很麻烦，就想着，啊那不如直接搞一个存硬盘的dict吧！


## 样例

```python
from rimo_storage import 超dict
d = 超dict('./savedata')
d['x'] = 114514
d['y'] = '好！'
```

然后下次运行程序的时候就还可以读`d`里面的内容了。

嗯，就是这么简单！


## 接口

- `rimo_storage.超dict(path, compress=None, serialize='json')`

基本上就相当于普通的`Dict[str, Any]`。

其中`compress`和`serialize`的类型是`Union[str, Tuple[Callable, Callable], None]`，它的行为是这样——
- `compress`可以选择`zlib`或者`lzma`，`serialize`可以选择`json`和`pickle`。
- 如果传`Tuple[Callable, Callable]`，则第一个函数会在写入的时候用，第二个函数会在读取的时候用。
- 如果是`None`，则什么都不做。

究竟能存什么东西依赖`serialize`，如果是`json`就只能存可json化的东西，如果是`pickle`就只能存可以pickle的东西<sub>(我又在讲废话了)</sub>。

- `rimo_storage.cache.disk_cache(*, path=None, compress=None, serialize='json')`

一个装饰器，差不多就是标准库的`functools.cache`的存硬盘版本，参数的意思和上面一样。


## 安装

只要使用pip安装就行啦！

```sh
pip install rimo_storage
```
