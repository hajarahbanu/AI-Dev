import FreeSimpleGUI as gui

labe1 = gui.Text("Enter feet: ")
input1 = gui.Input()

labe2 = gui.Text("Enter inches: ")
input2 = gui.Input()

button = gui.Button("CONVERT")

window = gui.Window("Convertor", layout= [[labe1,input1], 
                    [labe2,input2],
                    [button]])

window.read()
window.close()