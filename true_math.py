import sys
import pprint
def introspection_info(obj):
    data = {}
    data['type']= type(obj)
    fot= list(dir(obj))
    c=[]
    b=[]
    d=sys.modules[__name__]
    s1=9
    s2=9
    d=str(d)
    while d[s2]!="'":
        s2+=1
    e=d[s1:s2]
    data['moduls1']=e
    for i in fot:
        if not i[0:2]=='__':
            c.append(i)
        else:
            b.append(i)
    data['atributs']=c
    data['methods']=b
    return data


pprint.pprint(introspection_info(111))
