from pprint import pprint

d = dict(locals(), **globals())
exec("a=1", d, d)
exec("a+=1", d, d)
exec("print(a)", d, d)

pprint(d)
