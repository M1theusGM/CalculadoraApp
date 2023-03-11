from tkinter import *
from customtkinter import *
from numpy import sqrt

#####################################

        # Tela da aplicação

app = CTk()

app.title('Calculator')

app.geometry('405x583+700+200')

app.resizable(width=False, height=False)

CTk._set_appearance_mode(app,'dark')

app.iconbitmap('CalculadoraApp/Imagens/Calculator.ico')


#####################################
             # Funções 

def calcular_ao_quadrado():
        valor = label_resultados.get()  
        valor = int(valor)
        calculo = valor ** 2
        resultado.set(calculo)

def calcular_raiz_quadrada():
        valor = label_resultados.get()
        
        valor_inteiro = int(valor)

        raiz = sqrt(valor_inteiro)
        raiz_valor_str = str(raiz)
        procurar_ponto = raiz_valor_str.find('.')

        if '.0' in raiz_valor_str:

                str_raiz_atualizada = raiz_valor_str[:procurar_ponto] 
                resultado.set(int(str_raiz_atualizada))

        else:
                resultado.set(float(raiz_valor_str))


def mostrar_valores(valor):
        global posição
        global equação
        equação += valor
        
        label_resultados.insert(posição,valor)
        posição += 1
       
# função para limpar o conteúdo digitado na caixa de texto
def limpar_conteudo():
  
  # limpamos o conteúdo da caixa de texto Entry
  nova_string = label_resultados.get()
  nova_string = nova_string[:-1]
  text_atualizado = nova_string
  
  label_resultados.delete(0, END)
  label_resultados.insert(0,text_atualizado)

def limpar_tudo():
        label_resultados.delete(0,END)

def calcular_resultado():
    # Cria uma lista vazia para armazenar os valores e operadores da expressão
    lista_expressoes = []
    # Obtém a expressão atual da Entry
    expressao = resultado.get()

    # Verifica se a expressão não está vazia
    if expressao:
        expressao_atual = ''
        # Percorre cada caractere da expressão
        for caracter in expressao:
            # Se o caractere é um dígito ou um ponto, adiciona ao valor atual
            if caracter.isdigit() or caracter == ".":
                expressao_atual += caracter
            # Se o caractere é um operador, adiciona o valor atual à lista e adiciona o operador à lista
            else:
                if expressao_atual:
                    if '.' in expressao_atual:
                        lista_expressoes.append(float(expressao_atual))
                    else:
                        lista_expressoes.append(int(expressao_atual))
                expressao_atual = ""
                lista_expressoes.append(caracter)
        # Adiciona o último valor atual à lista, se houver algum
        if expressao_atual:
            lista_expressoes.append(float(expressao_atual))

    # Se a lista tiver pelo menos três elementos, realiza o cálculo
    if len(lista_expressoes) >= 3:
        resultado_value = lista_expressoes[0]
        # Percorre a lista na ordem em que os itens foram inseridos e realiza o cálculo
        for i in range(1, len(lista_expressoes), 2):
            operador = lista_expressoes[i]
            operando = lista_expressoes[i+1]
            if operador == "+":
                resultado_value += operando
            elif operador == "-":
                resultado_value -= operando
            elif operador == "*":
                resultado_value *= operando
            elif operador == "/":
                resultado_value /= operando
        # Define o resultado como uma string e atualiza a variável de controle (StringVar) 'resultado'
        resultado.set("{:.0f}".format(resultado_value) if resultado_value.is_integer() else "{:.1f}".format(resultado_value))

def validacao_valores(valor):
    valores_permitidos = "0123456789+-*/."
    for caracter in valor:
        if caracter not in valores_permitidos:
            return False
    return True

######################################
        # variaveis

validacao = app.register(validacao_valores)
posição = 0
equação = ''
resultado = StringVar(value="")

######################################

######################################

            # Elementos

label_resultados = CTkEntry(app,
                            width = 398,
                            height = 10,
                            justify = 'right',
                            font = ('arial bold', 45),
                            fg_color = '#242424',
                            border_color = '#242424',
                            text_color = '#eaebea',
                            corner_radius = -1,
                            validatecommand=(validacao, '%P'),
                            validate="key",
                            textvariable = resultado)

botão_0 = CTkButton(app,
                    text = '0',
                    fg_color = '#FE8100',
                    command = lambda: mostrar_valores('0'),
                    width = 198,
                    height = 60,
                    font = ('arial bold',20),
                    corner_radius = 5,
                    bg_color = '#242424')

botão_1 = CTkButton(app,
                    text = '1',
                    fg_color = '#FE8100',
                    command = lambda: mostrar_valores('1'),
                    width = 98,
                    height = 60,
                    font = ('arial bold',20),
                    corner_radius = 5,
                    bg_color = '#242424')

botão_2 = CTkButton(app,
                    text = '2',
                    fg_color = '#FE8100',
                    command = lambda: mostrar_valores('2'),
                    width = 98,
                    height = 60,
                    font = ('arial bold',20),
                    corner_radius = 5,
                    bg_color = '#242424')

botão_3 = CTkButton(app,
                    text = '3',
                    fg_color = '#FE8100',
                    command = lambda: mostrar_valores('3'),
                    width = 98,
                    height = 60,
                    font = ('arial bold',20),
                    corner_radius = 5,
                    bg_color = '#242424')

botão_4 = CTkButton(app,
                    text = '4',
                    fg_color = '#FE8100',
                    command = lambda: mostrar_valores('4'),
                    width = 98,
                    height = 60,
                    font = ('arial bold',20),
                    corner_radius = 5,
                    bg_color = '#242424')

botão_5 = CTkButton(app,
                    text = '5',
                    fg_color = '#FE8100',
                    command = lambda: mostrar_valores('5'),
                    width = 98,
                    height = 60,
                    font = ('arial bold',20),
                    corner_radius = 5,
                    bg_color = '#242424')

botão_6 = CTkButton(app,
                    text = '6',
                    fg_color = '#FE8100',
                    command = lambda: mostrar_valores('6'),
                    width = 98,
                    height = 60,
                    font = ('arial bold',20),
                    corner_radius = 5,
                    bg_color = '#242424')

botão_7 = CTkButton(app,
                    text = '7',
                    fg_color = '#FE8100',
                    command = lambda: mostrar_valores('7'),
                    width = 98,
                    height = 60,
                    font = ('arial bold',20),
                    corner_radius = 5,
                    bg_color = '#242424')

botão_8 = CTkButton(app,
                    text = '8',
                    fg_color = '#FE8100',
                    command = lambda: mostrar_valores('8'),
                    width = 98,
                    height = 60,
                    font = ('arial bold',20),
                    corner_radius = 5,
                    bg_color = '#242424')

botão_9 = CTkButton(app,
                    text = '9',
                    fg_color = '#FE8100',
                    command = lambda: mostrar_valores('9'),
                    width = 98,
                    height = 60,
                    font = ('arial bold',20),
                    corner_radius = 5,
                    bg_color = '#242424')

botão_ponto = CTkButton(app,
                    text = '.',
                    fg_color = '#FE8100',
                    command = lambda: mostrar_valores('.'),
                    width = 98,
                    height = 60,
                    font = ('arial bold',20),
                    corner_radius = 5,
                    bg_color = '#242424')

botão_resultado = CTkButton(app,
                    text = '=',
                    fg_color = '#FE8100',
                    command = lambda: calcular_resultado(),
                    width = 98,
                    height = 60,
                    font = ('arial bold',20),
                    corner_radius = 5,
                    bg_color = '#242424')

botão_soma = CTkButton(app,
                    text = '+',
                    fg_color = '#FE8100',
                    command = lambda: mostrar_valores('+'),
                    width = 98,
                    height = 60,
                    font = ('arial bold',20),
                    corner_radius = 5,
                    bg_color = '#242424')

botão_subtra = CTkButton(app,
                    text = '-',
                    fg_color = '#FE8100',
                    command = lambda: mostrar_valores('-'),
                    width = 98,
                    height = 60,
                    font = ('arial bold',20),
                    corner_radius = 5,
                    bg_color = '#242424')

botão_multipli = CTkButton(app,
                    text = 'x',
                    fg_color = '#FE8100',
                    command = lambda: mostrar_valores('*'),
                    width = 98,
                    height = 60,
                    font = ('arial bold',20),
                    corner_radius = 5,
                    bg_color = '#242424')

botão_divisao = CTkButton(app,
                    text = '÷',
                    fg_color = '#FE8100',
                    command = lambda: mostrar_valores('/'),
                    width = 98,
                    height = 60,
                    font = ('arial bold',20),
                    corner_radius = 5,
                    bg_color = '#242424')

botão_limpar = CTkButton(app,
                    text = 'CE',
                    fg_color = '#FE8100',
                    command = lambda: limpar_tudo(),
                    width = 298,
                    height = 60,
                    font = ('arial bold',20),
                    corner_radius = 5,
                    bg_color = '#242424')

botão_ao_quadrado = CTkButton(app,
                    text = 'x²',
                    fg_color = '#FE8100',
                    command = lambda: calcular_ao_quadrado(),
                    width = 198,
                    height = 60,
                    font = ('arial bold',20),
                    corner_radius = 5,
                    bg_color = '#242424')

botão_raiz_quadrada = CTkButton(app,
                    text = '²√x',
                    fg_color = '#FE8100',
                    command = lambda: calcular_raiz_quadrada(),
                    width = 98,
                    height = 60,
                    font = ('arial bold',20),
                    corner_radius = 5,
                    bg_color = '#242424')

botão_limpar_um_por_um = CTkButton(app,
                    text = '⌫',
                    fg_color = '#FE8100',
                    command = lambda: limpar_conteudo(),
                    width = 98,
                    height = 60,
                    font = ('arial bold',20),
                    corner_radius = 5,
                    bg_color = '#242424')

########################################
        # Primeira Linha

label_resultados.place(x = 4, y = 85)
botão_0.place(x = 4, y = 519)
botão_ponto.place(x = 204, y = 519)
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
        # Precionar Botões Pelo Teclado

# numeros vinculados ao teclado
app.bind('0',lambda event:mostrar_valores('0'))
app.bind('1', lambda event: mostrar_valores('1'))
app.bind('2', lambda event: mostrar_valores('2'))
app.bind('3', lambda event: mostrar_valores('3'))
app.bind('4', lambda event: mostrar_valores('4'))
app.bind('5', lambda event: mostrar_valores('5'))
app.bind('6', lambda event: mostrar_valores('6'))
app.bind('7', lambda event: mostrar_valores('7'))
app.bind('8', lambda event: mostrar_valores('8'))
app.bind('9', lambda event: mostrar_valores('9'))


app.bind('.',lambda event: mostrar_valores('.'))
app.bind('<Return>',lambda event: calcular_resultado())
app.bind('<BackSpace>', lambda event: limpar_conteudo())

#expressoes
app.bind('+', lambda event: mostrar_valores('+'))
app.bind('-', lambda event: mostrar_valores('-'))
app.bind('/', lambda event: mostrar_valores('/'))
app.bind('*', lambda event: mostrar_valores('*'))

# desliga os binds se a entry estiver selecionada
def desativar_binds(event):
        app.unbind('0')
        app.unbind('1')
        app.unbind('2')
        app.unbind('3')
        app.unbind('4')
        app.unbind('5')
        app.unbind('6')
        app.unbind('7')
        app.unbind('8')
        app.unbind('9')
        app.unbind('.')
        app.unbind('+')
        app.unbind('-')
        app.unbind('/')
        app.unbind('*')
        app.unbind('<BackSpace>')


label_resultados.bind('<FocusIn>', desativar_binds)

app.mainloop()