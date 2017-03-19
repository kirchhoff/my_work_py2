#coding=utf-8
def f(param):
    '''
    :type param: list[str]
    :return: int
    '''
    param.append('test') #这样param就有自动补全了
    n = len(param)
    return n

if __name__ == '__main__':
    print f(['1,2,3,4'])