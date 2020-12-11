import tkinter as tk
import time
from random import randint
import math
from PIL import Image, ImageTk
from playsound import playsound
import winsound
from constants import *

castle_sound = 'Classic Horror 3.wav'
forest_sound = 'Overworld.wav'
cave_sound = 'magic-forest-by-kevin-macleod-from-filmmusic-io.wav'
gameover_sound = 'Der Kleber Sting.wav'
done_sound = 'done.wav'
fire_sound = 'fire.wav'
deadin_sound = 'deadin.wav'
minusmr_sound = 'minusmr.wav'
minushp_sound = 'minushp.wav'
# Magic Forest by Kevin MacLeod
# Link: https://incompetech.filmmusic.io/song/4012-magic-forest
# License: http://creativecommons.org/licenses/by/4.0/
#
# "Overworld" Kevin MacLeod (incompetech.com)
# Licensed under Creative Commons: By Attribution 4.0 License
# http://creativecommons.org/licenses/by/4.0/
#
# "Classic Horror 3" Kevin MacLeod (incompetech.com)
# Licensed under Creative Commons: By Attribution 4.0 License
# http://creativecommons.org/licenses/by/4.0/
#
# "Der Kleber Sting" Kevin MacLeod (incompetech.com)
# Licensed under Creative Commons: By Attribution 4.0 License
# http://creativecommons.org/licenses/by/4.0/


class Character:
    def __init__(self):
        """ Конструктор класса Parameters
            Параметры:
            x(int) - положение персонажа по горизонтали
            y(int) - положение персонажа по вертикали
            vx(int) - скорость персонажа по оси x
            vy(int) - скорость персонажа по оси y
            T(list) - параметры, отвечающие за тайминг игры
            level_up(int) - текущий уровень
            character(PhotoImage) - изображение персонажа
        """
        self.vx = 0
        self.vy = 0
        self.character = 0
        self.T = []
        self.x = x
        self.y = y
        self.level_up = 1


    def on_key_press(self, event):
        """ Функция обрабатывает события клавиатуры. Срабатывает при нажатии на кнопку
            Параметры:
            event - кнопка, которая была нажата
        """
        if event.keysym == 'Left':
            self.vx = -u
        elif event.keysym == 'Right':
            self.vx = u
        elif event.keysym == 'Up':
            self.vy = -u
        elif event.keysym == 'Down':
            self.vy = u
        elif event.keysym == 'space':
            B.fire()
        elif event.keysym == 'Return':
            B.change_direction()


    def on_key_release(self, event):
        """ Функция обрабатывает события клавиатуры. Срабатывает при отпускании кнопки
            Параметры:
            event - кнопка, которая была отжата
        """
        if event.keysym in ('Left', 'Right'):
            self.vx = 0
        elif event.keysym in ('Up', 'Down'):
            self.vy = 0


tr = Character()


while True:
    level = tr.level_up
    root = tk.Tk()
    canvas = tk.Canvas(root, width=window_width, height=window_height)
    canvas.pack(side=tk.TOP)
    img_character_1 = Image.open('character_right.png')
    img_character_1 = img_character_1.resize((character_size, character_size), Image.ANTIALIAS)
    img_character_2 = Image.open('character_left.png')
    img_character_2 = img_character_2.resize((character_size, character_size), Image.ANTIALIAS)
    img_character_1 = ImageTk.PhotoImage(img_character_1)
    img_character_2 = ImageTk.PhotoImage(img_character_2)

    if level == 1:
        winsound.PlaySound(forest_sound, winsound.SND_ALIAS | winsound.SND_ASYNC | winsound.SND_LOOP)
        img = ImageTk.PhotoImage(Image.open('level_2_background.jpg'))
    if level == 2:
        move_location('forestandcastle1.png')
        winsound.PlaySound(castle_sound, winsound.SND_ALIAS | winsound.SND_ASYNC | winsound.SND_LOOP)
        img = ImageTk.PhotoImage(Image.open('level_3_background.jpg'))
    if level == 3:
        move_location('castleandcave1.png')
        winsound.PlaySound(cave_sound, winsound.SND_ALIAS | winsound.SND_ASYNC | winsound.SND_LOOP)
        img = ImageTk.PhotoImage(Image.open('level_1_background.png'))

    canvas.create_image(0, 0, image=img, anchor='nw')
    tr.character = canvas.create_image(tr.x, tr. y, image=img_character_1, anchor='nw')


    def move_location(loc_name):
        img1 = ImageTk.PhotoImage(Image.open(loc_name))
        canvas.create_image(0, 0, image=img1, anchor='nw')
        root.update()
        t = time.time()
        char_x = 0
        tr.character = canvas.create_image(char_x, 400, image=img_character_1, anchor='nw')
        while char_x < 600:
            while time.time() - t < 0.03:
                pass
            char_x += 5
            t = time.time()
            canvas.move(tr.character, 5, 0)
            root.update()


    class bullet:
        def __init__(self, bullet_x, bullet_y, color):
            """ Конструктор класса bullet
            Параметры:
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
            self.id = canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r,
                                         fill=self.color)

        def change_direction(self):
            """ Функция изменяет направление стрельбы на противоположное
            """
            if self.direction == 1:
                canvas.delete(tr.character)
                tr.character = canvas.create_image(tr.x, tr.y, image=img_character_2, anchor='nw')
                self.c = 0
            else:
                canvas.delete(tr.character)
                tr.character = canvas.create_image(tr.x, tr.y, image=img_character_1, anchor='nw')
                self.c = 1

        def fire(self):
            """Функция инициализирует выстрел
            """
            if self.x > right_border or self.x < left_border:
                self.x = tr.x
                self.y = tr.y
                self.direction  = self.c

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
                canvas.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)

            if self.y != bullet_x0:
                if self.direction == 1:
                    self.y += self.vy
                else:
                    self.y -= self.vy
                canvas.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)


    class boss:
        def __init__(self, x_boss, y_boss, x_size, y_size, img_boss):
            """ Конструктор класса boss
                Параметры:
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
            self.id = canvas.create_image(self.x - int(self.x_size / 2), self.y - int(self.y_size / 2), image=img_boss,
                                          anchor='nw')

        def change_x_direction(self):
            """ Функция изменяет направление движения по горизонтали на противоположное
            """
            if self.x_direction == 1:
                self.x_direction = 0
                self.x = self.x - 2 * self.vx

            else:
                self.x_direction = 1
                self.x = self.x + 2 * self.vx

        def change_y_direction(self):
            """ Функция изменяет направление движения по вертикали на противоположное
            """
            if self.y_direction == 1:
                self.y_direction = 0
                self.y = self.y - 2 * self.vy

            else:
                self.y_direction = 1
                self.y = self.y + 2 * self.vy

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

            canvas.coords(self.id, self.x - int(self.x_size / 2), self.y - int(self.y_size / 2))

        def destroying_boss(self):
            """Функция удаляет побежденного врага с экрана
            """
            playsound(minusmr_sound, False)
            self.x = delete_point
            self.size = 0
            self.boss_move()

        def rotate(self):
            """Функция меняет характер движения врага
            """
            self.x_direction = randint(0, 2)
            self.vx = randint(1, 3)
            self.vy = randint(1, 3)
            self.x_direction = randint(0, 2)


    class health_indicator:
        def __init__(self, length, x_0, y_0, color):
            """ Конструктор класса health_indicator
                Параметры:
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
            self.id = canvas.create_line(self.x, self.y, self.x + self.length, y_0, width=self.width, fill=self.color)

        def decrease(self, d):
            """Функция изменяет длину индикатора
               Параметры:
               d(int) - величина измениния длины
            """
            self.length -= d
            canvas.coords(self.id, self.x, self.y, self.x + self.length, self.y)
            playsound(minushp_sound, False)


    class mini_twins(boss):
        def __init__(self, x_mini, y_mini):
            """ Конструктор класса mini_boss - двойников осного босса появляющихся раз в 30 секунд и уничтожающихся после первого попадания
                Параметры:
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
            self.id = canvas.create_image(self.x - int(self.x_size / 2), self.y - int(self.x_size / 2),
                                          image=img_mini_boss, anchor='nw')


    def hit_character(array_bullet, T, strip, d):
        """Функция изменяет длину индикатора здоровья персонажа при попадании в него
           Параметры:
           array_bullet(list) - список со всеми вражескими пулями, находящимися на экране
           T(time) - время последнего попадания
           strip(health_indicator) - индикатор здоровья персонажа
           d(int) - величина измениния длины индикатора
        """
        t = []
        for i in range(len(array_bullet)):
            t.append(T)
        for i in range(len(array_bullet)):
            if ((array_bullet[i].x - tr.x) ** 2 + (
                    array_bullet[i].y - tr.y) ** 2) ** 0.5 < character_size / 3 and time.time() - t[i] > 1:
                strip.decrease(d)
                t[i] = time.time()


    def hit_enemy(array_enemyies, array_strips, d):
        """Функция изменяет длину индикатора здоровья противника при попадании в него
           Параметры:
           array_enemies(list) - список со всеми противниками, находящимися на экране
           array_strips(list) - список индикаторов здоровья противников
           d(int) - величина измениния длины индикатора
        """
        for i in range(len(array_enemyies)):
            if ((B.x - array_enemyies[i].x) ** 2 + (B.y - array_enemyies[i].y) ** 2) ** 0.5 < array_enemyies[i].y_size and time.time() - tr.T[1] > 1:
                array_strips[i].decrease(d)
                tr.T[1] = time.time()


    def choose_and_rotate(enemy_array, interval):
        """Функция выбирает одного из противников и случайным образом меняет направление его движения и величину скорости
          Параметры:
          enemies_array(list) - список со всеми противниками, находящимися на экране
          interval(int) - время через которое, функция снова будет запущена
        """
        if time.time() - tr.T[0] > interval:
            if len(enemy_array) != 0:
                j = randint(-1, len(enemy_array) - 1)
                enemy_array[j].rotate()
            tr.T[0] = time.time()


    def bullet_liquidation(array_bullet):
        """Функция уничтожает все пули, оказавшиеся за экраном
          Параметры:
          array_bullet(list) - список со всеми пулями
        """
        for b in array_bullet:
            b.bullet_move()
            if b.x > right_border or b.x < left_border or b.y < up_border or b.y > down_border:
                b.destroying_bullet()
                array_bullet.remove(b)


    def victory(level, enemy_lives_array, enemies):
        """Функция генерирует поздравительную надпись, если уровень пройден и уничтожает всех оставшихся второстепенных противников, пули,оставшиеся на экране и очищает все списки.
        Эта же функция используется если уничтожен только один из противников. В этом случае он и все связанные с ним атрибуты удаляются с экрана
          Параметры:
          level(int) - номер уровня
          enemy_lives_array(list) - список со всеми индикаторами здоровья основных противников
          enemies(list) - список всех противников
        """
        for i in range(len(enemy_lives_array)):
            if enemy_lives_array[i].length < 0:
                if len(enemy_lives_array) == 1:
                    winsound.PlaySound(done_sound, winsound.SND_ALIAS | winsound.SND_ASYNC)
                    print(
                        '\n' + '\n' + 'Great! You have destroyed boss!' + '\n' + 'Congratulations' + '\n' + 'Level ' + str(level) + ' complited')
                    tr.level_up = level + 1
                    root.destroy()
                    tr.x = x
                    tr.y = y
                    tr.vx = 0
                    tr.vy = 0
                enemy_lives_array[i].length = 0
                enemies[i].destroying_boss()
                enemy_lives_array[i].decrease(0)
                enemy_lives_array.pop(i)
                enemies.pop(i)
                break


    def defeat(enemy_bullet_array, enemies):
        """Функция генерирует надпись, в случае поражения и уничтожает всех оставшихся противников, пули,оставшиеся на экране и очищает все списки
          Параметры:
          enemy_lives_array(list) - список со всеми индикаторами здоровья основных противников
          enemies(list) - список всех противников
        """
        if character_lives.length < 0:
            print('\n' + '\n' + 'You lost!' + '\n' + 'Better lack next time!')
            character_lives.length = 0
            for b in enemy_bullet_array:
                b.destroying_bullet()
            enemy_bullet_array.clear()
            for enemy in enemies:
                enemy.destroying_boss()
            character_lives.decrease(0)
            enemies.clear()
            tr.x = x
            tr.y = y
            winsound.PlaySound(gameover_sound, winsound.SND_ALIAS | winsound.SND_ASYNC)


    def level_1():
        """ Главная функция первого уровня
            На первом уровне игрок сражается с одним главным противником, который время от времени призывает себе на помощь свою уменьшенную копию (время появления копий регулирутся параметром T).
            Копия уничтожается после первого попадания в нее.
            Противники двигаются с изменяющейся случайным образом скоростью ( как по модулю так и по направлению)
            Бой происходит по принципу перестрелки: спустя некоторое время, регулируемое параметром T противник и все его копии одновременн стреляют точно в игрока, поэтому чтобы успеть среагировать необходимо постоянно деражаться далеко от противника и его копий, стараться их уничтожать.
        """
        canvas.move(tr.character, tr.vx, tr.vy)
        tr.x += tr.vx
        tr.y += tr.vy
        root.after(20, level_1)
        B.bullet_move()
        boss_1.boss_move()
        boss = []
        boss.append(boss_1)
        enemy_lives_array = []
        enemy_lives_array.append(enemy_lives)
        choose_and_rotate(boss, 5)
        hit_enemy(boss, enemy_lives_array, 100)

        if time.time() - tr.T[2] > 2:
            for i in range(len(twins)):
                enemy_bullet[i].x = twins[i].x
                enemy_bullet[i].y = twins[i].y
                enemy_bullet[i].vx = 15 * (tr.x - twins[i].x) / ((tr.x - twins[i].x) ** 2 + (tr.y - twins[i].y) ** 2) ** 0.5
                enemy_bullet[i].vy = 15 * (tr.y - twins[i].y) / ((tr.x - twins[i].x) ** 2 + (tr.y - twins[i].y) ** 2) ** 0.5
            tr.T[2] = time.time()
        for b in enemy_bullet:
            b.bullet_move()

        if time.time() - tr.T[3] > 5 and len(twins) != 0:
            a = randint(left_border_1, right_border_1)
            b = randint(up_border_1, down_border_1)
            twins.append(mini_twins(a, b))
            enemy_bullet.append(bullet(a, b, 'red'))
            tr.T[3] = time.time()
        for m in twins:
            m.boss_move()

        hit_character(enemy_bullet, T, character_lives, 20)

        for i in range(1, len(twins)):
            if ((twins[i].x - B.x) ** 2 + (twins[i].y - B.y) ** 2) ** 0.5 < twins[i].y_size:
                twins[i].destroying_boss()
                enemy_bullet[i].destroying_bullet()
                del twins[i]
                del enemy_bullet[i]
                break

        victory(1, enemy_lives_array, boss)

        if len(enemy_lives_array) == 0:
            for m in twins:
                m.destroying_boss()
            twins.clear()

        defeat(enemy_bullet, twins)


    def explosion(N, color, array_bullet, enemies, interval):
        """Функция инициализирует специфическую атаку врага - выстрел по всем направлениям ("взрыв")
           Параметры:
           N(int) - количество выбрасываемых пуль
           color(str) - цвет пуль
           array_bullet(list) - список со всеми вражескими пулями, находящимися на экране
           enemies(list) - список всех противников
           interval(int) - промежуток времени между повторными запусками функции
        """
        if time.time() - tr.T[2] > interval and len(enemies) != 0:
            playsound(fire_sound, False)
            j = randint(-1, len(enemies) - 1)
            shift = randint(0, 10)
            for i in range(N):
                array_bullet.append(bullet(enemies[j].x, enemies[j].y, color))
                n = len(array_bullet) - 1
                array_bullet[n].vy = int(7 * math.sin(shift + i * 2 * math.pi / N))
                array_bullet[n].vx = int(7 * math.cos(shift + i * 2 * math.pi / N))
            tr.T[2] = time.time()


    def level_2():
        """ Главная функция второго уровня
            На втором уровне игроку приходится вести бой одновременно с тремя противниками
            У противников появляется новый тип атаки- одновременный выстрел по разным направлениям.
            За время регулироемое параметром T один случайно выбранный противник производит эту атаку один раз.
            Направления обстрела и их количество выбираются случайным образом
            Чтобы увернуться от атаки нужно все время находится достаточно далеко от всех противников
            Для победы надо уничтожить всех трех противников
        """
        canvas.move(tr.character, tr.vx, tr.vy)
        tr.x += tr.vx
        tr.y += tr.vy
        root.after(20, level_2)
        B.bullet_move()
        for boss_2 in bosses_2:
            boss_2.boss_move()
        choose_and_rotate(bosses_2, 5)
        hit_enemy(bosses_2, enemy_lives, 100)
        explosion(randint(20, 30), 'red', enemy_bullet_2, bosses_2, 2)
        bullet_liquidation(enemy_bullet_2)
        hit_character(enemy_bullet_2, T, character_lives, 10)
        victory(2, enemy_lives, bosses_2)
        defeat(enemy_bullet_2, bosses_2)


    def level_3():
        """ Главная функция третьего уровня
        На третьем уровне противник при каждом попадании в него делится на два новых меньшего размера и большей скорости
        Это происходит три раза и в конечном счете крупный противник последоательно распадается на шестнадцать мелких
        """
        tr.x += tr.vx
        tr.y += tr.vy
        canvas.move(tr.character, tr.vx, tr.vy)
        root.after(20, level_3)
        B.bullet_move()
        for boss_3 in bosses_3:
            boss_3.boss_move()
        choose_and_rotate(bosses_3, 5)


        for i in range(len(bosses_3)):
            if ((B.x - bosses_3[i].x) ** 2 + (B.y - bosses_3[i].y) ** 2) ** 0.5 < bosses_3[i].y_size / 2 and time.time() - tr.T[1] > 1:
                enemy_lives.decrease(20)
                if bosses_3[i].y_size != boss_3_x_size - 3 * delta:
                    bosses_3[i].c += 1
                    bosses_3[i].y_size -= delta
                    bosses_3[i].x_size -= delta
                    bosses_3.append(
                        boss(bosses_3[i].x, bosses_3[i].y + delta / 2, bosses_3[i].x_size, bosses_3[i].y_size,
                             img_boss[bosses_3[i].c]))
                    bosses_3.append(
                        boss(bosses_3[i].x, bosses_3[i].y + delta / 2, bosses_3[i].x_size, bosses_3[i].y_size,
                             img_boss[bosses_3[i].c]))
                    n = len(bosses_3)
                    bosses_3[n - 1].c = bosses_3[i].c
                    bosses_3[n - 2].c = bosses_3[i].c
                    bosses_3[n - 1].vx += 1
                    bosses_3[n - 2].y_direction = 0
                    bosses_3[n - 1].vy += 1
                    bosses_3[n - 2].vx += 1
                    bosses_3[n - 2].vy += 1
                    bosses_3[i].destroying_boss()
                    bosses_3.pop(i)
                else:
                    bosses_3[i].destroying_boss()
                    bosses_3.pop(i)
                    break
                tr.T[1] = time.time()

        explosion(randint(15, 20), 'cyan', enemy_bullet_3, bosses_3, 1)
        bullet_liquidation(enemy_bullet_3)
        hit_character(enemy_bullet_3, T, character_lives, 10)
        defeat(enemy_bullet_3, bosses_3)

        if enemy_lives.length < 0:
            enemy_lives.length = 0
            enemy_lives.decrease(0)
            print(
                '\n' + '\n' + 'Great! You have destroyed boss!' + '\n' + 'Congratulations' + '\n' + 'Level 3 complited')


    print(
        'Управление:' + '\n' + 'Стрелки отвечают за перемещение персонажа' + '\n' + 'Выстрел - клавиша пробел' + '\n' + 'Поменять направление стрельбы (с права на лево и наоборот) - клавиша Enter')

    T = time.time()
    for i in range(4):
        tr.T.append(T)
    character_lives = health_indicator(character_lives_len, character_lives_x0, character_lives_y0, 'lawn green')
    B = bullet(bullet_x0, bullet_x0, 'orange')

    if level == 1:
        img_boss = Image.open('boss_1.png')
        img_boss = img_boss.resize((boss_1_x_size, boss_1_y_size), Image.ANTIALIAS)
        img_boss = ImageTk.PhotoImage(img_boss)
        img_mini_boss = Image.open('boss_1.png')
        img_mini_boss = img_mini_boss.resize((int(boss_1_x_size / 2), int(boss_1_y_size / 2)), Image.ANTIALIAS)
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
            enemy_lives.append(
                health_indicator(int(enemy_lives_len / 2), enemy_lives_x0, enemy_lives_y0 - i * space, 'red'))
        enemy_bullet_2 = []

    if level == 3:
        bosses_3 = []
        img_b = Image.open('boss_3.png')
        img_sizes = []
        img_boss = []
        for i in range(4):
            img_sizes.append(img_b.resize((boss_3_x_size - i * delta, boss_3_y_size - i * delta), Image.ANTIALIAS))
            img_boss.append(ImageTk.PhotoImage(img_sizes[i]))
        bosses_3.append(boss(boss_x0, boss_y0, boss_3_x_size, boss_3_y_size, img_boss[0]))
        enemy_lives = health_indicator(enemy_lives_len, enemy_lives_x0, enemy_lives_y0, 'red')
        enemy_bullet_3 = []

    root.bind('<Key>', tr.on_key_press)
    root.bind('<KeyRelease>', tr.on_key_release)

    if level == 1:
        level_1()
    if level == 2:
        level_2()
    if level == 3:
        level_3()
    root.mainloop()