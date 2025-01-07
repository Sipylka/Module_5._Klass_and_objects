# Пример простейшего класса, который ничего не делает
class A:
    pass

a = A()
b = A()
a.arg = 1  # у экземпляра a появился атрибут arg, равный 1
b.arg = 2  # а у экземпляра b - атрибут arg, равный 2
print(a.arg)
print(b.arg)

c = A()
c.arg = 5
print(c.arg)  # а у этого экземпляра нет arg
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'A' object has no attribute 'arg'