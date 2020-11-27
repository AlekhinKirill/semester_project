import tkinter as tk
import time
from random import randint
import math


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



def on_key_press(event):
    """ Функция обрабатывает события клавиатуры. Срабатывает при нажатии на кнопку
      Args:
      event - кнопка, которая была нажата
    """
    global vx, vy
    if event.keysym == 'Left':
        vx = -5
    elif event.keysym == 'Right':
        vx = 5
    elif event.keysym == 'Up':
        vy = -5
    elif event.keysym == 'Down':
        vy = 5
    elif event.keysym == 'space':
        B.fire()
    elif event.keysym == 'Return':
        B.change_direction()



def on_key_release(event):
    """ Функция обрабатывает события клавиатуры. Срабатывает при отпускании кнопки
      Args:
      event - кнопка, которая была отжата
    """
    global vx, vy
    if event.keysym in ('Left', 'Right'):
        vx = 0
    elif event.keysym in ('Up', 'Down'):
        vy = 0


class bullet():
  def __init__(self, bullet_x, bullet_y, color):
    """ Конструктор класса bullet
    Args:
    x(int) - начальное положение по горизонтали
    y(int) - начальное положение по вертикали
    r(int) - радиус
    vx(int) - скорость по оси x
    vy(int) - скорость по оси y
    direction{0, 1} - направление полета пули(0 - влево, 1 - вправо)
    """
    self.x = bullet_x
    self.y = bullet_y
    self.r = 5
    self.vx = 15
    self.vy = 0
    self.direction = 1
    self.c = 1
    self.color = color
    self.id = canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=self.color)


  def change_direction(self):
    """ Функция изменяет направление стрельбы на противоположное
    """
    if self.direction == 1:
      self.c = 0
    else:
      self.c = 1

  
  def fire(self):
    """Функция инициализирует выстрел
    """
    if self.x > 810 or self.x < -10:
      self.x = x
      self.y = y
      self.direction = self.c

      
  def destroying_bullet(self):
    """Функция удаляет пулю с экрана
    """
    self.x = 1000
    self.r = 0
    self.bullet_move()

     

  def bullet_move(self):
    """Функция перемещает пулю по прошествии единицы времени.
    """
    if self.y != 900:
      if self.direction == 1:
        self.x += self.vx
      else:
        self.x -= self.vx
      canvas.coords(self.id, self.x -self.r, self.y - self.r , self.x + self.r, self.y + self.r)

    if self.y != 900:
      if self.direction == 1:
        self.y += self.vy
      else:
        self.y -= self.vy
      canvas.coords(self.id, self.x -self.r, self.y - self.r , self.x + self.r, self.y + self.r)


class boss():
  def __init__(self, x_boss, y_boss, color):
    """ Конструктор класса boss
    Args:
    x(int) - начальное положение по горизонтали
    y(int) - начальное положение по вертикали
    r(int) - радиус
    vy(int) - скорость по оси x
    vy(int) - скорость по оси y
    x_direction{0, 1} - направление движение по горизонтали(0 - влево, 1 - вправо)
    y_direction{0, 1} - направление движение по вертикали(0 - вниз, 1 - вверх)
    color - цвет
    """
    self.x = x_boss
    self.y = y_boss
    self.r = 20
    self.vx = 1
    self.vy = 1
    self.x_direction = 1
    self.y_direction = 1
    self.color = color
    self.id = canvas.create_oval(
              self.x - self.r,
              self.y - self.r,
              self.x + self.r,
              self.y + self.r,
              fill=self.color
      )


  def change_x_direction(self):
    """ Функция изменяет направление движения по горизонтали на противоположное
    """
    if self.x_direction == 1:
      self.x_direction = 0
      self.x = self.x - 2*self.vx

    else:
      self.x_direction = 1
      self.x = self.x + 2*self.vx


  def change_y_direction(self):
    """ Функция изменяет направление движения по вертикали на противоположное
    """
    if self.y_direction == 1:
      self.y_direction = 0
      self.y = self.y - 2*self.vy

    else:
      self.y_direction = 1
      self.y = self.y + 2*self.vy

  def boss_move(self):
    """Функция перемещает врага по прошествии единицы времени.
    """
    if self.x_direction == 1:
      if self.x < 750 and self.x > 50:
        self.x += self.vx
      else:
        self.change_x_direction()

    else:
      if self.x < 750 and self.x > 50:
        self.x -= self.vx
      else:
        self.change_x_direction()

    if self.y_direction == 1:
      if self.y < 550 and self.y > 50:
        self.y += self.vy
      else:
        self.change_y_direction()

    else:
      if self.y < 550 and self.y > 50:
        self.y -= self.vy
      else:
        self.change_y_direction()

    canvas.coords(self.id, self.x -self.r, self.y - self.r , self.x + self.r, self.y + self.r)


  def destroying_boss(self):
    """Функция удаляет побежденного врага с экрана
    """
    self.x = 1000
    self.r = 0
    self.boss_move()
     

  def rotate(self):
    """Функция меняет характер движения врага
    """
    self.x_direction = randint(0,2)
    self.vx = randint(1,3)
    self.vy = randint(1,3)
    self.x_direction = randint(0,2)


class health_indicator():
  def __init__(self, length, x_0, y_0, color):
    """ Конструктор класса health_indicator
    Args:
    x(int) - положение левого края по горизонтали
    y(int) - положение по вертикали
    length(int) - длина полосы
    vy(int) - скорость по оси x
    vy(int) - скорость по оси y
    color - цвет
    """
    self.length = length
    self.x = x_0
    self.y = y_0
    self.color = color
    self.id = canvas.create_line(self.x, self.y, self.x + self.length,y_0, width=10, fill = self.color)


  def decrease(self, d):
    """Функция изменяет длину индикатора
    Параметры:
    d(int) - величина измениния длины
    """
    self.length -= d
    canvas.coords(self.id, self.x, self.y, self.x + self.length,self.y)


class mini_twins(boss):
  def __init__(self, x_mini, y_mini):
    """ Конструктор класса mini_boss - двойников осного босса появляющихся раз в 30 секунд и уничтожающихся после первого попадания
    Args:
    x(int) - начальное положение по горизонтали
    y(int) - начальное положение по вертикали
    r(int) - радиус
    vx(int) - скорость по оси x
    vy(int) - скорость по оси y
    x_direction{0, 1} - направление движение по горизонтали(0 - влево, 1 - вправо)
    y_direction{0, 1} - направление движение по вертикали(0 - вниз, 1 - вверх)
    color - цвет
    """
    self.x = x_mini
    self.y = y_mini
    self.r = 20
    self.vx = 3
    self.vy = 3
    self.x_direction = 1
    self.y_direction = 1
    self.id = canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill='green4')




def game_loop_1():
  """Главная функция первого уровня
  """
  for thing in character:
    canvas.move(thing, vx, vy)
  global x, y
  x += vx
  y += vy
  root.after(30, game_loop_1)
  B.bullet_move()
  boss_1.boss_move()
    
  global T1
  if time.time() - T1 > 5:
    boss_1.rotate() 
    T1 = time.time()

  global T2
  if ((B.x - boss_1.x)**2 + (B.y - boss_1.y)**2)**0.5 < boss_1.r and time.time() - T2 > 1 :
    enemy_lives.decrease(30)
    T2 = time.time()
    
  global T3
  if time.time() - T3 > 6:
    for i in range(len(twins)):
      enemy_bullet[i].x = twins[i].x
      enemy_bullet[i].y = twins[i].y
      enemy_bullet[i].vx = 15*(x - twins[i].x)/((x - twins[i].x)**2 + (y - twins[i].y)**2)**0.5
      enemy_bullet[i].vy = 15*(y - twins[i].y)/((x - twins[i].x)**2 + (y - twins[i].y)**2)**0.5
    T3 = time.time()
  for b in enemy_bullet:
    b.bullet_move()
    
  global T4
  if time.time() - T4 > 30 and len(twins) != 0:
    a = randint(30, 730)
    b = randint(30, 520)
    twins.append(mini_twins(a, b))
    enemy_bullet.append(bullet(a, b, 'red'))
    T4 = time.time()
  for m in twins:
    m.boss_move()

  global T5
  t = []
  for i in range(len(enemy_bullet)):
    t.append(T5)
  for i in range(len(enemy_bullet)):
    if ((enemy_bullet[i].x - x)**2 + (enemy_bullet[i].y - y)**2)**0.5 < 10 and time.time() - t[i] > 1 :
      character_lives.decrease(30)
      t[i] = time.time()

  for i in range(1, len(twins)):
    if ((twins[i].x - B.x)**2 + (twins[i].y - B.y)**2)**0.5 < twins[i].r:
      twins[i].destroying_boss()
      enemy_bullet[i].destroying_bullet()
      del twins[i]
      del enemy_bullet[i]
      break
    

  if enemy_lives.length <= 0 and len(twins) !=0:
    print('\n' + '\n' + 'Great! You have destroyed boss!' + '\n' + 'Congratulations' + '\n' + 'Level 1 complited')
    enemy_lives.length = 0
    for m in twins:
      m.destroying_boss()
    twins.clear()

  if character_lives.length <= 0 and len(twins) !=0:
    print('\n' + '\n' + 'You lost!' + '\n' + 'Better lack next time!')
    character_lives.length = 0
    for b in enemy_bullet:
      b.destroying_bullet()
    enemy_bullet.clear()
    for m in twins:
      m.destroying_boss()
    twins.clear()






def explosion(x_explosion, y_explosion, N):
  """Функция инициализирует специфическую атаку врага - выстрел по всем направлениям ("взрыв")
  """
  shift = randint(0, 10)
  for i in range(N):
    enemy_bullet_2.append(bullet(x_explosion, y_explosion, 'red'))
    n = len(enemy_bullet_2) - 1
    enemy_bullet_2[n].vy = int(7*math.sin(shift + i*2*math.pi/N))
    enemy_bullet_2[n].vx = int(7*math.cos(shift + i*2*math.pi/N))


def game_loop_2():
  """Главная функция второго уровня
  """
  for thing in character:
    canvas.move(thing, vx, vy)
  global x, y
  x += vx
  y += vy
  root.after(30, game_loop_2)
  B.bullet_move()
  for boss_2 in bosses_2:
    boss_2.boss_move()
    
  global T1
  if time.time() - T1 > 5:
    if len(bosses_2) != 0:
      j = randint(-1,len(bosses_2) -1)
      bosses_2[j].rotate() 
    T1 = time.time()

  global T2
  for i in range(len(bosses_2)):
    if ((B.x - bosses_2[i].x)**2 + (B.y - bosses_2[i].y)**2)**0.5 < bosses_2[i].r and time.time() - T2 > 1 :
      enemy_lives[i].decrease(30)
      T2 = time.time()

  global T3
  if time.time() - T3 > 5:
    if len(bosses_2) != 0:
      j = randint(-1,len(bosses_2) - 1)
      explosion(bosses_2[j].x, bosses_2[j].y, randint(20, 30))
    T3 = time.time()
    
  for b in enemy_bullet_2:
    b.bullet_move()
    if b.x > 810 or b.x < -10 or b.y < -10 or b.y > 610:
      b.destroying_bullet()
      enemy_bullet_2.remove(b)

  global T5
  t = []
  for i in range(len(enemy_bullet_2)):
    t.append(T5)
  for i in range(len(enemy_bullet_2)):
    if ((enemy_bullet_2[i].x - x)**2 + (enemy_bullet_2[i].y - y)**2)**0.5 < 10 and time.time() - t[i] > 1 :
      character_lives.decrease(50)
      t[i] = time.time()
    
  for i in range(len(enemy_lives)):
    global num
    if enemy_lives[i].length < 0:
      num = num + 1
      if num == 3:
        print('\n' + '\n' + 'Great! You have destroyed boss!' + '\n' + 'Congratulations' + '\n' + 'Level 2 complited')
      enemy_lives[i].length = 0
      bosses_2[i].destroying_boss()
      enemy_lives[i].decrease(0)
      enemy_lives.pop(i)
      bosses_2.pop(i)
      break

  if character_lives.length < 0 :
    print('\n' + '\n' + 'You lost!' + '\n' + 'Better lack next time!')
    character_lives.length = 0
    for b in enemy_bullet_2:
      b.destroying_bullet()
    enemy_bullet_2.clear()
    for boss_2 in bosses_2:
      boss_2.destroying_boss()
    character_lives.decrease(0)





level = 2

print('Управление:' + '\n' + 'Стрелки отвечают за перемещение персонажа' + '\n' + 'Выстрел - клавиша пробел' + '\n' + 'Поменять направление стрельбы (с права на лево и наоборот) - клавиша Enter')

T = time.time()
T1 = T
T2 = T
T3 = T
T4 = T
T5 = T
character_lives = health_indicator(299, 30, 570, 'lawn green')
B = bullet(900, 900, 'orange')

if level == 1:
  boss_1 = boss(500, 500, 'green2')
  enemy_bullet = []
  enemy_bullet.append(bullet(900, 900, 'red'))
  twins = []
  twins.append(boss_1)
  enemy_lives = health_indicator(299, 420, 570, 'red')

if level == 2:
  bosses_2 = []
  bosses_2.append(boss(500, 500, 'magenta4'))
  bosses_2.append(boss(300, 300, 'magenta4'))
  bosses_2.append(boss(500, 100, 'magenta4'))
  bosses_2[1].x_direction = 0
  bosses_2[2].y_direction = 0
  enemy_lives = []
  for i in range(3):
    enemy_lives.append(health_indicator(159, 420, 570 - i*15, 'red'))
  enemy_bullet_2 = []

root.bind('<Key>', on_key_press)
root.bind('<KeyRelease>', on_key_release)
num = 0


if level == 1:
  game_loop_1()
if level == 2:
  game_loop_2()
root.mainloop()