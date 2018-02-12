# This tests should be run with -i so that
# it does not start a new variable namespace.

assert H < He < Li < C < O < Cl
assert 12 <= C < 12.5 # 12.0107
assert 179 <= mass('C6H12O6') <= 182 # 180.156
assert 179 <= m('C6H12O6') <= 182 # 180.156
assert 155 <= m('Cu(II)SO4') <= 165 # 159.609
