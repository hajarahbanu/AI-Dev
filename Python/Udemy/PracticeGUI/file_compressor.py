import FreeSimpleGUI as gui

label1 = gui.Text("Select Files to compress: ")
input1 = gui.Input()
button1 = gui.FilesBrowse()

label2 = gui.Text("Select Destination Folder: ")
input2 = gui.Input()
button2 = gui.FolderBrowse()


compress_button = gui.Button("Compress Files")

window = gui.Window("FILES COMPRESSOR", layout=[[label1, input1, button1],
                                                [label2, input2, button2],
                                                [compress_button]])

window.read()
window.close()