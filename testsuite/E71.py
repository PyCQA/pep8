#: E711
if res == None:
    pass
#: E711
if res != None:
    pass
#: E711
if None == res:
    pass
#: E711
if None != res:
    pass
#: E711
if res[1] == None:
    pass
#: E711
if res[1] != None:
    pass
#: E711
if None != res[1]:
    pass
#: E711
if None == res[1]:
    pass

#
#: E712
if res == True:
    pass
#: E712
if res != False:
    pass
#: E712
if True != res:
    pass
#: E712
if False == res:
    pass
#: E712
if res[1] == True:
    pass
#: E712
if res[1] != False:
    pass

#
#: E713
if not X in Y:
    pass
#: E713
if not X.B in Y:
    pass
#: E713
if not X in Y and Z == "zero":
    pass
#: E713
if X == "zero" or not Y in Z:
    pass
#: E713
if not f(1, 2, 3) in Z:
    pass
#: E713
if not X['a'] in Y:
    pass
#: E713
if not X[Y] in Z:
    pass
#: E713
if not X[f(1, 2, 3)] in Y:
    pass
#: E713
if not f(X[1], X[2], X[3]) in Y:
    pass
#: E713
if not f(X['1'], X['2'], X['3']) in Y:
    pass

#
#: E714
if not X is Y:
    pass
#: E714
if not X.B is Y:
    pass

#
#: Okay
if x not in y:
    pass

if (not x) in y:
    pass

if (not f(1, 2, 3)) in y:
    pass

if (not X['a']) in Y:
    pass

if (not X[Y]) in Z:
    pass

if (not X[f(1, 2, 3)]) in Y:
    pass

if (not f(X[1], X[2], X[3])) in Y:
    pass

if (not f(X['1'], X['2'], X['3'])) in Y:
    pass

if not (X in Y or X is Z):
    pass

if not (X in Y):
    pass

if x is not y:
    pass

if TrueElement.get_element(True) == TrueElement.get_element(False):
    pass

if (True) == TrueElement or x == TrueElement:
    pass

assert (not foo) in bar
assert {'x': not foo} in bar
assert [42, not foo] in bar
#:
