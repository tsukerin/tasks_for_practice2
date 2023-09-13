from pulp import *
import time

start = time.time()
x1 = LpVariable("x1", 0)
x2 = LpVariable("x2", 0)
x3 = LpVariable("x3", 0)
x4 = LpVariable("x4", 0)
problem = LpProblem("myProblem", LpMinimize)
problem += x1 +x2 + 3*x3 + 4*x4, "Функция цели"
problem += 5*x1 - 6*x2 + x3 - 2*x4 == 2, "1 условие"
problem += 11*x1 - 14*x2 + 2*x3 - 5*x4 == 2, "2 условие"
status = problem.solve()
print(LpStatus[status])
print("Результат:")
for variable in problem.variables():
    print(variable.name, "=", variable.varValue)
print("Прибыль:")
print(value(problem.objective))
stop = time.time()
print("Время :")
print(stop-start)

problem = LpProblem("myProblem", LpMaximize)
problem += x1 +x2 + 3*x3 + 4*x4, "Функция цели"
problem += 5*x1 - 6*x2 + x3 - 2*x4 == 2, "1 условие"
problem += 11*x1 - 14*x2 + 2*x3 - 5*x4 == 2, "2 условие"
status = problem.solve()
print(LpStatus[status])
print("Результат:")
for variable in problem.variables():
    print(variable.name, "=", variable.varValue)
print("Прибыль:")
if(value(problem.objective) > 20):
    print("Максимум отсутсвует")
else:
    print(value(problem.objective))
stop = time.time()
print("Время :")
print(stop-start)