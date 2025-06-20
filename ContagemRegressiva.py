import calendar
import datetime
import PySimpleGUI as sg


def dias_ate_chegada(chegada):
    hoje = datetime.date.today()
    evento = datetime.datetime.strptime(chegada, "%Y-%m-%d").date()

    if evento >= hoje:
        dias_restantes = (evento - hoje).days
        return dias_restantes
    else:
        return "O Giovanni chaga hoje!"

# Data do evento (formato: "YYYY-MM-DD")
data_chegada = "2024-09-03"
dias_restantes = dias_ate_chegada(data_chegada)

if isinstance(dias_restantes, int):
    print(f"Faltam {dias_restantes} dias para a chegada do Giovanni.")
else:
    print(dias_restantes)
	

layout = [
    [sg.Text('Faltam {dias_restantes} dias para a chegada do Giovanni.')],
    [sg.Button('Clique Aqui')]
]

window = sg.Window('Minha Primeira Janela').Layout(layout)

while True:
    event, values = window.Read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Clique Aqui':
        sg.Popup('Você clicou no botão!')

window.close()