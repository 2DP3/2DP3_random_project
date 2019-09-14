import random
import PySimpleGUI as Sg

participants_list = []
total_participants = Sg.PopupGetText("Enter Number of Participants: ")
layout_participants = []

for x in range(0, int(total_participants) + 1):
    layout_participants.append([Sg.Text("{}".format(x)), Sg.InputText("",
                                                            key="{}".format(x))])

layout_participants.append([Sg.Button("Choose", key="choose")])

main_window = Sg.Window("2DP3 Rand", layout = layout_participants)


while True:
    b, v = main_window.Read(timeout=100)

    if b == "choose":
        for x in range(0, int(total_participants) + 1):
            participants_list.append(x)
        Sg.Popup(v['{}'.format(random.choice(participants_list))])

    if b == "Exit":
        quit()

