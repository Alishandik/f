# module_1_5.py
# 1. Задайте переменные разных типов данных
immutable_var=(1,"Hello",True,3.14)
print(immutable_var)
# 2. Изменение значений переменных:Кортеж (tuple) в Python является неизменяемым(immutable) типом данных. Все таки при попытке изменить его выйдет ошибка TypeError.
# 3.Создание изменяемых структур данных:
mutable_list=[1,2,"a","b"]
print(mutable_list)
mutable_list.append("Modified")
print("mutable_list:",mutable_list)
