import pulp
import time

start = time.time()

x1 = pulp.LpVariable("x1", lowBound=0)
x2 = pulp.LpVariable("x2", lowBound=0)
x3 = pulp.LpVariable("x3", lowBound=0)
x4 = pulp.LpVariable("x4", lowBound=0)
x5 = pulp.LpVariable("x5", lowBound=0)
x6 = pulp.LpVariable("x6", lowBound=0)
x7 = pulp.LpVariable("x7", lowBound=0)
x8 = pulp.LpVariable("x8", lowBound=0)
x9 = pulp.LpVariable("x9", lowBound=0)
x10 = pulp.LpVariable("x10", lowBound=0)
x11 = pulp.LpVariable("x11", lowBound=0)
x12 = pulp.LpVariable("x12", lowBound=0)
x13 = pulp.LpVariable("x13", lowBound=0)
x14 = pulp.LpVariable("x14", lowBound=0)
x15 = pulp.LpVariable("x15", lowBound=0)
x16 = pulp.LpVariable("x16", lowBound=0)
x17 = pulp.LpVariable("x17", lowBound=0)
x18 = pulp.LpVariable("x18", lowBound=0)
x19 = pulp.LpVariable("x19", lowBound=0)
x20 = pulp.LpVariable("x20", lowBound=0)
x21 = pulp.LpVariable("x21", lowBound=0)
x22 = pulp.LpVariable("x22", lowBound=0)
x23 = pulp.LpVariable("x23", lowBound=0)
x24 = pulp.LpVariable("x24", lowBound=0)
x25 = pulp.LpVariable("x25", lowBound=0)

problem = pulp.LpProblem('0', pulp.LpMaximize)
problem += (-14 * x1 - 1 * x2 - 18 * x3 - 12 * x4 - 22 * x5
            - 9 * x6 - 9 * x7 - 25 * x8 - 3 * x9 - 21 * x10
            - 3 * x11 - 17 * x12 - 3 * x13 - 15 * x14 - 21 * x15
            - 6 * x16 - 14 * x17 - 10 * x18 - 12 * x19 - 23 * x20
            - 17 * x21 - 19 * x22 - 8 * x23 - 22 * x24 - 7 * x25), "Функция цели"

problem += x1 + x2 + x3 + x4 + x5 <= 122,"1"
problem += x6 + x7 + x8 + x9 + x10 <= 60,"2"
problem += x11 + x12 + x13 + x14 + x15 <= 52,"3"
problem += x16 + x17 + x18 + x19 + x20 <= 3,"4"
problem += x21 + x22 + x23 + x24 + x25 <= 45,"5"
problem += x1 + x6 + x11 + x16 + x21 == 30,"6"
problem += x2 + x7 + x12 + x17 + x22 == 55,"7"
problem += x3 + x8 + x13 + x18 + x23 == 40,"8"
problem += x4 + x9 + x14 + x19 + x24 == 24,"9"
problem += x5 + x10 + x15 + x20 + x25 == 59,"10"
problem.solve()
print("Результат:")
for variable in problem.variables():
    print(variable.name, "=", variable.varValue)
print("Стоимость доставки:")
print(abs(pulp.value(problem.objective)))

finish = time.time()
print("Время : ", finish - start)
