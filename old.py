if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            print(verde_rect.collidepoint(pos))
            if verde_rect.collidepoint(pos) and lista[0] == 0 and flag4 == True:
                ck.append(0)
                print(ck)
                print("Parabéns o correto é verde!")
                r_verde_claro(window)
                SOM00.play()
                pygame.time.wait(1500)
                r_base(window)
                pygame.time.wait(1500)
                novo_teste(lista[0])
                novo_teste(lista[1])
                flag4 = False
                

            elif vermelho_rect.collidepoint(pos) and lista[0] == 1 and flag4 == True:
                ck.append(1)
                print(ck)
                print("Vermelho")
                r_vermelho_claro(window)
                SOM01.play()
                pygame.time.wait(1500)
                r_base(window)
                pygame.time.wait(1500)
                novo_teste(lista[0])
                novo_teste(lista[1])
                flag4 = False

            elif amarelo_rect.collidepoint(pos) and lista[0] == 2 and flag4 == True:
                ck.append(2)
                print(ck)
                print("Amarelo")
                r_amarelo_claro(window)
                SOM02.play()
                pygame.time.wait(1500)
                r_base(window)
                pygame.time.wait(1500)
                novo_teste(lista[0])
                novo_teste(lista[1])
                flag4 = False

            elif azul_rect.collidepoint(pos) and lista[0] == 3 and flag4 == True:
                ck.append(3)
                print(ck)
                print("Azul")
                r_azul_claro(window)
                SOM03.play()
                pygame.time.wait(1500)
                r_base(window)
                pygame.time.wait(1500)
                novo_teste(lista[0])
                novo_teste(lista[1])
                flag4 = False