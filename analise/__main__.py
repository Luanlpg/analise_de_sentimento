import sys
import nltk

from aprendizado import Learn

RED   = "\033[1;31m"
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
RESET = "\033[0;0m"
REVERSE = "\033[;7m"

# baixa stop words
nltk.download('punkt')
nltk.download('stopwords')

# instancio a classe de aprendizado
ln = Learn()
# chamo o meto de iniciaização de aprendizado
ln.start()

def first_menu():
    """
    Método de execução de menu.
    """
    global cache

    try:
        def prt():
            """
            Menu principal.
            """ 
            print('--------------------------------------------------------')
            print('-----------------'+RED+'ANÁLISE DE SENTIMENTO'+RESET+'------------------')
            print('--------------------------------------------------------')
            print('--- '+RED+'1'+RESET+' - '+BLUE+'Teste de qualidade do modelo criado.'+RESET+' -----------')
            print('--- '+RED+'2'+RESET+' - '+BLUE+'Identificar sentimento de frase(em inglês).'+RESET+' ----')
            print('--- '+RED+'3'+RESET+' - '+BLUE+'Mostrar a última frase digitada.'+RESET+' ---------------')
            print('--------- '+RED+'Ctrl+C'+RESET+' - '+BLUE+'Para sair do programa.'+RESET+' --------------')
            print('--------------------------------------------------------')
            return '--------------------------------------------------------'
        #salvar última frase inserida   
        # chamo o metodo prt()
        print(prt())
        # armazeno a entrada do usuario na variável opt
        opt = int(input(CYAN+'>>>'+RESET))
        # caso a entrada seja igual a 1, apresento o retorno do método one_zero()
        # que traz a informações do teste de acurácia utilizando 300 frases
        if opt == 1:
            erro, acuracia = ln.one_zero()
            print(REVERSE+'          '+erro+'            '+RESET)
            print(REVERSE+'            '+acuracia+'             '+RESET)
            # chamo o menu principal novamente
            return first_menu()
        # caso a entrada seja igual a 2, solicito ao usuário uma frase em inglês
        # que ser vira como parametro para a chamada do método one(),  que retorna
        # a informação de positivo ou negativo, dependendo da frase
        elif opt == 2:
            print('-------'+RED+'Digite a frase em inglês a ser analisada'+RESET+'--------')
            print('-------'+RED+'Exemplos: i am happy\ Im afraid \ Im excited:'+RESET+'--------')
            data = str(input(CYAN+'>>>'+RESET))
            cache = data
            print(REVERSE+'                   '+ln.one(data)+'                    '+RESET)
            # chamo o menu principal novamente
            return first_menu()

        elif opt == 3:
            #caso a entrada for igual a 3, mostro qual foi a última frase digitada
            #verificando se o usuário já inseriu alguma frase
            if cache == "":
                print(REVERSE+'   '+'Nenhuma frase digitada'+'   '+RESET)
                # chamo o menu principal novamente
                return first_menu()
            #se inseriu, apresento qual frase foi
            else:
                print(REVERSE+'   '+cache+'   '+RESET)
                # chamo o menu principal novamente
                return first_menu()
        # caso a entrada seja diferente de 1,2,3 retorno uma mensagem de erro
        else:
            print('------------------'+RED+'ENTRADA INVALIDA!!!'+RESET+'-------------------')
            # chamo o menu principal novamente
            return first_menu()
    # em caso de KeyboardInterrupt(Ctrl_C) retorno mensagem de finalização e feco o programa
    except KeyboardInterrupt:
        print('---------------------'+RED+'FIM!!!'+RESET+'------------------------')
        sys.exit()
    #em casdo de NameError que é usado na hora de montar o cache da frase retorna o programa ate o usuario inserir uma.
    except NameError:
        print(REVERSE+'   '+'Nenhuma frase digitada'+'   '+RESET)
        return first_menu()


first_menu()
