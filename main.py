print('N# Complier')
q = input('enter file name :')
var = ''
num1 = None
num2 = None
with open(q,'r') as f:
    code = f.readlines()
for line in code:
    line = line.strip()
    if line.startswith('write:'):
        print(line[6:])
    elif line.startswith('createvar:input:'):
        var = input('enter the input:')
        print(f'variable stored as {var}')
    elif line.startswith('createvar:'):
        var = line[10:]
        print(f'variable stored as {var}')
    elif line.startswith('printvar:'):
        print(var)
    elif line.startswith('add:num1:'):
        num1 = int(line[9:])
    elif line.startswith('add:num2:'):
        num2 = int(line[9:])
    elif line.startswith('addrun:'):
        if num1 is not None and num2 is not None:
            addans = num1 + num2
            print(addans)
        else:
            print('num1 and num2 not defined')
    elif line.startswith('sub:num1:'):
        num1 = int(line[9:])
    elif line.startswith('sub:num2:'):
        num2 = int(line[9:])
    elif line.startswith('subrun:'):
        if num1 is not None and num2 is not None:
            subans = num1 - num2
            print(subans)
        else:
            print('num1 and num2 not defined')
    elif line.startswith('div:num1:'):
        num1 = int(line[9:])
    elif line.startswith('div:num2:'):
        num2 = int(line[9:])
    elif line.startswith('divrun:'):
        if num1 is not None and num2 is not None:
            divans = num1 / num2
            print(divans)
        else:
            print('num1 and num2 not defined')
    elif line.startswith('multi:num1:'):
        num1 = int(line[11:])
    elif line.startswith('multi:num2:'):
        num2 = int(line[11:])
    elif line.startswith('multirun:'):
        if num1 is not None and num2 is not None:
            multians = num1 * num2
            print(multians)
        else:
            print('num1 and num2 not defined')
input('exit ? :')
