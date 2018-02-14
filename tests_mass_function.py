# This tests should be run with -i so that
# it does not start a new variable namespace.

assert 179 <= mass('C6H12O6') <= 182 # 180.156
assert 179 <= m('C6H12O6') <= 182 # 180.156
assert 155 <= m('Cu(II)SO4') <= 165 # 159.609
assert 188 <= m('KHC4H4O6') <= 189 # 188.177
assert 59 <= m('(CH3)2CHOH') <= 61 # ‎60.096
assert 470 <= m('KAl(SO4)2·12H2O') <= 480 # 474.3884

# TODO : implement other stuffs
# assert 285 <= m('Na2CO3.10 H2O') <= 287 # 286.1
# assert 285 <= m('Na2CO3+10H2O') <= 287 # 286.1