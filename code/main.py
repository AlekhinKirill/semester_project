import tkinter as tk
import level_1


window_width = 800
window_height = 600
root = tk.Tk()
canvas = tk.Canvas(root, width=window_width, height=window_height, bg="black")
canvas.pack(side=tk.TOP)
character = []
x = 160
y = 110
character.append(canvas.create_oval((150, 100, 170, 120), fill='yellow'))
character.append(canvas.create_oval((155, 105, 165, 115), fill='red'))
vx = 0
vy = 0

print('Управление:' + '\n' + 'Стрелки отвечают за перемещение персонажа' + '\n' + 'Выстрел - клавиша пробел' + '\n' + 'Поменять направление стрельбы (с права на лево и наоборот) - клавиша Enter')


root.bind('<Key>', level_1.on_key_press)
root.bind('<KeyRelease>', level_1.on_key_release)

level_1.game_loop_1()
root.mainloop()