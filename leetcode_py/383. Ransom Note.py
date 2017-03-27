class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine_k_v = {}
        for i in magazine:
            t = magazine_k_v.get(i)
            if t == None:
                magazine_k_v[i]=1
            else:
                magazine_k_v[i]+=1
        for j in ransomNote:
            t = magazine_k_v.get(j)
            if t == None:
                return False
            elif t == 0:
                return False
            else:
                magazine_k_v[j]=t-1
        return True


if __name__ == '__main__':
    print Solution().canConstruct("a", "b")
    print Solution().canConstruct("aa", "ab")
    print Solution().canConstruct("aa", "aab")
