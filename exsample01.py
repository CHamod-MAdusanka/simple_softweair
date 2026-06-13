import FreeSimpleGUI as FSGUI
FSGUI.popup("Hello world!", title = "My first desktop popup", button_color = "red", background_color="blue", text_color= "yellow")
FSGUI.popup(image = "nnn.png")
answer = FSGUI.popup_get_text("Who are you?")