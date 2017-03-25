#coding=utf-8
'''
快捷键：ctrl+alt+space basic completion
'''
def f(param):
    '''
    :type param: list[str]
    :return: int
    '''
    param.append('test') #这样param就有自动补全了
    n = len(param)
    return n

def f2(x):# 使用stub
    '''
PyCharm supports Python stub files with the .pyi extension. These files allow you to specify the type hints using Python3
syntax for both Python 2 and 3.
The stub files are created as usual , but you must specify the extension .pyi explicitly.
PyCharm shows an asterisk in the left gutter for those Python files that have stubs:
    '''
    return x.upper()

#Type syntax in Python docstrings is not defined by any standard. Thus, PyCharm suggests the following notation:
# Syntax	                Description
# Foo	                    Class Foo visible in the current scope
# x.y.Bar	                Class Bar from x.y module
# Foo | Bar	                Foo or Bar
# (Foo, Bar)	            Tuple of Foo and Bar
# list[Foo]	                List of Foo elements
# dict[Foo, Bar]	        Dict from Foo to Bar
# T	                        Generic type (T-Z are reserved for generics)
# T <= Foo	                Generic type with upper bound Foo
# Foo[T]	                Foo parameterized with T
# (Foo, Bar) -> Baz	        Function of Foo and Bar that returns Baz
# list[dict[str, datetime]]	List of dicts from str to datetime (nested arguments)
class C():
    def deserialize(self):
        return 1
    def f(self):
        self.foo = self.deserialize()
        """:type : str"""
        #可以直接指定self.foo的类型
        self.foo.upper()

class Foo(object):
    """
    :type a: list[str]
    :type b: int | None
    """
    #或者在docstring中进行如上的指示
    def __init__(self):
        self.a = []
        self.b = None

def e(p):
    """
    @type p: str
    """
    return p.upper()


if __name__ == '__main__':
    print f(['1,2,3,4'])
