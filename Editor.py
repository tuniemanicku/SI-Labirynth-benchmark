import tkinter as tk
from Labyrinth import LABYRINTH_SIZE

def changeColor(x,y):
    if buttons[y][x][1] == 0:
        buttons[y][x][0].config(bg="red")
        buttons[y][x][1] = 1
    else:
        buttons[y][x][0].config(bg="white")
        buttons[y][x][1] = 0

def saveToFile(buttons):
    with open("save.txt", "w") as f:
        for row in buttons:
            line = ' '.join(str(cell[1]) for cell in row)  # Create a string like '0010110...'
            f.write(line + "\n")

def loadFromFile(buttons):
    try:
        with open("save.txt", "r") as f:
            lines = f.readlines()
            for y, line in enumerate(lines):
                values = line.strip().split()
                for x, val in enumerate(values):
                    value = int(val)
                    buttons[y][x][1] = value
                    color = "red" if value == 1 else "white"
                    buttons[y][x][0].config(bg=color)
    except FileNotFoundError:
        print("save.txt not found.")



root = tk.Tk()
root.geometry(f'{720}x{900}')
for i in range(LABYRINTH_SIZE):
    root.columnconfigure(i, weight=1)
    root.rowconfigure(i, weight=1)
root.rowconfigure(LABYRINTH_SIZE, weight=LABYRINTH_SIZE//10)

buttons = []
for y in range(LABYRINTH_SIZE):
    buttons.append([])
    for x in range(LABYRINTH_SIZE):
        button = tk.Button(root, bg="white", command=lambda x=x, y=y: changeColor(x, y))
        button.grid(row=y, column=x, sticky="news")
        buttons[y].append([button, 0])

saveButton = tk.Button(root, bg="gray", text="Save", command=lambda: saveToFile(buttons))
saveButton.grid(row=LABYRINTH_SIZE, column=LABYRINTH_SIZE//2)
loadButton = tk.Button(root, bg="gray", text="Load", command=lambda: loadFromFile(buttons))
loadButton.grid(row=LABYRINTH_SIZE, column=(LABYRINTH_SIZE//2) + 1)


root.mainloop()