#coding=utf-8
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        res = "".join(set(t)-set(s))
        if res!="":
            return res
        else:
            s_table = {}
            t_table = {}
            for i in s:
                v=s_table.get(i)
                if v == None:
                    s_table[i]=1
                else:
                    s_table[i]=v+1
            for j in t:
                v = t_table.get(j)
                if v == None:
                    t_table[j] = 1
                else:
                    t_table[j] = v + 1

            for k in t_table.keys():
                if t_table[k] != s_table[k]:
                    return k

class Solution2(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        res = 0
        for i in s:
            res ^= ord(i)
        for j in t:
            res ^= ord(j)
        return chr(res)

class Solution3(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        return chr(sum(map(ord, t)) - sum(map(ord, s)))


if __name__ == '__main__':
    print Solution3().findTheDifference("abcd", "abccd")
