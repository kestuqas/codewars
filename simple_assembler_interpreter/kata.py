# import cython

# class Recurse(Exception):
#     def __init__(self, *args, **kwargs):
#         self.args = args
#         self.kwargs = kwargs

# def recurse(*args, **kwargs):
#     raise Recurse(*args, **kwargs)
        
# def tail_recursive(f):
#     def decorated(*args, **kwargs):
#         while True:
#             try:
#                 return f(*args, **kwargs)
#             except Recurse as r:
#                 args = r.args
#                 kwargs = r.kwargs
#                 continue
#     return decorated
from tail_rezursion import tail_recursive, recurse

# code = '''\
# mov a 5
# inc a
# dec a
# dec a
# jnz a -1
# inc a'''

code = '''\
mov c 12
mov b 0
mov a 200
dec a
inc b
jnz a -2
dec c
mov a b
jnz c -5
jnz 0 1
mov c a'''

program = code.splitlines()

reg_dic = {}

@tail_recursive
def simple_assembler(program, step=0):
    
    for item in program[step:]:
        reg = item[4]
        instr = item[6:]
        start = item[:3]
        if start == 'mov':
            if instr.isalpha():
                reg_dic[reg] = reg_dic[instr]
            else:
                reg_dic[reg] = int(instr)
        elif start == 'inc':
            reg_dic[reg] += 1
        elif start == 'dec':
            reg_dic[reg] -= 1
        elif (reg != '0') and reg.isalpha() and (reg_dic[reg] != 0):
            step += int(instr)
            # simple_assembler(program, step=step)
            recurse(program, step=step)
        step += 1
    return(reg_dic)

print(simple_assembler(program))

