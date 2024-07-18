immutable_var = ("Aleksandr", 13, True)
print(immutable_var)
# immutable_var[0] = 13
# Кортеж не изменяется потому что он используется для харнения элементов, которые программист не хочет изменять
mutable_list = ["Aleksandr", 13, True]
mutable_list[1] = 69
print(mutable_list)
mutable_list.append("Dragon")
print(mutable_list)
mutable_list.extend("FIRE")
print(mutable_list)