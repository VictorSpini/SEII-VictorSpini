//Victor Spini Paranaiba - 11611EMT005

# Inicia-se importando os módulos que permite execução de thread e apoio para trabalhar com funções de tempo
import concurrent.futures	# Interface para processos e threads de forma assincrona
import time	# Para utilizar funções relacionadas a tempo
import threading	# Suporte para thread

start = time.perf_counter()	# Definição do início do performance counter

#Função aleatória para exemplo
def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    # print('Done Sleeping...')
    return f'Done Sleeping...{seconds}'

with concurrent.futures.ThreadPoolExecutor() as executor:	# Executor de processos e threads de forma assincrona
    # f1 = executor.submit(do_something, 1)	
    # f2 = executor.submit(do_something, 1)	# executores f1 e f2 para a função de exemplo
    # print(f1.result())	# Retorna o primeiro executor
    # print(f2.result())	# Retorna o segundo executor
    # results = [executor.submit(do_something, 1) for _ in range(10)]	# Lista de tamanho (range) 10 de possíveis executores
    secs = [5, 4, 3, 2, 1]
    # results = [executor.submit(do_something, sec) for sec in secs] # Seguindo as definições e parâmetros, cria-se uma lista de executores para a função.
    # for f in concurrent.futures.as_completed(results):  
    #    print(f.result()) 	# Exibido o resultado conforme finalização dos processos
    results = executor.map( do_something, secs) 	# De acordo com cada parâmetro listado, é executada a função exemplo 

    for result in results:  
        print(result)	# Exibição dos resultados do map na ordem de execução

# threads = []		# Cria-se uma lista vazia

# Thread para executar a função para o parametro abaixo
# for _ in range(10):
#    t = threading.Thread(target=do_something, args=[1.5])	#Parâmetro
#    t.start()		 # Início da thread
#    threads.append(t)	 # Threads adicionadas na lista

# for thread in threads:	# Segura o processo até a finalização de cada thread
#    thread.join()

# t1 = threading.Thread(target=do_something)
# t2 = threading.Thread(target=do_something) 	# Cria-se thread para executar a função

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# do_something()
# do_something()	# Chama a função

finish = time.perf_counter()  # Função de contabilização e encerramento do contador de performance
print(f'Finished in {round(finish-start, 2)} second(s)')
