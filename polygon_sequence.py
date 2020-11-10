

from math import *
from polygons import *


class polygons_sequence:
    def __init__(self,n,r):
        self.n = n
        if n < 3:
            raise ValueError("n must be greater then 3")
        self.r = r
        self._polygons = list([polygons((i), r )  for (i) in range(3,n+1)])
    def __repr__(self):
        return f'No of sides :{self.n} , \n Radius : {self.r}'
    def __len__(self):
        return self.n -2 
    def __getitem__(self,s):
        return self._polygons[s]
    

    def max_efficiency_polygons(self):
        seq = sorted(self._polygons,
                    key = lambda p:p.area()/p.perimeter(),
                    reverse = True)
        # print(seq)
        return seq[0]
    