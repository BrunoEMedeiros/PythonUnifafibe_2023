
def soma(args: tuple) -> float:
    try:
        #if type(a) == float and type(b) == float or type(a) == int and type(b) == int:
        if args.__le__ == 2:
            if isinstance(args[0], (int,float)) and isinstance(args[1], (int,float)):
                return (args[0] + args[1])
            else:
                return ("tipos incompativeis")
        else:
            return ("Ha parametros faltando!!!")
    except:
        return ("Erro inesperado!")

soma((10))

