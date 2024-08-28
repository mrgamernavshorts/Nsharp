import os
autorun_init = 0
print('N# Complier')
if os.path.exists('autorun_init.txt'):
    autorun_init = 1
    print('autorun enabled')
else:
    pass
if autorun_init == 0:
    q = input('enter the file name :')
elif autorun_init == 1:
    with open('autorun_init.txt','r') as f:
        q = f.read()
if q == 'autorun':
    file_name = input('enter the file name you want to autorun :')
    with open('autorun_init.txt','w') as f:
        f.write(file_name)
    print('autorun eneabled')
    input('exit ?:')
    exit()
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
    elif line.startswith('add:num1:input:'):
        num1 = int(input('num1 :'))
    elif line.startswith('add:num2:input:'):
        num2 = int(input('num2 :'))
    elif line.startswith('sub:num1:input:'):
        num1 = int(input('num1 :'))
    elif line.startswith('sub:num2:input:'):
        num2 = int(input('num2 :'))
    elif line.startswith('div:num1:input:'):
        num1 = int(input('num1 :'))
    elif line.startswith('div:num2:input:'):
        num2 = int(input('num2 :'))
    elif line.startswith('multi:num1:input:'):
        num1 = int(input('num1 :'))
    elif line.startswith('multi:num2:input:'):
        num2 = int(input('num2 :'))
    elif line.startswith('expo:num1:input:'):
        num1 = int(input('num1 :'))
    elif line.startswith('expo:num2:input:'):
        num2 = int(input('num2 :'))
    elif line.startswith('add:num1:'):
        num1 = int(line[10:])
    elif line.startswith('add:num2:'):
        num2 = int(line[10:])
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
    elif line.startswith('expo:num1:'):
        num1 = int(line[10:])
    elif line.startswith('expo:num2:'):
        num2 = int(line[10:])
    elif line.startswith('exporun:'):
        if num1 is not None and num2 is not None:
            expoans = num1 ** num2
            print(expoans)
        else:
            print('num1 and num2 not defined')

input('exit ? :')