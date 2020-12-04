import tkinter as tk
import time
from random import randint
import math
from PIL import Image, ImageTk


level = 2

window_width = 800
window_height = 600
vx = 0
vy = 0
x = 160
y = 110
global u, left_border, right_border, up_border, down_border, boss_3_x_size, boss_3_y_size, boss_2_x_size, boss_2_y_size, boss_1_x_size, boss_1_y_size, delta, boss_x0, boss_y0, boss_x0_2a, boss_y0_2a, boss_x0_2b, boss_y0_2b, boss_x0_2c, boss_y0_2c, bullet_x0,delete_point, character_lives_x0, character_lives_y0, character_lives_len, enemy_lives_x0, enemy_lives_y0, enemy_lives_len, character_size
u = 5
left_border = -10
right_border = 810
up_border = -10
down_border = 610
left_border_1 = 50
right_border_1 = 750
up_border_1 = 50
down_border_1 = 550
boss_3_x_size = 100
boss_3_y_size = 100
boss_2_x_size = 100
boss_2_y_size = 100
boss_1_x_size = 100
boss_1_y_size = 150
boss_x0_2a = 500
boss_y0_2a = 500
boss_x0_2b = 300
boss_y0_2b = 300
boss_x0_2c = 500 
boss_y0_2c = 100
boss_x0 = 500
boss_y0 = 300
bullet_x0 = 900
delete_point = 1000
delta = 20
enemy_lives_x0 = 420
enemy_lives_y0 = 570
enemy_lives_len = 299
character_lives_x0 =30
character_lives_y0 = 570
character_lives_len = 299
character_size = 50
space = 15

root = tk.Tk()

img_character = Image.open('boss_2.png')
img_character = img_character.resize((character_size, character_size), Image.ANTIALIAS)
img_character = ImageTk.PhotoImage(img_character)

if level == 1:
  img = ImageTk.PhotoImage(Image.open('level_2_background.jpg'))
if level == 2:
  img = ImageTk.PhotoImage(Image.open('level_3_background.jpg'))
if level == 3:
  img = ImageTk.PhotoImage(Image.open('level_1_background.png'))

canvas = tk.Canvas(root, width=window_width, height=window_height)
canvas.pack(side=tk.TOP)
canvas.create_image(0,0, image=img, anchor='nw')
character = canvas.create_image(x,y, image=img_character, anchor='nw')


def on_key_press(event):
    """ Функция обрабатывает события клавиатуры. Срабатывает при нажатии на кнопку
      Args:
      event - кнопка, которая была нажата
    """
    global vx, vy
    if event.keysym == 'Left':
        vx = -u
    elif event.keysym == 'Right':
        vx = u
    elif event.keysym == 'Up':
        vy = -u
    elif event.keysym == 'Down':
        vy = u
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
    if self.x > right_border or self.x < left_border:
      self.x = x
      self.y = y
      self.direction = self.c

      
  def destroying_bullet(self):
    """Функция удаляет пулю с экрана
    """
    self.x = delete_point
    self.r = 0
    self.bullet_move()

     

  def bullet_move(self):
    """Функция перемещает пулю по прошествии единицы времени.
    """
    if self.y != bullet_x0:
      if self.direction == 1:
        self.x += self.vx
      else:
        self.x -= self.vx
      canvas.coords(self.id, self.x -self.r, self.y - self.r , self.x + self.r, self.y + self.r)

    if self.y != bullet_x0:
      if self.direction == 1:
        self.y += self.vy
      else:
        self.y -= self.vy
      canvas.coords(self.id, self.x -self.r, self.y - self.r , self.x + self.r, self.y + self.r)


class boss():
  def __init__(self, x_boss, y_boss, x_size, y_size, img_boss):
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
    self.x_size = x_size
    self.y_size = y_size
    self.vx = 1
    self.vy = 1
    self.c = 0
    self.x_direction = 1
    self.y_direction = 1
    self.color = 'magenta4'
    self.id = canvas.create_image(self.x - int(self.x_size/2), self.y - int(self.y_size/2), image=img_boss, anchor='nw')


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
      if self.x < right_border_1 and self.x > left_border_1:
        self.x += self.vx
        canvas.move(self.id, self.vx, 0)
      else:
        self.change_x_direction()

    else:
      if self.x < right_border_1 and self.x > left_border_1:
        self.x -= self.vx
        canvas.move(self.id, -self.vx, 0)
      else:
        self.change_x_direction()

    if self.y_direction == 1:
      if self.y < down_border_1 and self.y > up_border_1:
        self.y += self.vy
        canvas.move(self.id, 0, self.vy)
      else:
        self.change_y_direction()

    else:
      if self.y < down_border_1 and self.y > up_border_1:
        self.y -= self.vy
        canvas.move(self.id, 0, -self.vy)
      else:
        self.change_y_direction()

    canvas.coords(self.id, self.x - int(self.x_size/2), self.y - int(self.y_size/2))


  def destroying_boss(self):
    """Функция удаляет побежденного врага с экрана
    """
    self.x = delete_point
    self.size = 0
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
    self.width = 10
    self.id = canvas.create_line(self.x, self.y, self.x + self.length,y_0, width=self.width, fill = self.color)


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
    self.x_size = 25
    self.y_size = 37
    self.vx = 3
    self.vy = 3
    self.x_direction = 1
    self.y_direction = 1
    self.id = canvas.create_image(self.x - int(self.x_size/2), self.y - int(self.x_size/2), image=img_mini_boss, anchor='nw')


def game_loop_1():
  """Главная функция первого уровня
  На первом уровне игрок сражается с одним главным противником, который время от времени призывает себе на помощь свою уменьшенную копию (время появления копий регулирутся параметром T4).
  Копия уничтожается после первого попадания в нее.
  Противники двигаются с изменяющейся случайным образом скоростью ( как по модулю так и по направлению) 
  Бой происходит по принципу перестрелки: спустя некоторое время, регулируемое параметром T3 противник и все его копии одновременн стреляют точно в игрока, поэтому чтобы успеть среагировать необходимо постоянно деражаться далеко от противника и его копий, стараться их уничтожать.
  """
  canvas.move(character, vx, vy)
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
  if ((B.x - boss_1.x)**2 + (B.y - boss_1.y)**2)**0.5 < boss_1.y_size and time.time() - T2 > 1 :
    enemy_lives.decrease(10)
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
  if time.time() - T4 > 15 and len(twins) != 0:
    a = randint(left_border_1, right_border_1)
    b = randint(up_border_1, down_border_1)
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
      character_lives.decrease(50)
      t[i] = time.time()

  for i in range(1, len(twins)):
    if ((twins[i].x - B.x)**2 + (twins[i].y - B.y)**2)**0.5 < twins[i].y_size:
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


def explosion(x_explosion, y_explosion, N, color, massive):
  """Функция инициализирует специфическую атаку врага - выстрел по всем направлениям ("взрыв")
  """
  shift = randint(0, 10)
  for i in range(N):
    massive.append(bullet(x_explosion, y_explosion, color))
    n = len(massive) - 1
    massive[n].vy = int(7*math.sin(shift + i*2*math.pi/N))
    massive[n].vx = int(7*math.cos(shift + i*2*math.pi/N))


def game_loop_2():
  """Главная функция второго уровня
  На втором уровне игроку приходится вести бой одновременно с тремя противниками, у которых появляется новый тип атаки - одновременный выстрел по разным направлениям.
  За время регулироемое параметром T3 один случайно выбранный противник производит эту атаку один раз. Направления обстрела и их количество выбираются случайным образом
  Чтобы увернуться от атаки нужно все время находится достаточно далеко от всех противников
  Для победы надо уничтожить всех трех противников
  """
  canvas.move(character, vx, vy)
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
    if ((B.x - bosses_2[i].x)**2 + (B.y - bosses_2[i].y)**2)**0.5 < bosses_2[i].y_size and time.time() - T2 > 1 :
      enemy_lives[i].decrease(30)
      T2 = time.time()

  global T3
  if time.time() - T3 > 5:
    if len(bosses_2) != 0:
      j = randint(-1,len(bosses_2) - 1)
      explosion(bosses_2[j].x, bosses_2[j].y, randint(20, 30), 'red', enemy_bullet_2)
    T3 = time.time()
    
  for b in enemy_bullet_2:
    b.bullet_move()
    if b.x > right_border or b.x < left_border or b.y < up_border or b.y > down_border:
      b.destroying_bullet()
      enemy_bullet_2.remove(b)

  global T5
  t = []
  for i in range(len(enemy_bullet_2)):
    t.append(T5)
  for i in range(len(enemy_bullet_2)):
    if ((enemy_bullet_2[i].x - x)**2 + (enemy_bullet_2[i].y - y)**2)**0.5 < 2*enemy_bullet_2[i].r and time.time() - t[i] > 1 :
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


def game_loop_3():
  """Главная функция третьего уровня
  На третьем уровне противник при каждом попадании в него делится на 2 новых меньшего размера и большей скорости, в которых труднее попасть. Деление происходит три раза и в конечном счете крупный противник последоательно распадается на 16 мелких, каждый из оставшихся 16 при попадании уничтожается
  """
  canvas.move(character, vx, vy)
  global x, y
  x += vx
  y += vy
  root.after(30, game_loop_3)
  B.bullet_move()
  for boss_3 in bosses_3:
    boss_3.boss_move()
    
  global T1
  if time.time() - T1 > 5:
    if len(bosses_3) != 0:
      j = randint(-1,len(bosses_3) -1)
      bosses_3[j].rotate() 
    T1 = time.time()

  global T2
  for i in range(len(bosses_3)):
    if ((B.x - bosses_3[i].x)**2 + (B.y - bosses_3[i].y)**2)**0.5 < bosses_3[i].y_size/2 and time.time() - T2 > 1 :
      enemy_lives.decrease(20)
      if bosses_3[i].y_size != boss_3_x_size - 3*delta:
        bosses_3[i].c += 1
        bosses_3[i].y_size -= delta
        bosses_3[i].x_size -= delta
        bosses_3.append(boss(bosses_3[i].x, bosses_3[i].y + delta/2, bosses_3[i].x_size, bosses_3[i].y_size, img_boss[bosses_3[i].c]))
        bosses_3.append(boss(bosses_3[i].x, bosses_3[i].y + delta/2, bosses_3[i].x_size, bosses_3[i].y_size, img_boss[bosses_3[i].c]))
        n = len(bosses_3)
        bosses_3[n - 1].c = bosses_3[i].c
        bosses_3[n - 2].c = bosses_3[i].c
        bosses_3[n-1].vx += 1
        bosses_3[n-2].y_direction = 0
        bosses_3[n-1].vy += 1
        bosses_3[n-2].vx += 1
        bosses_3[n-2].vy += 1
        bosses_3[i].destroying_boss()
        bosses_3.pop(i)
      else:
        bosses_3[i].destroying_boss()
        bosses_3.pop(i)
        break
      T2 = time.time()

  global T3
  if time.time() - T3 > 5:
    if len(bosses_3) != 0:
      j = randint(-1,len(bosses_3) - 1)
      explosion(bosses_3[j].x, bosses_3[j].y, randint(20, 30), 'cyan',enemy_bullet_3)
    T3 = time.time()
    
  for b in enemy_bullet_3:
    b.bullet_move()
    if b.x > right_border or b.x < left_border or b.y < up_border or b.y > down_border:
      b.destroying_bullet()
      enemy_bullet_3.remove(b)

  global T5
  t = []
  for i in range(len(enemy_bullet_3)):
    t.append(T5)
  for i in range(len(enemy_bullet_3)):
    if ((enemy_bullet_3[i].x - x)**2 + (enemy_bullet_3[i].y - y)**2)**0.5 < 2*enemy_bullet_3[i].r and time.time() - t[i] > 1 :
      character_lives.decrease(20)
      t[i] = time.time()
    
  if enemy_lives.length < 0:
    enemy_lives.length = 0
    enemy_lives.decrease(0)
    print('\n' + '\n' + 'Great! You have destroyed boss!' + '\n' + 'Congratulations' + '\n' + 'Level 3 complited')

  if character_lives.length < 0 :
    print('\n' + '\n' + 'You lost!' + '\n' + 'Better lack next time!')
    character_lives.length = 0
    for b in enemy_bullet_3:
      b.destroying_bullet()
    enemy_bullet_3.clear()
    for boss_3 in bosses_3:
      boss_3.destroying_boss()
    character_lives.decrease(0)


print('Управление:' + '\n' + 'Стрелки отвечают за перемещение персонажа' + '\n' + 'Выстрел - клавиша пробел' + '\n' + 'Поменять направление стрельбы (с права на лево и наоборот) - клавиша Enter')

T = time.time()
T1 = T2 = T3 = T4 = T5 = T
character_lives = health_indicator(character_lives_len, character_lives_x0, character_lives_y0, 'lawn green')
B = bullet(bullet_x0, bullet_x0, 'orange')

if level == 1:
  img_boss = Image.open('boss_1.jpg')
  img_boss = img_boss.resize((boss_1_x_size, boss_1_y_size), Image.ANTIALIAS)
  img_boss = ImageTk.PhotoImage(img_boss)
  img_mini_boss = Image.open('boss_1.jpg')
  img_mini_boss = img_mini_boss.resize((int(boss_1_x_size/2), int(boss_1_y_size/2)), Image.ANTIALIAS)
  img_mini_boss = ImageTk.PhotoImage(img_mini_boss)
  boss_1 = boss(boss_x0, boss_y0, boss_1_x_size, boss_1_y_size, img_boss)
  enemy_bullet = []
  enemy_bullet.append(bullet(bullet_x0, bullet_x0, 'red'))
  twins = []
  twins.append(boss_1)
  enemy_lives = health_indicator(enemy_lives_len, enemy_lives_x0, enemy_lives_y0, 'red')

if level == 2:
  bosses_2 = []
  img_boss = Image.open('boss_2.png')
  img_boss = img_boss.resize((boss_2_x_size, boss_2_y_size), Image.ANTIALIAS)
  img_boss = ImageTk.PhotoImage(img_boss)
  bosses_2.append(boss(boss_x0_2a, boss_y0_2a, boss_2_x_size, boss_2_y_size, img_boss))
  bosses_2.append(boss(boss_x0_2b, boss_y0_2b, boss_2_x_size, boss_2_y_size, img_boss))
  bosses_2.append(boss(boss_x0_2c, boss_y0_2c, boss_2_x_size, boss_2_y_size, img_boss))
  bosses_2[1].x_direction = 0
  bosses_2[2].y_direction = 0
  enemy_lives = []
  for i in range(3):
    enemy_lives.append(health_indicator(int(enemy_lives_len/2), enemy_lives_x0, enemy_lives_y0 - i*space, 'red'))
  enemy_bullet_2 = []

if level == 3:
  bosses_3 = []
  img_b = Image.open('boss_2.png')
  img_sizes = []
  img_boss = []
  for i in range(4):
    img_sizes.append(img_b.resize((boss_3_x_size - i*delta, boss_3_y_size - i*delta), Image.ANTIALIAS))
    img_boss.append(ImageTk.PhotoImage(img_sizes[i]))
  bosses_3.append(boss(boss_x0, boss_y0, boss_3_x_size, boss_3_y_size, img_boss[0]))
  enemy_lives = health_indicator(enemy_lives_len, enemy_lives_x0, enemy_lives_y0, 'red')
  enemy_bullet_3 = []
  

root.bind('<Key>', on_key_press)
root.bind('<KeyRelease>', on_key_release)
num = 0


if level == 1:
  game_loop_1()
if level == 2:
  game_loop_2()
if level == 3:
  game_loop_3()
root.mainloop()