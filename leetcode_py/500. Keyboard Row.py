import re


class Solution(object):
    def __init__(self):
        self.table1 = set('qwertyuiop')
        self.table2 = set('asdfghjkl')
        self.table3 = set('zxcvbnm')

    def findWords(self, words):
        """
        :type words: list[str]
        :rtype: list[str]
        """
        res = []
        for i in words:
            ilower = set(i.lower())
            if ilower.issubset(self.table1):
                res.append(i)
            elif ilower.issubset(self.table2):
                res.append(i)
            elif ilower.issubset(self.table3):
                res.append(i)
        return res


class Solution2(object):
    def findWords(self, words):
        return filter(re.compile('(?i)([qwertyuiop]*|[asdfghjkl]*|[zxcvbnm]*)$').match, words)


class Solution3(object):
    def findWords(self, words):
        return [word for word in words if
                any(set(word.lower()) <= set(row) for row in [set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')])]


if __name__ == '__main__':
    print Solution3().findWords(["Hello", "Alaska", "Dad", "Peace"])
