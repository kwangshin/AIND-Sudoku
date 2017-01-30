rows = 'ABCDEFGHI'
cols = '123456789'

def cross(a, b):
    return [s+t for s in a for t in b]
def diagonal_linear(a, b):
    return [a[i]+b[i] for i in range(9)]
def diagonal_backward_linear(a, b):
    return [a[i]+b[8-i] for i in range(9)]

boxes = cross(rows, cols)

row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
diagonal_units = [diagonal_linear(rows, cols), diagonal_backward_linear(rows, cols)]
unitlist = row_units + column_units + square_units + diagonal_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)