from math import *
from functools import lru_cache
class polygon_sequence:
    def __init__(self,n,r):
        self.n = n
        self.r = r
        self.s = self.edge_length()
        self.ia = self.interior_angle()
        self.a = self.apothem()
        self.per = self.perimeter()
        self.ar = self.area()
    def interior_angle(self):
        ia = (self.n - 2)*(180/self.n)
        return ia
    def edge_length(self):
        s = 2*self.r*sin(pi/self.n)
        return s
    def apothem(self):
        a = self.r * cos(pi/self.n)
        return a
    def area(self):
        s = self.edge_length()
        a = self.apothem()
        ar = (self.n * s * a)/2
        return ar
    def perimeter(self):
        s = self.edge_length()
        per = self.n * s
        return per
    def __repr__(self):
        print("This class create the convex polygons and\
        calculates their attributes")
    def __eq__(self,other):
        return (self.n == other.n) and (self.r == other.r)
    def __gt__(self,other):
        return (self.n > other.n)
    def __len__(self):
        pass
    def __getitem__(self,sl):
        if isinstance(sl,int):
            if sl < 0 or sl >= self.n:
                raise IndexError
            else:
                return polygon_sequence._ps(sl)
    @staticmethod
    @lru_cache(2**10)
    def _ps(n):
        if n < 2 :
            print( n)
            return "Not posible"
        else:
            return polygon_sequence._ps(n-1)+polygon_sequence._ps(n-2)
            