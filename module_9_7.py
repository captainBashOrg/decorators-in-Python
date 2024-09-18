print ("Декораторы в Python")

def is_prime(func):
    def simpler (*args):    # собираем аргументы основной функции в *args, без этого получается несоотв. к-ва аргументов функций
        result = func(*args)
        orig_sum = sum(args)
        print(simple (orig_sum))
        return result
    return simpler



@is_prime # декоритруем основную функцию.
def sum_three (*args):
    return sum(args)

def simple (x):
    if x < 2:
        return "Сложное" # Технически ноль и 1 составные
    i = 0
    simp = ""
    for i in range (2, x ):
        #print(i, x % i)
        if x % i == 0 :
            return "Сложное"
    return "Простое" # не выпали из цикла по промежуточному делителю наыело, потому их нет, и число простое






#@is_prime:
result = sum_three(2, 3, 6)
print(result)
result = sum_three(2, 3, 16)
print(result)
result = sum_three(2, 3, 26)
print(result)
result = sum_three(1, 2, 3, 4, 5, 9)
print(result)