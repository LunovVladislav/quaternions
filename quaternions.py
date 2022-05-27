import numpy as np

class CNum():
    # m - multiplier
    # b - base

    @staticmethod
    def zero():
        return CNum(0)

    @staticmethod
    def dot(f, an):
        if isinstance(an, CNum):
            n = 1
            fb = 'r'
            if f.b == an.b and f.b != 'r':
                n = -1
            elif f.b == 'r' and an.b != 'r':
                fb = an.b
            elif an.b == 'r' and f.b != 'r':
                fb = f.b
            elif f.b == 'i':
                if an.b == 'j':
                    fb = 'k'
                elif an.b == 'k':
                    fb = 'j'
                    n = -1
            elif f.b == 'j':
                if an.b == 'i':
                    fb = 'k'
                    n = -1
                elif an.b == 'k':
                    fb = 'i'
            elif f.b == 'k':
                if an.b == 'i':
                    fb = 'j'
                elif an.b == 'j':
                    fb = 'i'
                    n = -1

            m = n*f.m*an.m
            return CNum(m, fb)

    def dotp(self, an):
        return self.dot(self, an)

    def __init__(self, m, b='r'):
        if isinstance(m, float) or isinstance(m, int):
            self.m = m
        else:
            raise ValueError('First argument must be a real number')
        if b == '1' or b == 'r' or b == 'R':
            self.b = 'r'
        elif b == 'i' or b == 'j' or b == 'k':
            self.b = b
        else:
            raise ValueError('Base type is not supported')
    
    def __str__(self):
        add = self.b
        if self.b == 'r':
            add = ''
        if self.m != 1 and self.m != -1 or add == '':
            return str(round(self.m, 3))+add
        elif self.m == 1 and add != '':
            return add
        elif self.m == -1 and add != '':
            return '-'+add


class CVNum():
    @staticmethod
    def dot(a, b):
        if isinstance(a, CVNum) and isinstance(b, CVNum):
            arr = []
            al = a.as_list()
            bl = b.as_list()

            for i in range(4):
                for j in range(4):
                    arr.append(al[i].dotp(bl[j]))
            
            p = [
                [],
                [],
                [],
                []
            ]

            for i in range(len(arr)):
                if arr[i].b == 'r':
                    p[0].append(arr[i])
                elif arr[i].b == 'i':
                    p[1].append(arr[i])
                elif arr[i].b == 'j':
                    p[2].append(arr[i])
                elif arr[i].b == 'k':
                    p[3].append(arr[i])
            
            res = [0, 0, 0, 0]

            for i in range(len(p)):
                r = 0
                for j in range(len(p[i])):
                    r += p[i][j].m
                res[i] = r
            
            return CVNum(res)
        else:
            raise ValueError('Function ony accepts two agrumnts of type CVNum')
    
    def dotp(self, b):
        return self.dot(self, b)
    
    def m(self, ml):
        return CVNum(self.r.m * ml, self.i.m * ml, self.j.m * ml, self.k.m * ml)
    
    def m_except_real(self, m):
        return CVNum(self.r.m, self.i.m * m, self.j.m * m, self.k.m * m)
    
    def rotate(self, base_vector, degree):
        vec = self
        if base_vector.i.m**2+base_vector.j.m**2+base_vector.k.m**2 == 1 and base_vector.r.m == 0 and isinstance(base_vector, CVNum) and isinstance(degree, float) or isinstance(degree, int):
            bv = base_vector
            bv.r.m = np.cos(degree/2)
            bv = bv.m_except_real(np.sin(degree/2))
            bv = bv.dotp(vec)

            bv1 = base_vector
            bv1.r.m = np.cos(-degree/2)
            bv1 = bv1.m_except_real(np.sin(-degree/2))
            return bv.dotp(bv1)
        else:
            raise ValueError('Base vector must have 0 real part, and degree must be float or int')

    def as_list(self):
        return [self.r, self.i, self.j, self.k]

    def __init__(self, f, s='null', t='null', ft='null'):
        if isinstance(f, list):
            if len(f) == 3:
                r = CNum.zero()
                i = CNum(f[0], 'i')
                j = CNum(f[1], 'j')
                k = CNum(f[2], 'k')
            elif len(f) == 4:
                r = CNum(f[0], 'r')
                i = CNum(f[1], 'i')
                j = CNum(f[2], 'j')
                k = CNum(f[3], 'k')
            else:
                raise ValueError('If you provide arguments via list, it has to consist of 3 or 4 elements')
        elif isinstance(f, float) or isinstance(f, int) and isinstance(s, float) or isinstance(s, int) and isinstance(t, float) or isinstance(t, int):
            if isinstance(ft, float) or isinstance(ft, int):
                r = CNum(f)
                i = CNum(s, 'i')
                j = CNum(t, 'j')
                k = CNum(ft, 'k')
            else:
                r = CNum.zero()
                i = CNum(f, 'i')
                j = CNum(s, 'j')
                k = CNum(t, 'k')
        else:
            if isinstance(f, CNum) == False or isinstance(s, CNum) == False or isinstance(t, CNum) == False:
                raise ValueError('All arguments must have \'CNum\' type')
            if isinstance(ft, CNum) == False:
                r = CNum.zero()
                i = f
                j = s
                k = t
            else:
                r = f
                i = s
                j = t
                k = ft
 
        if i.b == 'i' and j.b == 'j' and k.b == 'k' and r.b == 'r':
            self.r = r
            self.i = i
            self.j = j
            self.k = k
        else:
            raise ValueError('Arguments must have r, i, j, k or i, j, k bases')
    
    def __str__(self):
        front = ''
        if self.r.m != 0:
            front = str(self.r.m)
        sn = ['', '', '']
        if self.i.m >= 0 and front != '':
            sn[0] = '+'
        if self.j.m >= 0:
            sn[1] = '+'
        if self.k.m >= 0:
            sn[2] = '+'
        
        return (front+sn[0]+self.i.__str__()+sn[1]+self.j.__str__()+sn[2]+self.k.__str__())
