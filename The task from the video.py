# The task is taken from this video - https://youtu.be/SjSY9PBfDj4

# 0
times = lambda x: lambda y: x * y
plus = lambda x: lambda y: x + y
minus = lambda y: lambda x: x - y
divided_by = lambda y: lambda x: x // y

# 1
seven = lambda x = None: x(7) if callable(x) else 7
five = lambda x = None: x(5) if callable(x) else 5

# 2 
four = lambda x = None: x(4) if callable(x) else 4
nine = lambda x = None: x(9) if callable(x) else 9

# 3
eight = lambda x = None: x(8) if callable(x) else 8
three = lambda x = None: x(3) if callable(x) else 3

# 4
six = lambda x = None: x(6) if callable(x) else 6
two = lambda x = None: x(2) if callable(x) else 2

# 1
assert seven(times(five())) == 35
# 2
assert four(plus(nine())) == 13
# 3
assert eight(minus(three())) == 5
# 4
assert six(divided_by(two())) == 3


print('Успех')
