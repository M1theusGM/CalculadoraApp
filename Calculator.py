from tkinter import *
from customtkinter import *
from funções_botoes import *



#####################################

        # Tela da aplicação

app = CTk()

app.title('Calculator')

app.geometry('405x583+700+200')

app.resizable(width=False, height=False)

CTk._set_appearance_mode(app,'dark')

app.iconbitmap('CalculadoraApp/Imagens/Calculator.ico')

######################################


######################################

            # Elementos

label_resultados = CTkLabel(app,
                            width = 398,
                            height = 10,
                            text = '12345',
                            font = ('arial bold', 45),
                            fg_color = '#242424',
                            anchor = E,
                            text_color = '#eaebea')
label_resultados.place(x = 4, y = 85)


            
botão_0 = CTkButton(app,
                    text = '0',
                    fg_color = '#FE8100',
                    command = valor_botao_0,
                    width = 198,
                    height = 60,
                    font = ('arial bold',20),
                    corner_radius = 5,
                    bg_color = '#242424'
                    )

botão_1 = CTkButton(app,
                    text = '1',
                    fg_color = '#FE8100',
                    command = valor_botao_1,
                    width = 98,
                    height = 60,
                    font = ('arial bold',20),
                    corner_radius = 5,
                    bg_color = '#242424')

botão_2 = CTkButton(app,
                    text = '2',
                    fg_color = '#FE8100',
                    command = valor_botao_2,
                    width = 98,
                    height = 60,
                    font = ('arial bold',20),
                    corner_radius = 5,
                    bg_color = '#242424')

botão_3 = CTkButton(app,
                    text = '3',
                    fg_color = '#FE8100',
                    command = valor_botao_3,
                    width = 98,
                    height = 60,
                    font = ('arial bold',20),
                    corner_radius = 5,
                    bg_color = '#242424')

botão_4 = CTkButton(app,
                    text = '4',
                    fg_color = '#FE8100',
                    command = valor_botao_4,
                    width = 98,
                    height = 60,
                    font = ('arial bold',20),
                    corner_radius = 5,
                    bg_color = '#242424')

botão_5 = CTkButton(app,
                    text = '5',
                    fg_color = '#FE8100',
                    command = valor_botao_5,
                    width = 98,
                    height = 60,
                    font = ('arial bold',20),
                    corner_radius = 5,
                    bg_color = '#242424')

botão_6 = CTkButton(app,
                    text = '6',
                    fg_color = '#FE8100',
                    command = valor_botao_6,
                    width = 98,
                    height = 60,
                    font = ('arial bold',20),
                    corner_radius = 5,
                    bg_color = '#242424')

botão_7 = CTkButton(app,
                    text = '7',
                    fg_color = '#FE8100',
                    command = valor_botao_7,
                    width = 98,
                    height = 60,
                    font = ('arial bold',20),
                    corner_radius = 5,
                    bg_color = '#242424')

botão_8 = CTkButton(app,
                    text = '8',
                    fg_color = '#FE8100',
                    command = valor_botao_8,
                    width = 98,
                    height = 60,
                    font = ('arial bold',20),
                    corner_radius = 5,
                    bg_color = '#242424')

botão_9 = CTkButton(app,
                    text = '9',
                    fg_color = '#FE8100',
                    command = valor_botao_9,
                    width = 98,
                    height = 60,
                    font = ('arial bold',20),
                    corner_radius = 5,
                    bg_color = '#242424')

botão_virgula = CTkButton(app,
                    text = '.',
                    fg_color = '#FE8100',
                    command = virgula,
                    width = 98,
                    height = 60,
                    font = ('arial bold',20),
                    corner_radius = 5,
                    bg_color = '#242424')

botão_resultado = CTkButton(app,
                    text = '=',
                    fg_color = '#FE8100',
                    command = igual,
                    width = 98,
                    height = 60,
                    font = ('arial bold',20),
                    corner_radius = 5,
                    bg_color = '#242424')

botão_soma = CTkButton(app,
                    text = '+',
                    fg_color = '#FE8100',
                    command = soma,
                    width = 98,
                    height = 60,
                    font = ('arial bold',20),
                    corner_radius = 5,
                    bg_color = '#242424')

botão_subtra = CTkButton(app,
                    text = '-',
                    fg_color = '#FE8100',
                    command = subtra,
                    width = 98,
                    height = 60,
                    font = ('arial bold',20),
                    corner_radius = 5,
                    bg_color = '#242424')

botão_multipli = CTkButton(app,
                    text = 'x',
                    fg_color = '#FE8100',
                    command = multipli,
                    width = 98,
                    height = 60,
                    font = ('arial bold',20),
                    corner_radius = 5,
                    bg_color = '#242424')

botão_divisao = CTkButton(app,
                    text = '÷',
                    fg_color = '#FE8100',
                    command = divisao,
                    width = 98,
                    height = 60,
                    font = ('arial bold',20),
                    corner_radius = 5,
                    bg_color = '#242424')

botão_limpar = CTkButton(app,
                    text = 'CE',
                    fg_color = '#FE8100',
                    command = limpar,
                    width = 298,
                    height = 60,
                    font = ('arial bold',20),
                    corner_radius = 5,
                    bg_color = '#242424')

botão_ao_quadrado = CTkButton(app,
                    text = 'x²',
                    fg_color = '#FE8100',
                    command = ao_quadrado,
                    width = 198,
                    height = 60,
                    font = ('arial bold',20),
                    corner_radius = 5,
                    bg_color = '#242424')

botão_raiz_quadrada = CTkButton(app,
                    text = '²√x',
                    fg_color = '#FE8100',
                    command = raiz_quadrada,
                    width = 98,
                    height = 60,
                    font = ('arial bold',20),
                    corner_radius = 5,
                    bg_color = '#242424')

botão_limpar_um_por_um = CTkButton(app,
                    text = '⌫',
                    fg_color = '#FE8100',
                    command = limpar_um_por_um,
                    width = 98,
                    height = 60,
                    font = ('arial bold',20),
                    corner_radius = 5,
                    bg_color = '#242424')



########################################
        # Primeira Linha

botão_0.place(x = 4, y = 519)
botão_virgula.place(x = 204, y = 519)
botão_resultado.place(x = 304, y = 519)

########################################

########################################
        # Segunda Linha

botão_1.place(x = 4, y = 456)
botão_2.place(x = 104, y = 456)
botão_3.place(x = 204, y = 456)
botão_soma.place(x = 304, y = 456)

########################################

########################################
        # Terceira Linha

botão_4.place(x = 4, y = 393)
botão_5.place(x = 104, y = 393)
botão_6.place(x = 204, y = 393)
botão_subtra.place(x = 304, y = 393)

########################################

########################################
        # Quarta Linha

botão_7.place(x = 4, y = 330)
botão_8.place(x = 104, y = 330)
botão_9.place(x = 204, y = 330)
botão_multipli.place(x = 304, y = 330)

########################################

########################################
        # Quinta Linha

botão_ao_quadrado.place(x = 4, y = 267)
botão_raiz_quadrada.place(x = 204, y = 267)
botão_divisao.place(x = 304, y = 267)

########################################

########################################
        # Sexta Linha

botão_limpar.place(x = 4, y = 204)
botão_limpar_um_por_um.place(x = 304, y = 204)

########################################

##########################################
        # Precionas Botões Pelo Teclado

app.bind('0',lambda event:valor_botao_0())
app.bind('.',lambda event:virgula())
app.bind('=',lambda event:igual())

app.mainloop()