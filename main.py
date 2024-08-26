print('N# Complier')
q = input('enter file name :')
var = ''
with open(q,'r') as f:
    code = f.readlines()
if code[0].strip().startswith('write:'):
    print(code[0].strip()[6:])
elif code[0].strip().startswith('createvar:'):
    var = code[0].strip()[10:]
    print(f'the value is stored as {var}')
    w = input('print it? :')
    if w == 'y':
        print(var)
    else:
        pass
if code[1].strip().startswith('write:'):
    print(code[1].strip()[6:])
if code[1].strip().startswith('createvar:'):
    var = code[1].strip()[10:]
    print(f'the value is stored as {var}')
    w = input('print it? :')
    if w == 'y':
        print(var)
    else:
        pass
input('exit ? :')