from ArvPesqBinaria import ArvPesqBinaria

arvore01 = ArvPesqBinaria()
while True: 
    interface = input("""
-------------------------------------------------------------------------------------
                ÁRVORE 01                    
1. ADICIONAR elementos na árvore.
2. Retornar o PAI de um elemento.
3. Verificar qual é a ALTURA da árvore.
4. Verificar quantos ELEMENTOS tem na árvore.
5. Verificar se a árvore está VAZIA.
6. Retornar os elementos da árvore com CAMINHAMENTOS(em ordem, pré ordem e pós ordem).
7. PROCURAR nó.
8. Sair e ir para interface da árvore 02.
                      
Digite a opção que você quer executar:""")

    if interface == "1":
        elemento = int(input("Qual elemento você deseja adicionar: "))
        arvore01.insert(elemento)

    if interface == "2":
        elemento = int(input("Qual elemento você quer saber o pai: "))
        arvore01.get_father(elemento)

    if interface == "3":
        altura = arvore01.height(arvore01.get_root())
        print(altura - 1)

    if interface == "4":
        tamanho = arvore01.size(arvore01.get_root())
        print(tamanho)

    if interface == "5":
        print(arvore01.is_empty())
        
    
    if interface == "6":
        print('')
        arvore01.in_order(arvore01.get_root())
        print('\n')
        arvore01.pre_order(arvore01.get_root())
        print('\n')
        arvore01.post_order(arvore01.get_root())

    if interface == "7":
        chave = int(input("Qual elemento você deseja procurar: "))
        arvore01.search(chave)

    if interface == "8":
        print("Saindo da interface da árvore 1...")
        break



arvore02 = ArvPesqBinaria()
while True: 
    interface = input("""
-------------------------------------------------------------------------------------
                ÁRVORE 02
1. ADICIONAR elementos na árvore.                    
2. Retornar o PAI de um elemento.
3. Verificar qual é a ALTURA da árvore.
4. Verificar quantos ELEMENTOS tem na árvore.
5. Verificar se a árvore está VAZIA.
6. Retornar os elementos da árvore com CAMINHAMENTOS(em ordem, pré ordem e pós ordem).
7. PROCURAR nó.
8. Sair e ir para interface da árvore 03.
                      
Digite a opção que você quer executar:""")

    if interface == "1":
        elemento = int(input("Qual elemento você deseja adicionar: "))
        arvore02.insert(elemento)

    if interface == "2":
        elemento = int(input("Qual elemento você quer saber o pai: "))
        arvore02.get_father(elemento)

    if interface == "3":
        altura = arvore02.height(arvore02.get_root())
        print(altura - 1)

    if interface == "4":
        tamanho = arvore02.size(arvore02.get_root())
        print(tamanho)

    if interface == "5":
        print(arvore02.is_empty())
    
    if interface == "6":
        print('')
        arvore02.in_order(arvore02.get_root())
        print('\n')
        arvore02.pre_order(arvore02.get_root())
        print('\n')
        arvore02.post_order(arvore02.get_root())

    if interface == "8":
        print("Saindo da interface da árvore 2")
        break



arvore03 = ArvPesqBinaria()
while True: 
    interface = input("""
-------------------------------------------------------------------------------------
                ÁRVORE 03   
1. ADICIONAR elementos na árvore.                 
2. Retornar o PAI de um elemento.
3. Verificar qual é a ALTURA da árvore.
4. Verificar quantos ELEMENTOS tem na árvore.
5. Verificar se a árvore está VAZIA.
6. Retornar os elementos da árvore com CAMINHAMENTOS(em ordem, pré ordem e pós ordem).
7. PROCURAR nó.
8. Sair.
                      
Digite a opção que você quer executar:""")

    if interface == "1":
        elemento = int(input("Qual elemento você deseja adicionar: "))
        arvore03.insert(elemento)

    if interface == "2":
        elemento = int(input("Qual elemento você quer saber o pai: "))
        arvore03.get_father(elemento)

    if interface == "3":
        altura = arvore03.height(arvore03.get_root())
        print(altura - 1)

    if interface == "4":
        tamanho = arvore03.size(arvore03.get_root())
        print(tamanho)

    if interface == "5":
        print(arvore03.is_empty())
    
    if interface == "6":
        print('')
        arvore03.in_order(arvore03.get_root())
        print('\n')
        arvore03.pre_order(arvore03.get_root())
        print('\n')
        arvore03.post_order(arvore03.get_root())

    if interface == "8":
        print("Saindo da interface")
        break

