#!/usr/bin/env python3

from mgraph import digraph, trigraph

assert digraph(0)       == '00'
assert digraph(1)       == '01'
assert digraph(12)      == '0C'
assert digraph(123)     == '3F'
assert digraph(1234)    == 'YA'
assert digraph(12345)   == digraph(681) == 'IX'
assert digraph(123456)  == digraph(336) == '9C'
assert digraph(1294)    == 'ZY'
assert digraph(1295)    == 'ZZ'
assert digraph(1296)    == digraph(0) == '00'
assert digraph(1297)    == digraph(1) == '01'

assert trigraph(0)      == '000'
assert trigraph(1)      == '001'
assert trigraph(12)     == '00C'
assert trigraph(123)    == '03F'
assert trigraph(1234)   == '0YA'
assert trigraph(12345)  == '9IX'
assert trigraph(123456) == trigraph(30144) == 'N9C'
assert trigraph(46654)  == 'ZZY'
assert trigraph(46655)  == 'ZZZ'
assert trigraph(46656)  == trigraph(0) == '000'
assert trigraph(46657)  == trigraph(1) == '001'

for x in [0, 1, 12, 123, 1234, 12345, 123456, 1294, 1295, 1296, 1297]:
    print(f"digraph({x}) -> '{digraph(x)}'")

for x in [0, 1, 12, 123, 1234, 12345, 123456, 46654, 46655, 46656, 46657]:
    print(f"trigraph({x}) -> '{trigraph(x)}'")

