text = "id:123456"
text_input = "id:" + input("Введите id номер: ")
text_id= text_input[3:]
if text_id.isdigit():
    print("Введено верно", text_input)
else:
    print("Error")
