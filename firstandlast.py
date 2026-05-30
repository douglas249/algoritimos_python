print ('voce pricisa de um login para acessar')
nome = str(input('coloque seu login:'))
senha = int(input('escreva sua senha, somente de numeros:')) 

print ('voce utilizou o nome {} esse é seu login'.format(nome))
print ('voce colocou {} como senha, não esqueça'.format(senha))
print('cadastro criado com sucesso!'.format(nome)) 

logan  = str(input('nome:'))
tria = int(input(('senha:')))

if logan == nome and tria == senha:
    print('aacesso liberado!')

    sacos = int(input('quantos sacos há?'))
    sabão = int(input('há quantas bonbonas de sabão?'))
    sacosbrancos = int(input('há quantos packs de sacos brancos?'))
    vassouras = int(input('há quantas vassouras?'))
    #dando resposta#
    print ('voce tem {} de sacos armazenados'.format(sacos))
    print ('voce tem {} de sabão armazenados'.format(sabão))
    print ('voce tem {} sacos brancos armazenados'.format(sacosbrancos))
    print ('voce tem {} de vassouras armazenadas'.format(vassouras))

    tt = str(input('voce deseja retirar algum material?'))
    gg = tt.strip()
    if gg == 'sim':
     tirarsacos = int(input('quantos de sacos voce deseja tirar?'))     
     tirarsabão = int(input('quantos de sabão deseja tirar?'))
     tirarsacosbrancos = int(input('quantos sacos brancos voce deseja tirar?'))
     tirarvassoura = int(input('quantas vassouras voce deseja tirar?'))

     retirar = sacos - tirarsacos
     retirar1 = sabão - tirarsabão
     retirar2 = sacosbrancos - tirarsacosbrancos
     retirar3 = vassouras - tirarvassoura

     print ('voce possui {} de sacos e voce tirou {}, agora voce tem no total {} sacos'.format(sacos,tirarsacos,retirar))
     print('voce possui {} de sabão, voce retirou {}, voce possui no total {} de sabão'.format(sabão,tirarsabão,retirar1))
     print ('voce tem {} de sacos brancos e voce retirou {}, voce tem no total {} de sacos'.format(sacosbrancos,tirarsacosbrancos,retirar2))
     print ('voce tem {} de vassouras, voce retirou {}, voce tem no total {} de vassouras'.format(vassouras,tirarvassoura,retirar3))
else:  
    print('login incorreto...')

