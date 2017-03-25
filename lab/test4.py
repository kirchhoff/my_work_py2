#coding = utf-8
f = open("c:/Users/kirchhoff/Desktop/test.txt")
l = f.readlines()
l2= []
for i in l:
    l2.append(i[:-1])
l3 = []
l4=[]
for w in ['2016','2015','2014','2013','2012','2011','2010','2009','2008']:
    l3 = []
    l4=[]
    for i in l2:
        if w in i:
            if 'Conference' in i:
                l3.append(i)
            elif 'conference' in i:
                l3.append(i)
            else:
                l4.append(i)

    def my_cmp(s1, s2):
        m1 = s1.split('.')[0].split(',')
        m2 = s2.split('.')[0].split(',')
        n1 = 0
        n2 = 0
        for i, j in enumerate(m1):
            if "Wanchun" in j:
                n1 = i
        for i, j in enumerate(m2):
            if "Wanchun" in j:
                n2 = i

        if n1<n2:
            return -1
        if n1>n2:
            return 1
        return 0

    def my_cmp2(s1, s2):
        if "Transaction" in s1:
            return -1
        if "Transaction" in s2:
            return 1
        return 0

    s = sorted(l4, my_cmp)
    s2 = sorted(s,my_cmp2)
    for i in s2:
        print i
