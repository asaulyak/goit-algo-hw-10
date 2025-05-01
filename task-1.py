import pulp

model = pulp.LpProblem("Production", pulp.LpMaximize)

lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
juice = pulp.LpVariable('Juice', lowBound=0, cat='Integer')

model += lemonade + juice, 'Quantity'

# water
model += 2 * lemonade + juice <= 100

# sugar
model += lemonade <= 50

# lemon juice
model += lemonade <= 30

# puree
model += 2 * juice <= 40

model.solve()

print('Lemonade production', lemonade.varValue)
print('Juice production', juice.varValue)

