"""
This is the helper module. The attributes of this module
do not interact withy facebook rather help get better
info about the objects fethced from facebook.
"""

D=type( {1:1} )
L=type( [1,2] )

def get_fields(d, s):
        if type(d) == D:
                for i in d.keys():
                        if type(d[i]) == L:
                                print(s+i+"(list)")
                        else:
                                print(s+i)
                        r = len(i)
                        r = ' '*r 
                        get_fields(d[i], r+s)

        elif type(d) == L:
                a = d[0]
                l = len(a)
                for i in a.keys():
                        if type(a[i]) == L:
                                print(s+i+"(list)")
                        else:
                                print(s+i)  
                        r = len(i)
                        r = " "*r
                        get_fields(a[i], r+s)


def fields(d):
        return get_fields(d, '')
