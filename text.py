import tkinter

def send():
  input = text.get('1.0', 'end-1c')
  print(f"The user sent: {input}")
  print("It's working oooo")
window = tkinter.Tk()
window.title("text widget")
frame = tkinter.Frame(window,padx=10, pady=10)
frame.pack()

text = tkinter.Text(frame,background="blue",width=50, height=10)
text.grid(row=0, column=0, padx=5, pady=5)

button = tkinter.Button(frame, background="blue", command=send, text="Send comment")
button.grid(row=1,column=0, padx=5, pady=5)
window.mainloop()