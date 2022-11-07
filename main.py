from tkinter import *
from tkinter import ttk

# Importando tkcalendar

from tkcalendar import Calendar, DateEntry

# Importando Dateutil
from dateutil.relativedelta import relativedelta

# Importando datetime

from datetime import date


# Criando janela

janela = Tk()
janela.title('Calculadora Idade')
janela.geometry('310x400')

# Corres

cor1 = '#3b3b3b'
cor2 = '#000000'
cor3 =  '#FFFFFF'
cor4 = "#fcc058"  # orange / laranja
cor5 = '#FF0000'

# Criando frames
frame_cima = Frame(janela, width =310, height=140, pady = 0, relief = FLAT, bg = cor2 )
frame_cima.grid(row = 0, column = 0)

frame_baixo = Frame(janela, width =310, height=260, pady = 0, relief = FLAT, bg = cor1 )
frame_baixo.grid(row = 1, column = 0)




# Criando labels para frame cima

TXT_calculadora = Label(frame_cima, text = 'CALCULADORA', width= 25, height= 1, padx=3, relief= 'flat', anchor='center', font=('Ivy 15 bold'), bg = cor2, fg = cor3)
TXT_calculadora.place(x = 0, y=30)
TXT_idade = Label(frame_cima, text = 'DE IDADE', width= 25, height= 1, padx=3, relief= 'flat', anchor='center', font=('Ivy 15 bold'), bg = cor2, fg = cor4)
TXT_idade.place(x = 0, y=70)



# Agora vamos também criar alguns Labels e Botões no Frame de baixo

txt_data_inicial = Label(frame_baixo, text='Data inicial', height=1, pady = 0, padx = 0, relief = 'flat', anchor = NW, font = ('Ivy 11'), bg = cor1, fg = cor3)
txt_data_inicial.place(x=50,y=30)

cal_1 = DateEntry(frame_baixo, width = 13, background = 'darkblue', foreground = 'white', borderwidht = 2, date_pattern = 'mm/dd/y', year = 2022)
cal_1.place(x=170, y=30)

txt_data_nasci = Label(frame_baixo, text = 'Data nascimento', height=1, pady = 0, padx= 0, relief='flat', anchor= NW, font = ('Ivy 11'), bg = cor1, fg = cor3 )
txt_data_nasci.place(x=50,y=60)

cal_2 = DateEntry(frame_baixo, width = 13, background = 'darkblue', foreground = 'white', borderwidth=2, date_pattern = 'mm/dd/y', year = 2022)
cal_2.place(x=170, y=60)


# Criando label para o resultado

n_anos = Label(frame_baixo, text = '', height=1, padx=0, relief = 'flat', anchor = 'center', font = ('Ivy 25 bold'), bg = cor1, fg=cor3)
n_anos.place(x=60,y=135)


n_meses = Label(frame_baixo, text = '', height =1, padx = 0, relief = 'flat', anchor ='center', font = ('Ivy 20 bold'), bg = cor1, fg = cor3)
n_meses.place(x=135, y =135)



n_dia = Label(frame_baixo, text = '', height =1, padx = 0, relief = 'flat', anchor ='center', font = ('Ivy 20 bold'), bg = cor1, fg = cor3)
n_dia.place(x=215, y =135)

erro = Label(frame_baixo, text = '', height =1, padx = 0, relief = 'flat', anchor ='center', font = ('Ivy 11 bold'), bg = cor1, fg = cor5)
erro.place(x=30, y=175)


# Para obter os valores do Combobox, temos que fazer o seguinte

inicial = cal_1.get()
termino = cal_2.get()

# Criando uma função para calcular idade

def calcular():

    inicial = cal_1.get()
    termino = cal_2.get()

    # Separando os valores e atribuindo em variaveis diferentes
    mes_1, dia_1, ano_1 = [int(f) for f in inicial.split('/')]

    # Convertendo os valores em formato datetime
    data_inicial = date(ano_1, mes_1, dia_1)

    # Separando os valores e atribuindo em variaveis diferentes
    mes_2, dia_2, ano_2 = [int(f) for f in termino.split('/')]

    # Convertendo os valores em formato datetime
    
    data_nascimento = date(ano_2, mes_2, dia_2)

    if data_nascimento > data_inicial:
       erro['text'] = 'Por favor, colocar uma data valida!'

    else:
        erro['text'] = ''
        t_anos = Label(frame_baixo, text = 'anos', height=1, padx=0, relief = 'flat', anchor = 'center', font = ('Ivy 11 bold'), bg = cor1, fg=cor3)
        t_anos.place(x=50,y=175)
        t_meses = Label(frame_baixo, text = 'meses', height =1, padx = 0, relief = 'flat', anchor ='center', font = ('Ivy 11 bold'), bg = cor1, fg = cor3)
        t_meses.place(x=120, y =175)    
        t_dia = Label(frame_baixo, text = 'dias', height =1, padx = 0, relief = 'flat', anchor ='center', font = ('Ivy 11 bold'), bg = cor1, fg = cor3)
        t_dia.place(x=210, y =175)
        anos = relativedelta(data_inicial, data_nascimento).years   
        meses = relativedelta(data_inicial, data_nascimento).months    
        dias = relativedelta(data_inicial, data_nascimento).days


    print(anos)
    print(meses)
    print(dias)

    n_anos['text'] = anos 
    n_meses['text'] = meses
    n_dia['text'] = dias 
    

# Criando botão calcular

b_age = Button(frame_baixo, command=calcular, text='Calcular idade', width=20, height= 1, bg=cor1, fg=cor3, font = ('Ivy 10 bold'), relief = RAISED, overrelief= RIDGE)
b_age.place(x=60, y=225)



janela.mainloop() 