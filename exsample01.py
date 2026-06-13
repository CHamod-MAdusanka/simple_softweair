import FreeSimpleGUI as FSGUI
FSGUI.popup("Hello world!", title = "My first desktop popup", button_color = "red", background_color="blue", text_color= "yellow")
FSGUI.popup(image = "nnn.png")
answer = FSGUI.popup_get_text("Who are you?",title = "name", button_color = "red", background_color="blue", text_color= "yellow")

def popup_get_choice(options, title = "Make a Choice"):
    layout = [[FSGUI.Listbox(options, size=(30, None), key="-LISTBOX-")],
            [FSGUI.Button('Ok'), FSGUI.Button('Cancel')]]
    event, values = FSGUI.Window(title, layout).read(close=True)

    if event == "Ok":
        try:
            return values["-LISTBOX-"][0]
        except:
            return None
    else:
        return None

# Use something similar to the following when using the popup_get_choice function
subjects = ["English", "Math", "Computer Science", "History", "Phys Ed"]
favourite = popup_get_choice(subjects)