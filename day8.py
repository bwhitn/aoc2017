import operator

reg = {}
tmpval = 0
ops = {
    "<":operator.lt,
    ">":operator.gt,
    ">=":operator.ge,
    "<=":operator.le,
    "==":operator.eq,
    "!=":operator.ne
}

def execute_condition(condition):
    assert isinstance(condition, list) and len(condition) == 3
    global ops
    return ops[condition[1]](reg[condition[0]], int(condition[2]))

def execute_statement(statement):
    assert isinstance(statement, list) and len(statement) == 7
    global tmpval
    condition_val = execute_condition(statement[4:])
    statement = statement[:3]
    if condition_val:
        if statement[1] == "dec":
            reg[statement[0]] = reg[statement[0]] - int(statement[2])
        else:
            reg[statement[0]] = reg[statement[0]] + int(statement[2])
    if tmpval < reg[statement[0]]:
        tmpval = reg[statement[0]]

with open("day8.txt") as instructions:
    instruction_list = []
    for instruction in instructions:
        val = instruction.split()
        reg[val[0]] = 0
        instruction_list.append(val)
    for instruction in instruction_list:
        execute_statement(instruction)
print("Highest value during execution is: {}".format(str(tmpval)))

#Find the largest
tmpval = 0
for val in reg.values():
    if val > tmpval:
        tmpval = val
print("Highest final value is: {}".format(str(tmpval)))
