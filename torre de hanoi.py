# listas de torres
a1 = [] 
b2 = []
c3 = []
# variavel para quantidade de discos
y = 0
# para o codigo iniciar
x = True
# função para definir se a jogada é invalida   
def ehInvalida(to, td):
    if len(to) == 0: # para verificar se a torre esta vazia 
        return True
    elif len(td) > 0:
        if to[-1] > td[-1]: # para verificar se tem um disco menor no destino do disco maior
            return True
        else:
            return False
# função para verificar se tem ganhador 
def tem_ganhador():
    for i in range(y, 0, -1):
        if i not in c3:
            return False
    print (" VOCÊ COMPLETOU A TORRE! PARABENS !!!! ")
    return True
# função para mover os discos de torre
def posição():
           global y
           print("no minimo 3 discos ")
           y = int(input("Digite quantos discos você quer: "))
           a1 = list(range(y, 0, -1)) # para criar a torre com os discos impilhados
           # para repetir as jogas  
           while not tem_ganhador():
               print("'a' para torre 1 / 's' para torre 2 / 'd' para torre 3")
               # definir a torre de origem e a torre de destino
               x = input(" Digite a torre de origem: ")
               z = input("Digite a torre de destino: ")
               to = []
               td = []
            
               if x == 'a':
                    to = a1
               elif x == 's':
                    to = b2
               elif x == 'd':
                    to = c3

               if z == 'a':
                    td = a1
               elif z == 's':
                    td = b2
               elif z == 'd':
                    td = c3

               if not ehInvalida(to, td):
                    print('faz movimento')
                    # para retirar o disco da torre de origem
                    if x == 'a':
                        val = a1.pop()
                    elif x == 's':
                        val = b2.pop()
                    elif x == 'd':
                        val = c3.pop()
                    # para acrescentar o disco na torre de destino
                    if z == 'a':
                        a1.append(val)
                    elif z == 's':
                        b2.append(val)
                    elif z == 'd':
                        c3.append(val)
                    # para mostrar as torres
                    print ("", a1)
                    print ("", b2)
                    print ("", c3)
               else:
                    print('jogada invalida')

  
# menu para inciar partida ou sair do jogo            
while x == True:
    print("para jogar digite '1'")
    print("para sair do jogo digite '2'")
    z = input("digite sua opção: ")
    if z == '1':
        a1 = [] 
        b2 = []
        c3 = []
        posição()
    elif z == '2':
        x = False
        

        
        
        
