#coding=utf-8
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word[0].isupper() and word[1:].lower() == word[1:]:
            return True
        elif word.isupper():
            return True
        elif word.islower():
            return True
        else:
            return False



if __name__ == '__main__':
    print Solution().detectCapitalUse("USA")