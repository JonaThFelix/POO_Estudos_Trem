from Trem import Trem

#Criação do Objeto
trem1 = Trem('Trem 101','Destino Camaragibe')
trem2 = Trem('Trem 404','Destino Jaboatão')

trem1.apresentar()
print('-'*80,'\n')

#Execução do Objeto trem1

trem1.ligar()
print('-'*80,'\n')

trem1.estacoes(10)
trem1.estacoes(40)
trem1.estacoes(100)

print('-'*80,'\n')

#Execução do Objeto trem2
trem2.ligar()
print('-'*80,'\n')

trem2.apresentar()
trem2.estacoes(80)
trem2.estacoes(10)
trem2.estacoes(10)
trem2.estacoes(10)




