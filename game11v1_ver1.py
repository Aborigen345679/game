import tkinter as tk  # Импортируем библиотеку для создания графического интерфейса
import random  # Импортируем модуль для генерации случайных чисел

# ============= ГЛАВНЫЙ КЛАСС ПРИЛОЖЕНИЯ =============
class Game11v1:
    def __init__(self):
        # Создаем главное окно приложения
        self.root = tk.Tk()
        self.root.title("11v1 GAMING HUB")  # Устанавливаем заголовок окна
        self.root.geometry("1200x700")  # Устанавливаем размер окна (ширина x высота)
        self.root.configure(bg='#0a0a0a')  # Устанавливаем темный фон окна (hex-код цвета)
        
        # Словарь с цветовой схемой приложения (для единообразия)
        self.colors = {
            'bg': '#0a0a0a',      # Основной темный фон
            'card': '#1a1a1a',     # Фон для карточек игр (чуть светлее)
            'primary': '#00ff88',   # Основной акцентный цвет (зеленый неон)
            'secondary': '#ff3366', # Второстепенный акцентный цвет (розовый)
            'text': '#ffffff',      # Основной цвет текста (белый)
            'text2': '#b0b0b0'      # Второстепенный цвет текста (серый)
        }
        
        # Вызываем метод создания главного меню
        self.create_menu()
    
    def create_menu(self):
        """Создает главное меню с карточками всех игр"""
        # Создаем заголовок меню
        tk.Label(self.root, 
                text="⚡ 11v1 GAMING HUB ⚡",  # Текст заголовка с эмодзи
                font=('Helvetica', 28, 'bold'),  # Шрифт: название, размер, жирный
                bg=self.colors['bg'],  # Фон из словаря цветов
                fg=self.colors['primary']  # Цвет текста из словаря
               ).pack(pady=20)  # Размещаем с отступом сверху/снизу 20 пикселей
        
        # Создаем фрейм-контейнер для сетки с играми
        frame = tk.Frame(self.root, bg=self.colors['bg'])
        frame.pack(expand=True)  # expand=True - фрейм будет расширяться при изменении окна
        
        # Список всех игр: (эмодзи, название, класс игры)
        games = [
            ("🐍", "Змейка", SnakeGame),
            ("🧩", "Тетрис", TetrisGame),
            ("🎯", "2048", Game2048),
            ("💣", "Сапер", MinesweeperGame),
            ("⚓", "Морской бой", BattleshipGame),
            ("♜", "Шахматы", ChessGame),
            ("●", "Шашки", CheckersGame),
            ("◉", "Реверси", ReversiGame),
            ("🏓", "Пинг-понг", PongGame),
            ("🧱", "Арканоид", ArkanoidGame),
            ("🐦", "Flappy Bird", FlappyBirdGame)
        ]
        
        # Создаем карточки для каждой игры в цикле
        # enumerate возвращает индекс и значение для каждого элемента списка
        for i, (emoji, name, game) in enumerate(games):
            # Создаем карточку - отдельный фрейм для каждой игры
            card = tk.Frame(frame, 
                           bg=self.colors['card'],  # Цвет фона карточки
                           width=300,  # Ширина карточки
                           height=180  # Высота карточки
                          )
            # Размещаем в сетке: row = i//3 (целочисленное деление), column = i%3 (остаток)
            # Это создает сетку 3 колонки
            card.grid(row=i//3, column=i%3, padx=10, pady=10)
            card.pack_propagate(False)  # Запрещаем изменение размера карточки содержимым
            
            # Добавляем эмодзи игры
            tk.Label(card, 
                    text=emoji,
                    font=('Segoe UI Emoji', 40),  # Специальный шрифт для эмодзи
                    bg=self.colors['card'],
                    fg=self.colors['primary']
                   ).pack(pady=10)  # Отступ сверху/снизу 10 пикселей
            
            # Добавляем название игры
            tk.Label(card, 
                    text=name,
                    font=('Helvetica', 14, 'bold'),
                    bg=self.colors['card'],
                    fg=self.colors['text']
                   ).pack()
            
            # Добавляем кнопку "ИГРАТЬ"
            # lambda g=game: self.open_game(g) - создает функцию, которая при нажатии
            # вызывает open_game с текущим классом игры
            tk.Button(card, 
                     text="ИГРАТЬ",
                     font=('Helvetica', 12, 'bold'),
                     bg=self.colors['primary'],
                     fg=self.colors['bg'],
                     command=lambda g=game: self.open_game(g)  # Функция при нажатии
                    ).pack(side='bottom', fill='x', ipady=5)  # side='bottom' - внизу, fill='x' - по ширине, ipady - внутренний отступ
    
    def open_game(self, game_class):
        """Открывает окно с выбранной игрой"""
        # Создаем новое окно поверх главного
        win = tk.Toplevel(self.root)
        win.title("11v1")  # Заголовок окна
        win.geometry("800x600")  # Размер окна игры
        win.configure(bg=self.colors['bg'])  # Устанавливаем фон
        
        # Делаем окно модальным (блокирует главное окно)
        win.transient(self.root)
        win.grab_set()  # Захватываем фокус ввода
        
        # Создаем экземпляр выбранной игры, передавая окно и цвета
        game_class(win, self.colors)


# ============= БАЗОВЫЙ КЛАСС ДЛЯ ВСЕХ ИГР =============
class BaseGame:
    """Базовый класс, от которого наследуются все игры.
       Содержит общую логику создания интерфейса"""
    
    def __init__(self, window, colors):
        self.win = window  # Сохраняем ссылку на окно
        self.c = colors    # Сохраняем цветовую схему
        
        self.setup_ui()    # Создаем пользовательский интерфейс
        self.new_game()    # Запускаем новую игру
    
    def setup_ui(self):
        """Создает общие элементы интерфейса для всех игр"""
        # Заголовок игры (будет изменен в конкретных играх)
        self.title = tk.Label(self.win, 
                              font=('Helvetica', 24, 'bold'),
                              bg=self.c['bg'], 
                              fg=self.c['primary'])
        self.title.pack(pady=10)
        
        # Холст для рисования игры
        self.canvas = tk.Canvas(self.win, 
                                bg=self.c['bg'], 
                                highlightthickness=2,  # Толщина рамки
                                highlightbackground=self.c['card'])  # Цвет рамки
        self.canvas.pack(pady=10)
        
        # Нижняя панель с информацией и кнопками
        frame = tk.Frame(self.win, bg=self.c['bg'])
        frame.pack()
        
        # Метка для отображения статуса/счета
        self.status = tk.Label(frame, 
                               font=('Helvetica', 12),
                               bg=self.c['bg'], 
                               fg=self.c['text2'])
        self.status.pack(side='left', padx=10)
        
        # Кнопка новой игры (перезапуска)
        tk.Button(frame, 
                  text="🔄 Новая игра", 
                  font=('Helvetica', 11, 'bold'),
                  bg=self.c['primary'], 
                  fg=self.c['bg'],
                  command=self.new_game  # При нажатии вызываем new_game
                 ).pack(side='right', padx=10)
    
    def new_game(self):
        """Метод для переопределения в конкретных играх"""
        pass  # pass означает "ничего не делать" (заглушка)


# ============= ИГРА 1: ЗМЕЙКА =============
class SnakeGame(BaseGame):
    """Классическая игра Змейка"""
    
    def setup_ui(self):
        """Настройка специфического интерфейса для Змейки"""
        super().setup_ui()  # Вызываем метод родительского класса
        self.title.config(text="🐍 ЗМЕЙКА")  # Устанавливаем заголовок
        self.cell = 20  # Размер одной клетки в пикселях
        self.canvas.config(width=400, height=400)  # Размер холста 20x20 клеток
        
        # Привязываем нажатия клавиш к методу key
        self.win.bind('<KeyPress>', self.key)
        self.win.focus_set()  # Устанавливаем фокус на окно для приема клавиш
    
    def new_game(self):
        """Начинает новую игру"""
        # Начальная позиция змейки (список координат (x,y))
        self.snake = [(10,10), (9,10), (8,10)]
        self.dir = (1,0)  # Направление движения (x, y): (1,0) - вправо
        self.food = self.spawn_food()  # Создаем еду
        self.score = 0  # Счет
        self.game_over = False  # Флаг окончания игры
        
        self.update()  # Запускаем игровой цикл
    
    def spawn_food(self):
        """Создает еду в случайном месте, где нет змейки"""
        while True:  # Бесконечный цикл, пока не найдем свободное место
            # random.randint(0,19) - случайное число от 0 до 19
            f = (random.randint(0,19), random.randint(0,19))
            if f not in self.snake:  # Если место свободно
                return f  # Возвращаем координаты
    
    def key(self, e):
        """Обрабатывает нажатия клавиш"""
        # Словарь соответствия клавиш направлениям
        d = {'Up':(0,-1), 'Down':(0,1), 'Left':(-1,0), 'Right':(1,0),
             'w':(0,-1), 's':(0,1), 'a':(-1,0), 'd':(1,0)}
        
        if e.keysym in d:  # Если нажатая клавиша есть в словаре
            new = d[e.keysym]  # Получаем новое направление
            
            # Запрещаем разворот на 180 градусов
            # Проверяем, что новое направление не противоположно текущему
            if (new[0] != -self.dir[0] or new[1] != -self.dir[1]):
                self.dir = new  # Меняем направление
    
    def update(self):
        """Игровой цикл - обновляет состояние игры"""
        if self.game_over:  # Если игра окончена, ничего не делаем
            return
        
        # Вычисляем новую голову змейки
        head = (self.snake[0][0] + self.dir[0], self.snake[0][1] + self.dir[1])
        
        # Проверяем столкновение со стенами или с самой собой
        if (head[0] < 0 or head[0] >= 20 or  # Выход за левую/правую границу
            head[1] < 0 or head[1] >= 20 or  # Выход за верхнюю/нижнюю границу
            head in self.snake):  # Столкновение с собой
            self.game_over = True  # Устанавливаем флаг окончания
            self.draw()  # Рисуем (покажем сообщение о конце)
            return
        
        # Добавляем новую голову в начало списка
        self.snake.insert(0, head)
        
        if head == self.food:  # Если голова на еде
            self.score += 10  # Увеличиваем счет
            self.food = self.spawn_food()  # Создаем новую еду
        else:
            self.snake.pop()  # Удаляем хвост (последний элемент)
        
        self.draw()  # Перерисовываем экран
        
        # Планируем следующий вызов update через 150 миллисекунд
        self.win.after(150, self.update)
    
    def draw(self):
        """Отрисовывает текущее состояние игры"""
        self.canvas.delete("all")  # Очищаем холст
        
        # Рисуем сетку (клетки поля)
        for i in range(20):  # Проходим по всем x
            for j in range(20):  # Проходим по всем y
                x, y = i*self.cell, j*self.cell  # Вычисляем координаты на холсте
                # Чередуем цвета клеток для красоты
                color = '#2a2a2a' if (i+j)%2 else '#1a1a1a'
                self.canvas.create_rectangle(x, y, x+self.cell, y+self.cell, 
                                            fill=color, outline='')
        
        # Рисуем змейку
        for i, s in enumerate(self.snake):
            x, y = s[0]*self.cell+2, s[1]*self.cell+2  # Координаты с отступом 2px
            # Голова - основным цветом, тело - вторичным
            color = self.c['primary'] if i==0 else self.c['secondary']
            # Рисуем овал (круг) - сегмент змейки
            self.canvas.create_oval(x, y, x+self.cell-4, y+self.cell-4, fill=color)
        
        # Рисуем еду
        fx, fy = self.food[0]*self.cell+self.cell//2, self.food[1]*self.cell+self.cell//2
        self.canvas.create_oval(fx-6, fy-6, fx+6, fy+6, fill=self.c['secondary'])
        
        # Если игра окончена, показываем сообщение
        if self.game_over:
            self.canvas.create_text(200, 200, 
                                   text=f"ИГРА ОКОНЧЕНА\nСчет: {self.score}",
                                   fill='red', 
                                   font=('Helvetica', 20, 'bold'), 
                                   justify='center')  # Выравнивание по центру
        
        # Обновляем текст статуса
        self.status.config(text=f"Счет: {self.score}")


# ============= ИГРА 2: ТЕТРИС =============
class TetrisGame(BaseGame):
    def setup_ui(self):
        super().setup_ui()
        self.title.config(text="🧩 ТЕТРИС")
        self.cell = 25  # Размер клетки
        self.canvas.config(width=250, height=500)  # 10x20 клеток
        
        # Словарь всех возможных фигур тетриса
        # 1 - есть клетка, 0 - пусто
        self.shapes = {
            'I': [[1,1,1,1]],  # Палочка
            'O': [[1,1],[1,1]],  # Квадрат
            'T': [[0,1,0],[1,1,1]],  # Т-образная
            'S': [[0,1,1],[1,1,0]],  # S-образная
            'Z': [[1,1,0],[0,1,1]],  # Z-образная
            'L': [[1,0,0],[1,1,1]],  # Г-образная (поворот влево)
            'J': [[0,0,1],[1,1,1]]   # Г-образная (поворот вправо)
        }
        
        # Цвета для каждой фигуры
        self.col = {
            'I':'#00ffff',  # Голубой
            'O':'#ffff00',  # Желтый
            'T':'#ff00ff',  # Пурпурный
            'S':'#00ff00',  # Зеленый
            'Z':'#ff0000',  # Красный
            'L':'#ff8800',  # Оранжевый
            'J':'#0000ff'   # Синий
        }
        
        # Привязываем клавиши управления
        self.win.bind('<Left>', lambda e: self.move(-1))   # Стрелка влево
        self.win.bind('<Right>', lambda e: self.move(1))   # Стрелка вправо
        self.win.bind('<Down>', lambda e: self.drop())     # Стрелка вниз (ускорение)
        self.win.bind('<Up>', lambda e: self.rotate())     # Стрелка вверх (поворот)
        self.win.focus_set()
    
    def new_game(self):
        """Начинает новую игру"""
        # Создаем пустое игровое поле 10x20
        self.board = [[0]*10 for _ in range(20)]  # 0 - пустая клетка
        self.score = 0
        self.game_over = False
        self.new_piece()  # Создаем первую фигуру
        self.update()
    
    def new_piece(self):
        """Создает новую случайную фигуру"""
        name = random.choice(list(self.shapes.keys()))  # Выбираем случайное название
        self.piece = {
            'shape': self.shapes[name],  # Форма фигуры
            'color': self.col[name],      # Цвет фигуры
            'x': 5 - len(self.shapes[name][0])//2,  # Центрируем по горизонтали
            'y': 0                         # Начинаем сверху
        }
        # Проверяем, не накладывается ли новая фигура на уже занятые клетки
        if self.collision():
            self.game_over = True  # Если да - игра окончена
    
    def collision(self):
        """Проверяет столкновение текущей фигуры с границами или другими фигурами"""
        for y,row in enumerate(self.piece['shape']):
            for x,cell in enumerate(row):
                if cell:  # Если клетка фигуры не пуста
                    bx = self.piece['x'] + x  # x на поле
                    by = self.piece['y'] + y  # y на поле
                    
                    # Проверяем выход за границы
                    if (bx < 0 or bx >= 10 or      # Выход по горизонтали
                        by >= 20 or                  # Выход вниз
                        (by >= 0 and self.board[by][bx])):  # Столкновение с другой фигурой
                        return True
        return False
    
    def move(self, dx):
        """Перемещает фигуру по горизонтали"""
        if self.game_over: return
        self.piece['x'] += dx  # Смещаем
        if self.collision():    # Если произошло столкновение
            self.piece['x'] -= dx  # Отменяем смещение
    
    def rotate(self):
        """Поворачивает фигуру"""
        if self.game_over: return
        shape = self.piece['shape']
        # Поворачиваем матрицу на 90 градусов по часовой стрелке
        rotated = [list(row) for row in zip(*shape[::-1])]
        self.piece['shape'] = rotated
        if self.collision():  # Если после поворота столкновение
            self.piece['shape'] = shape  # Возвращаем старую форму
    
    def drop(self):
        """Опускает фигуру на одну клетку вниз"""
        if self.game_over: return
        self.piece['y'] += 1
        if self.collision():  # Если столкнулись
            self.piece['y'] -= 1  # Возвращаем на место
            self.lock()           # Фиксируем фигуру на поле
            self.new_piece()      # Создаем новую
    
    def lock(self):
        """Фиксирует текущую фигуру на игровом поле"""
        # Копируем фигуру на поле
        for y,row in enumerate(self.piece['shape']):
            for x,cell in enumerate(row):
                if cell:
                    self.board[self.piece['y']+y][self.piece['x']+x] = self.piece['color']
        
        # Проверяем заполненные линии
        lines = 0
        y = 19  # Начинаем снизу
        while y >= 0:
            if all(self.board[y]):  # Если вся линия заполнена
                del self.board[y]           # Удаляем линию
                self.board.insert(0, [0]*10)  # Добавляем пустую сверху
                lines += 1
            else:
                y -= 1
        
        # Начисляем очки за линии
        # 1 линия - 100, 2 - 300, 3 - 500, 4 - 800
        self.score += [0,100,300,500,800][lines]
    
    def update(self):
        """Игровой цикл"""
        if not self.game_over:
            self.drop()  # Опускаем фигуру
            self.draw()  # Перерисовываем
            # Планируем следующий шаг через 500 мс
            self.win.after(500, self.update)
    
    def draw(self):
        """Отрисовка игры"""
        self.canvas.delete("all")
        
        # Рисуем игровое поле
        for y in range(20):
            for x in range(10):
                x1, y1 = x*self.cell, y*self.cell
                # Если клетка занята - цвет фигуры, иначе - серый
                color = self.board[y][x] or ('#2a2a2a' if (x+y)%2 else '#1a1a1a')
                self.canvas.create_rectangle(x1, y1, x1+self.cell, y1+self.cell, fill=color)
        
        # Рисуем текущую падающую фигуру
        for y,row in enumerate(self.piece['shape']):
            for x,cell in enumerate(row):
                if cell:
                    x1 = (self.piece['x']+x)*self.cell
                    y1 = (self.piece['y']+y)*self.cell
                    self.canvas.create_rectangle(x1, y1, x1+self.cell, y1+self.cell,
                                                fill=self.piece['color'])
        
        self.status.config(text=f"Счет: {self.score}")


# ============= ИГРА 3: 2048 =============
class Game2048(BaseGame):
    def setup_ui(self):
        super().setup_ui()
        self.title.config(text="🎯 2048")
        self.cell = 100  # Размер клетки
        self.canvas.config(width=400, height=400)  # Поле 4x4
        
        # Цвета для разных чисел
        self.col = {
            0:'#cdc1b4',      # Пустая клетка
            2:'#eee4da',       # 2
            4:'#ede0c8',       # 4
            8:'#f2b179',       # 8
            16:'#f59563',      # 16
            32:'#f67c5f',      # 32
            64:'#f65e3b',      # 64
            128:'#edcf72',     # 128
            256:'#edcc61',     # 256
            512:'#edc850',     # 512
            1024:'#edc53f',    # 1024
            2048:'#edc22e'     # 2048
        }
        
        # Привязываем клавиши управления
        self.win.bind('<Left>', lambda e: self.move('left'))
        self.win.bind('<Right>', lambda e: self.move('right'))
        self.win.bind('<Up>', lambda e: self.move('up'))
        self.win.bind('<Down>', lambda e: self.move('down'))
        self.win.focus_set()
    
    def new_game(self):
        """Начинает новую игру"""
        self.board = [[0]*4 for _ in range(4)]  # Пустое поле 4x4
        self.score = 0
        self.add_tile()  # Добавляем первую плитку
        self.add_tile()  # Добавляем вторую плитку
        self.draw()
    
    def add_tile(self):
        """Добавляет новую плитку (2 или 4) в случайную пустую клетку"""
        # Список всех пустых клеток
        empty = [(i,j) for i in range(4) for j in range(4) if not self.board[i][j]]
        if empty:
            i,j = random.choice(empty)  # Выбираем случайную пустую
            # 90% - 2, 10% - 4
            self.board[i][j] = 2 if random.random()<0.9 else 4
    
    def move(self, dir):
        """Перемещает все плитки в указанном направлении"""
        old = [row[:] for row in self.board]  # Сохраняем старое состояние
        
        if dir == 'left':
            # Обрабатываем каждую строку
            for i in range(4):
                self.board[i] = self.merge(self.board[i])
        elif dir == 'right':
            # Разворачиваем строку, обрабатываем, разворачиваем обратно
            for i in range(4):
                self.board[i] = self.merge(self.board[i][::-1])[::-1]
        elif dir == 'up':
            # Транспонируем матрицу (строки становятся столбцами)
            self.board = list(map(list, zip(*self.board)))
            for i in range(4):
                self.board[i] = self.merge(self.board[i])
            # Транспонируем обратно
            self.board = list(map(list, zip(*self.board)))
        else:  # down
            self.board = list(map(list, zip(*self.board)))
            for i in range(4):
                self.board[i] = self.merge(self.board[i][::-1])[::-1]
            self.board = list(map(list, zip(*self.board)))
        
        # Если поле изменилось, добавляем новую плитку
        if old != self.board:
            self.add_tile()
            self.draw()
    
    def merge(self, row):
        """Объединяет одинаковые числа в строке (логика 2048)"""
        # Убираем нули
        new = [x for x in row if x]
        
        # Объединяем соседние одинаковые числа
        for i in range(len(new)-1):
            if new[i] == new[i+1]:
                new[i] *= 2
                self.score += new[i]
                new[i+1] = 0
        
        # Снова убираем нули
        new = [x for x in new if x]
        # Дополняем нулями до длины 4
        return new + [0]*(4-len(new))
    
    def draw(self):
        """Отрисовка игры"""
        self.canvas.delete("all")
        
        for i in range(4):
            for j in range(4):
                x, y = j*self.cell+5, i*self.cell+5  # +5 для отступа
                val = self.board[i][j]
                # Рисуем клетку
                self.canvas.create_rectangle(x, y, x+self.cell-10, y+self.cell-10,
                                            fill=self.col.get(val,'#3c3a32'))
                if val:  # Если не пусто, пишем число
                    self.canvas.create_text(x+45, y+45, text=str(val),
                                           font=('Helvetica', 24, 'bold'))
        
        self.status.config(text=f"Счет: {self.score}")


# ============= ИГРА 4: САПЕР =============
class MinesweeperGame(BaseGame):
    def setup_ui(self):
        super().setup_ui()
        self.title.config(text="💣 САПЕР")
        self.cell = 40  # Размер клетки
        self.canvas.config(width=320, height=320)  # Поле 8x8
        
        # Привязываем левую и правую кнопки мыши
        self.canvas.bind('<Button-1>', self.left)   # Левый клик - открыть клетку
        self.canvas.bind('<Button-3>', self.right)  # Правый клик - поставить флаг
    
    def new_game(self):
        """Начинает новую игру"""
        self.rows = self.cols = 8
        self.mines = 10  # Количество мин
        
        # Игровое поле: -1 = мина, числа = количество мин вокруг
        self.board = [[0]*8 for _ in range(8)]
        self.revealed = [[False]*8 for _ in range(8)]  # Открытые клетки
        self.flags = [[False]*8 for _ in range(8)]    # Клетки с флагами
        self.game_over = False
        
        # Расставляем мины случайно
        for _ in range(self.mines):
            while True:
                r, c = random.randint(0,7), random.randint(0,7)
                if self.board[r][c] != -1:  # Если здесь еще нет мины
                    self.board[r][c] = -1
                    break
        
        # Вычисляем числа для каждой клетки (сколько мин вокруг)
        for r in range(8):
            for c in range(8):
                if self.board[r][c] != -1:  # Если не мина
                    cnt = 0
                    # Проверяем все 8 соседних клеток
                    for dr in [-1,0,1]:
                        for dc in [-1,0,1]:
                            nr, nc = r+dr, c+dc
                            if 0<=nr<8 and 0<=nc<8 and self.board[nr][nc]==-1:
                                cnt += 1
                    self.board[r][c] = cnt
        self.draw()
    
    def left(self, e):
        """Обработка левого клика - открыть клетку"""
        if self.game_over: return
        
        # Определяем координаты клетки по позиции мыши
        r, c = e.y//self.cell, e.x//self.cell
        
        if not self.flags[r][c]:  # Если нет флага
            if self.board[r][c] == -1:  # Если это мина
                self.game_over = True
                self.revealed[r][c] = True
            else:
                self.reveal(r,c)  # Открываем клетку
            self.draw()
    
    def right(self, e):
        """Обработка правого клика - поставить/убрать флаг"""
        if self.game_over: return
        
        r, c = e.y//self.cell, e.x//self.cell
        
        if not self.revealed[r][c]:  # Если клетка еще не открыта
            self.flags[r][c] = not self.flags[r][c]  # Переключаем флаг
            self.draw()
    
    def reveal(self, r, c):
        """Рекурсивно открывает клетки (если число 0 - открывает соседние)"""
        # Проверяем границы и не открыта ли уже
        if not (0<=r<8 and 0<=c<8) or self.revealed[r][c] or self.flags[r][c]:
            return
        
        self.revealed[r][c] = True  # Открываем клетку
        
        # Если клетка с числом 0, открываем всех соседей
        if self.board[r][c] == 0:
            for dr in [-1,0,1]:
                for dc in [-1,0,1]:
                    self.reveal(r+dr, c+dc)
    
    def draw(self):
        """Отрисовка игры"""
        self.canvas.delete("all")
        
        for r in range(8):
            for c in range(8):
                x, y = c*self.cell, r*self.cell
                
                if self.revealed[r][c]:  # Открытая клетка
                    if self.board[r][c] == -1:  # Мина
                        self.canvas.create_rectangle(x,y,x+self.cell,y+self.cell, fill='red')
                        self.canvas.create_text(x+20,y+20, text='💣', font=('Segoe UI Emoji', 20))
                    else:  # Число
                        self.canvas.create_rectangle(x,y,x+self.cell,y+self.cell, fill='#c0c0c0')
                        if self.board[r][c]:  # Если не 0, показываем число
                            self.canvas.create_text(x+20,y+20, text=str(self.board[r][c]),
                                                   font=('Helvetica', 16, 'bold'))
                else:  # Закрытая клетка
                    self.canvas.create_rectangle(x,y,x+self.cell,y+self.cell, fill='#808080')
                    if self.flags[r][c]:  # Если есть флаг
                        self.canvas.create_text(x+20,y+20, text='🚩', font=('Segoe UI Emoji', 20))


# ============= ИГРА 5: МОРСКОЙ БОЙ =============
class BattleshipGame(BaseGame):
    def setup_ui(self):
        super().setup_ui()
        self.title.config(text="⚓ МОРСКОЙ БОЙ")
        self.cell = 40
        self.canvas.config(width=400, height=400)
        self.canvas.bind('<Button-1>', self.click)
        
        # Размеры кораблей для расстановки
        self.ships = [4,3,3,2,2,2,1,1,1,1]  # 1 палуба, 2 палубы, и т.д.
        
        # Панель с кнопками режимов
        self.mode_frame = tk.Frame(self.win, bg=self.c['bg'])
        self.mode_frame.pack()
        
        tk.Button(self.mode_frame, text="⚔ БОЙ", command=self.start_battle,
                 bg=self.c['primary'], fg=self.c['bg']).pack(side='left', padx=5)
        tk.Button(self.mode_frame, text="🚢 РАССТАВИТЬ", command=self.new_game,
                 bg=self.c['secondary'], fg=self.c['bg']).pack(side='left', padx=5)
    
    def new_game(self):
        """Начинает новую игру (режим расстановки)"""
        self.player = [[0]*8 for _ in range(8)]      # Корабли игрока
        self.computer = [[0]*8 for _ in range(8)]    # Корабли компьютера
        self.player_shots = [[False]*8 for _ in range(8)]    # Выстрелы игрока
        self.computer_shots = [[False]*8 for _ in range(8)]  # Выстрелы компьютера
        
        self.placement_mode = True   # Режим расстановки
        self.current_ship = 0        # Индекс текущего корабля для расстановки
        self.battle_mode = False     # Режим боя
        self.game_over = False
        self.player_turn = True      # Чей ход
        
        self.draw()
        self.status.config(text="Расставьте корабли (клик для поворота)")
    
    def start_battle(self):
        """Переключает в режим боя"""
        if self.placement_mode:
            self.auto_place(self.computer)  # Автоматически расставляем корабли компьютера
            self.placement_mode = False
            self.battle_mode = True
            self.player_turn = True
            self.status.config(text="Ваш ход")
        self.draw()
    
    def auto_place(self, board):
        """Автоматическая расстановка кораблей"""
        for size in self.ships:
            placed = False
            while not placed:
                # Выбираем случайную позицию и ориентацию
                r, c = random.randint(0,7), random.randint(0,7)
                horizontal = random.choice([True, False])
                
                if horizontal and c+size <= 8:  # Горизонтально, проверяем границы
                    # Проверяем, что все клетки свободны
                    if all(board[r][c+i] == 0 for i in range(size)):
                        for i in range(size): 
                            board[r][c+i] = size  # Ставим корабль
                        placed = True
                elif not horizontal and r+size <= 8:  # Вертикально
                    if all(board[r+i][c] == 0 for i in range(size)):
                        for i in range(size): 
                            board[r+i][c] = size
                        placed = True
    
    def click(self, e):
        """Обработка кликов мыши"""
        c, r = e.x//self.cell, e.y//self.cell  # Координаты клетки
        
        if self.placement_mode:
            # Режим расстановки кораблей
            if e.char == 'r':  # Клавиша 'r' для поворота (не реализовано)
                pass
            elif self.current_ship < len(self.ships):
                size = self.ships[self.current_ship]
                
                # Пробуем поставить горизонтально
                if c+size <= 8 and all(self.player[r][c+i] == 0 for i in range(size)):
                    for i in range(size): 
                        self.player[r][c+i] = size
                    self.current_ship += 1
                # Пробуем поставить вертикально
                elif r+size <= 8 and all(self.player[r+i][c] == 0 for i in range(size)):
                    for i in range(size): 
                        self.player[r+i][c] = size
                    self.current_ship += 1
                
                # Если все корабли расставлены, переходим в режим боя
                if self.current_ship >= len(self.ships):
                    self.start_battle()
        
        elif self.battle_mode and self.player_turn and not self.game_over:
            # Режим боя, ход игрока
            if not self.player_shots[r][c]:  # Если в эту клетку еще не стреляли
                self.player_shots[r][c] = True
                
                if self.computer[r][c]:  # Попадание
                    self.status.config(text="Попадание!")
                else:  # Промах
                    self.status.config(text="Мимо")
                    self.player_turn = False  # Передаем ход компьютеру
                    self.win.after(500, self.computer_turn)  # Через 0.5 сек ход компьютера
                
                # Проверяем победу
                if self.check_win():
                    self.status.config(text="Вы победили!")
                    self.game_over = True
        
        self.draw()
    
    def computer_turn(self):
        """Ход компьютера (случайный выстрел)"""
        if self.game_over: return
        
        # Выбираем случайную клетку, в которую еще не стреляли
        r, c = random.randint(0,7), random.randint(0,7)
        while self.computer_shots[r][c]:
            r, c = random.randint(0,7), random.randint(0,7)
        
        self.computer_shots[r][c] = True
        
        if self.player[r][c]:  # Попадание
            self.status.config(text="Компьютер попал!")
        else:  # Промах
            self.status.config(text="Ваш ход")
            self.player_turn = True  # Возвращаем ход игроку
        
        # Проверяем победу компьютера
        if self.check_win(player=True):
            self.status.config(text="Компьютер победил!")
            self.game_over = True
        
        self.draw()
    
    def check_win(self, player=False):
        """Проверяет, все ли корабли противника потоплены"""
        board = self.player if player else self.computer
        shots = self.computer_shots if player else self.player_shots
        
        # Если есть корабль, в который не стреляли - игра продолжается
        for r in range(8):
            for c in range(8):
                if board[r][c] and not shots[r][c]:
                    return False
        return True
    
    def draw(self):
        """Отрисовка игры"""
        self.canvas.delete("all")
        
        for r in range(8):
            for c in range(8):
                x, y = c*self.cell, r*self.cell
                
                if self.battle_mode:
                    # В режиме боя показываем только выстрелы игрока
                    if self.player_shots[r][c]:
                        # Попадание или промах
                        color = '#ff6b6b' if self.computer[r][c] else '#4a4a4a'
                    else:
                        color = '#2a2a2a' if (r+c)%2 else '#1a1a1a'
                else:
                    # В режиме расстановки показываем корабли игрока
                    if self.player[r][c]:
                        color = self.c['primary']  # Корабли зеленым
                    else:
                        color = '#2a2a2a' if (r+c)%2 else '#1a1a1a'
                
                self.canvas.create_rectangle(x, y, x+self.cell, y+self.cell,
                                            fill=color, outline='#333')
                
                # В режиме боя показываем выстрелы компьютера
                if self.battle_mode and self.computer_shots[r][c]:
                    if self.player[r][c]:
                        # Попадание по кораблю игрока
                        self.canvas.create_text(x+20, y+20, text='💥', 
                                               font=('Segoe UI Emoji', 20))
                    else:
                        # Промах компьютера
                        self.canvas.create_oval(x+15, y+15, x+25, y+25, fill='black')


# ============= ИГРА 6: ШАХМАТЫ =============
class ChessGame(BaseGame):
    def setup_ui(self):
        super().setup_ui()
        self.title.config(text="♜ ШАХМАТЫ")
        self.cell = 50
        self.canvas.config(width=400, height=400)
        self.canvas.bind('<Button-1>', self.click)  # Клик для выбора и хода
    
    def new_game(self):
        """Начальная расстановка фигур"""
        # Используем символы юникода для шахматных фигур
        self.board = [
            ['♜','♞','♝','♛','♚','♝','♞','♜'],  # Черные фигуры
            ['♟']*8,                               # Черные пешки
            [None]*8, [None]*8, [None]*8, [None]*8, # Пустые клетки
            ['♙']*8,                               # Белые пешки
            ['♖','♘','♗','♕','♔','♗','♘','♖']     # Белые фигуры
        ]
        
        self.selected = None      # Выбранная фигура (r,c)
        self.player_turn = True    # True - белые (игрок), False - черные (компьютер)
        self.game_over = False
        
        self.draw()
        self.status.config(text="Ваш ход (белые)")
    
    def click(self, e):
        """Обработка клика мыши"""
        if not self.player_turn or self.game_over: return
        
        r, c = e.y//self.cell, e.x//self.cell
        
        if self.selected:
            # Если уже выбрана фигура - пытаемся сходить
            if self.move(self.selected[0], self.selected[1], r, c):
                self.selected = None
                self.player_turn = False  # Передаем ход компьютеру
                self.draw()
                self.win.after(500, self.ai_move)  # Ход компьютера через 0.5 сек
            else:
                self.selected = None  # Если ход невозможен, снимаем выделение
        
        elif self.board[r][c] and self.board[r][c] in ['♙','♖','♘','♗','♕','♔']:
            # Выбираем белую фигуру (игрока)
            self.selected = (r,c)
        
        self.draw()
    
    def move(self, r1, c1, r2, c2):
        """Очень упрощенная логика хода (без проверки правил)"""
        if not (0<=r2<8 and 0<=c2<8): return False
        
        piece = self.board[r1][c1]
        target = self.board[r2][c2]
        
        # Можно съесть черную фигуру или пойти на пустую клетку
        if target and target in ['♟','♜','♞','♝','♛','♚']:
            self.board[r2][c2] = piece
            self.board[r1][c1] = None
            return True
        elif not target:
            self.board[r2][c2] = piece
            self.board[r1][c1] = None
            return True
        return False
    
    def ai_move(self):
        """Простой ИИ для черных - случайный ход"""
        if self.game_over: return
        
        moves = []  # Список возможных ходов
        
        # Собираем все возможные ходы для черных фигур
        for r in range(8):
            for c in range(8):
                if self.board[r][c] and self.board[r][c] in ['♟','♜','♞','♝','♛','♚']:
                    for dr in [-1,0,1]:
                        for dc in [-1,0,1]:
                            nr, nc = r+dr, c+dc
                            if 0<=nr<8 and 0<=nc<8:
                                target = self.board[nr][nc]
                                # Можно пойти на пустую или съесть белую фигуру
                                if not target or target in ['♙','♖','♘','♗','♕','♔']:
                                    moves.append((r,c,nr,nc))
        
        if moves:
            # Выбираем случайный ход
            r1,c1,r2,c2 = random.choice(moves)
            self.board[r2][c2] = self.board[r1][c1]
            self.board[r1][c1] = None
        
        self.player_turn = True  # Возвращаем ход игроку
        self.status.config(text="Ваш ход (белые)")
        self.draw()
    
    def draw(self):
        """Отрисовка доски"""
        self.canvas.delete("all")
        
        # Цвета клеток (светлые и темные)
        colors = ['#f0d9b5', '#b58863']
        
        for r in range(8):
            for c in range(8):
                x, y = c*self.cell, r*self.cell
                
                # Рисуем клетку
                self.canvas.create_rectangle(x, y, x+self.cell, y+self.cell,
                                            fill=colors[(r+c)%2])
                
                # Рисуем фигуру, если есть
                if self.board[r][c]:
                    self.canvas.create_text(x+25, y+25, text=self.board[r][c],
                                           font=('Segoe UI Emoji', 30))
                
                # Подсвечиваем выбранную фигуру
                if self.selected == (r,c):
                    self.canvas.create_rectangle(x+2, y+2, x+self.cell-2, y+self.cell-2,
                                                outline=self.c['primary'], width=3)


# ============= ИГРА 7: ШАШКИ =============
class CheckersGame(BaseGame):
    def setup_ui(self):
        super().setup_ui()
        self.title.config(text="● ШАШКИ")
        self.cell = 50
        self.canvas.config(width=400, height=400)
        self.canvas.bind('<Button-1>', self.click)
    
    def new_game(self):
        """Начальная расстановка шашек"""
        self.board = [[None]*8 for _ in range(8)]
        
        for i in range(8):
            for j in range(8):
                if (i+j)%2:  # Только на черных клетках (шашечная доска)
                    if i < 3: 
                        self.board[i][j] = 'b'  # Черные шашки (компьютер) сверху
                    elif i > 4: 
                        self.board[i][j] = 'w'  # Белые шашки (игрок) снизу
        
        self.selected = None
        self.player_turn = True  # Белые ходят первыми
        self.game_over = False
        
        self.draw()
        self.status.config(text="Ваш ход")
    
    def click(self, e):
        """Обработка клика"""
        if not self.player_turn or self.game_over: return
        
        r, c = e.y//self.cell, e.x//self.cell
        
        if self.selected:
            # Если есть выбранная шашка - пробуем сходить
            if self.move(self.selected[0], self.selected[1], r, c):
                self.selected = None
                self.player_turn = False  # Ход компьютеру
                self.draw()
                self.win.after(500, self.ai_move)  # Ход компьютера
            else:
                self.selected = None  # Если ход невозможен, снимаем выделение
        
        elif 0<=r<8 and 0<=c<8 and self.board[r][c] == 'w':
            # Выбираем белую шашку игрока
            self.selected = (r,c)
        
        self.draw()
    
    def move(self, r1, c1, r2, c2):
        """Проверка возможности хода и его выполнение"""
        # Проверка границ, что клетка пуста и что это черная клетка
        if not (0<=r2<8 and 0<=c2<8) or self.board[r2][c2] or (r2+c2)%2==0:
            return False
        
        dr, dc = r2-r1, c2-c1
        
        if abs(dr) == 1 and abs(dc) == 1:  # Простой ход на 1 клетку
            self.board[r2][c2] = self.board[r1][c1]
            self.board[r1][c1] = None
            return True
        
        elif abs(dr) == 2 and abs(dc) == 2:  # Ход со взятием (через шашку)
            mr, mc = (r1+r2)//2, (c1+c2)//2  # Клетка с шашкой противника
            # Проверяем, что там шашка противника
            if self.board[mr][mc] and self.board[mr][mc][0] != self.board[r1][c1][0]:
                self.board[r2][c2] = self.board[r1][c1]
                self.board[r1][c1] = None
                self.board[mr][mc] = None  # Убираем срубленную шашку
                return True
        
        return False
    
    def ai_move(self):
        """ИИ для черных шашек"""
        if self.game_over: return
        
        moves = []      # Обычные ходы
        captures = []   # Ходы со взятием (приоритетные)
        
        # Собираем все возможные ходы для черных шашек
        for r in range(8):
            for c in range(8):
                if self.board[r][c] == 'b':
                    # Проверяем все 4 направления
                    for dr, dc in [(-1,-1), (-1,1), (1,-1), (1,1)]:
                        nr, nc = r+dr, c+dc
                        # Обычный ход
                        if 0<=nr<8 and 0<=nc<8 and not self.board[nr][nc]:
                            moves.append((r,c,nr,nc))
                        
                        # Ход со взятием
                        nr2, nc2 = r+dr*2, c+dc*2
                        mr, mc = r+dr, c+dc
                        if (0<=nr2<8 and 0<=nc2<8 and not self.board[nr2][nc2] and
                            self.board[mr][mc] == 'w'):  # Есть белая шашка для взятия
                            captures.append((r,c,nr2,nc2))
        
        # Выбираем ход: сначала взятие, если есть, иначе обычный ход
        if captures:
            r1,c1,r2,c2 = random.choice(captures)
        elif moves:
            r1,c1,r2,c2 = random.choice(moves)
        else:
            # Если ходов нет - игрок выиграл
            self.game_over = True
            self.status.config(text="Вы выиграли!")
            self.draw()
            return
        
        self.move(r1,c1,r2,c2)  # Выполняем ход
        self.player_turn = True  # Возвращаем ход игроку
        self.status.config(text="Ваш ход")
        self.draw()
    
    def draw(self):
        """Отрисовка доски"""
        self.canvas.delete("all")
        colors = ['#f0d9b5', '#b58863']
        
        for r in range(8):
            for c in range(8):
                x, y = c*self.cell, r*self.cell
                self.canvas.create_rectangle(x, y, x+self.cell, y+self.cell,
                                            fill=colors[(r+c)%2])
                
                if self.board[r][c]:
                    color = 'black' if self.board[r][c][0]=='b' else 'white'
                    self.canvas.create_oval(x+5, y+5, x+self.cell-5, y+self.cell-5,
                                          fill=color, outline='gray')
                
                if self.selected == (r,c):
                    self.canvas.create_rectangle(x+2, y+2, x+self.cell-2, y+self.cell-2,
                                                outline=self.c['primary'], width=3)


# ============= ИГРА 8: РЕВЕРСИ =============
class ReversiGame(BaseGame):
    def setup_ui(self):
        super().setup_ui()
        self.title.config(text="◉ РЕВЕРСИ")
        self.cell = 50
        self.canvas.config(width=400, height=400, bg='green')
        self.canvas.bind('<Button-1>', self.click)
    
    def new_game(self):
        """Начальная расстановка"""
        self.board = [[None]*8 for _ in range(8)]
        # Стартовые 4 фишки в центре
        self.board[3][3] = 'white'
        self.board[3][4] = 'black'
        self.board[4][3] = 'black'
        self.board[4][4] = 'white'
        
        self.player_turn = True  # Черные ходят первыми
        self.game_over = False
        
        self.draw()
        self.status.config(text="Ваш ход (черные)")
    
    def click(self, e):
        """Обработка клика"""
        if not self.player_turn or self.game_over: return
        
        r, c = e.y//self.cell, e.x//self.cell
        
        # Проверяем, можно ли поставить черную фишку
        if self.valid_move(r, c, 'black'):
            self.place(r, c, 'black')  # Ставим фишку
            self.player_turn = False    # Ход компьютеру
            self.draw()
            self.win.after(500, self.ai_move)  # Ход компьютера
    
    def valid_move(self, r, c, color):
        """Проверяет, можно ли поставить фишку в клетку (r,c)"""
        if not (0<=r<8 and 0<=c<8) or self.board[r][c]: 
            return False
        
        opp = 'white' if color == 'black' else 'black'
        # Все 8 направлений
        dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        
        for dr, dc in dirs:
            nr, nc = r+dr, c+dc
            # Ищем клетку с фишкой противника
            if 0<=nr<8 and 0<=nc<8 and self.board[nr][nc] == opp:
                nr += dr; nc += dc
                # Продолжаем двигаться в том же направлении
                while 0<=nr<8 and 0<=nc<8:
                    if self.board[nr][nc] is None: 
                        break
                    if self.board[nr][nc] == color: 
                        return True  # Нашли свою фишку - ход возможен
                    nr += dr; nc += dc
        return False
    
    def place(self, r, c, color):
        """Ставит фишку и переворачивает захваченные фишки противника"""
        self.board[r][c] = color
        opp = 'white' if color == 'black' else 'black'
        dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        
        for dr, dc in dirs:
            flip = []  # Фишки для переворота в этом направлении
            nr, nc = r+dr, c+dc
            
            # Собираем фишки противника подряд
            while 0<=nr<8 and 0<=nc<8 and self.board[nr][nc] == opp:
                flip.append((nr,nc))
                nr += dr; nc += dc
            
            # Если в конце цепочки нашли свою фишку - переворачиваем
            if 0<=nr<8 and 0<=nc<8 and self.board[nr][nc] == color:
                for fr, fc in flip:
                    self.board[fr][fc] = color
    
    def ai_move(self):
        """ИИ для белых фишек"""
        if self.game_over: return
        
        # Собираем все возможные ходы для белых
        moves = []
        for r in range(8):
            for c in range(8):
                if self.valid_move(r, c, 'white'):
                    moves.append((r,c))
        
        if moves:
            # Выбираем случайный ход
            r, c = random.choice(moves)
            self.place(r, c, 'white')
        else:
            # Если ходов нет - игра окончена
            self.game_over = True
        
        self.player_turn = True  # Возвращаем ход игроку
        self.draw()
    
    def draw(self):
        """Отрисовка доски"""
        self.canvas.delete("all")
        
        for r in range(8):
            for c in range(8):
                x, y = c*self.cell, r*self.cell
                self.canvas.create_rectangle(x, y, x+self.cell, y+self.cell, outline='black')
                
                if self.board[r][c]:
                    color = 'black' if self.board[r][c]=='black' else 'white'
                    self.canvas.create_oval(x+5, y+5, x+self.cell-5, y+self.cell-5,
                                          fill=color, outline='gray')
                elif self.valid_move(r, c, 'black') and self.player_turn:
                    # Показываем возможные ходы желтым
                    self.canvas.create_oval(x+15, y+15, x+self.cell-15, y+self.cell-15,
                                          fill='yellow')
        
        # Считаем и показываем счет
        black = sum(row.count('black') for row in self.board)
        white = sum(row.count('white') for row in self.board)
        self.status.config(text=f"Ч:{black}  Б:{white}")


# ============= ИГРА 9: ПИНГ-ПОНГ =============
class PongGame(BaseGame):
    def setup_ui(self):
        super().setup_ui()
        self.title.config(text="🏓 ПИНГ-ПОНГ")
        self.canvas.config(width=600, height=400, bg='black')
        
        # Управление: w/s для левой ракетки, стрелки для правой
        self.win.bind('<KeyPress-w>', lambda e: self.move(1, -15))
        self.win.bind('<KeyPress-s>', lambda e: self.move(1, 15))
        self.win.bind('<KeyPress-Up>', lambda e: self.move(2, -15))
        self.win.bind('<KeyPress-Down>', lambda e: self.move(2, 15))
        self.win.focus_set()
    
    def new_game(self):
        """Начинает новую игру"""
        self.p1y = self.p2y = 160  # Позиции ракеток
        self.ball = [300, 200, 4, 4]  # [x, y, скорость_x, скорость_y]
        self.score = [0,0]  # Счет [игрок1, игрок2]
        self.running = True
        self.update()
    
    def move(self, player, dy):
        """Движение ракетки"""
        if player == 1:
            self.p1y = max(0, min(320, self.p1y + dy))  # Ограничиваем сверху/снизу
        else:
            self.p2y = max(0, min(320, self.p2y + dy))
    
    def update(self):
        """Игровой цикл"""
        if not self.running: return
        
        # Движение мяча
        self.ball[0] += self.ball[2]
        self.ball[1] += self.ball[3]
        
        # Отскок от верхней/нижней стены
        if self.ball[1] <= 0 or self.ball[1] >= 390:
            self.ball[3] *= -1
        
        # Отскок от левой ракетки
        if (self.ball[0] <= 10 and self.p1y <= self.ball[1] <= self.p1y+80):
            self.ball[2] = abs(self.ball[2])  # Меняем направление на право
        
        # Отскок от правой ракетки
        if (self.ball[0] >= 580 and self.p2y <= self.ball[1] <= self.p2y+80):
            self.ball[2] = -abs(self.ball[2])  # Меняем направление на лево
        
        # Голы
        if self.ball[0] <= 0:  # Мяч ушел влево
            self.score[1] += 1  # Очко правому игроку
            self.ball = [300,200,4,4]  # Сбрасываем мяч в центр
        elif self.ball[0] >= 590:  # Мяч ушел вправо
            self.score[0] += 1  # Очко левому игроку
            self.ball = [300,200,-4,4]  # Мяч летит влево
        
        self.draw()
        self.win.after(30, self.update)  # Обновляем каждые 30 мс (~33 FPS)
    
    def draw(self):
        """Отрисовка игры"""
        self.canvas.delete("all")
        
        # Центральная линия
        self.canvas.create_line(300,0,300,400, fill='white', dash=(5,5))
        
        # Ракетки
        self.canvas.create_rectangle(0, self.p1y, 10, self.p1y+80, fill='white')
        self.canvas.create_rectangle(590, self.p2y, 600, self.p2y+80, fill='white')
        
        # Мяч
        self.canvas.create_oval(self.ball[0]-5, self.ball[1]-5, 
                               self.ball[0]+5, self.ball[1]+5, fill='white')
        
        # Счет
        self.status.config(text=f"{self.score[0]} : {self.score[1]}")


# ============= ИГРА 10: АРКАНОИД =============
class ArkanoidGame(BaseGame):
    def setup_ui(self):
        super().setup_ui()
        self.title.config(text="🧱 АРКАНОИД")
        self.canvas.config(width=600, height=400, bg='black')
        
        # Управление стрелками
        self.win.bind('<Left>', lambda e: self.move(-20))
        self.win.bind('<Right>', lambda e: self.move(20))
        self.win.focus_set()
    
    def new_game(self):
        """Начинает новую игру"""
        self.paddle = 250  # Позиция ракетки
        self.ball = [300, 350, 4, -4]  # [x, y, скорость_x, скорость_y]
        self.bricks = []  # Список кирпичей
        self.score = 0
        self.running = True
        
        # Создаем кирпичи
        colors = ['red', 'orange', 'yellow', 'green', 'blue']
        for i in range(5):  # 5 рядов
            for j in range(8):  # 8 кирпичей в ряду
                self.bricks.append({
                    'x': j*75+5,          # x координата
                    'y': i*25+30,          # y координата
                    'w': 70,                # ширина
                    'h': 20,                # высота
                    'color': colors[i]      # цвет
                })
        self.update()
    
    def move(self, dx):
        """Движение ракетки"""
        self.paddle = max(0, min(500, self.paddle + dx))  # Ограничиваем по краям
    
    def update(self):
        """Игровой цикл"""
        if not self.running: return
        
        # Движение мяча
        self.ball[0] += self.ball[2]
        self.ball[1] += self.ball[3]
        
        # Отскок от стен
        if self.ball[0] <= 0 or self.ball[0] >= 590:
            self.ball[2] *= -1
        if self.ball[1] <= 0:
            self.ball[3] *= -1
        
        # Отскок от ракетки
        if (self.ball[1] >= 370 and 
            self.paddle <= self.ball[0] <= self.paddle+100):
            self.ball[3] = -abs(self.ball[3])  # Отскок вверх
        
        # Проверка столкновения с кирпичами
        for b in self.bricks[:]:  # Проходим по копии списка
            if (b['x'] <= self.ball[0] <= b['x']+b['w'] and
                b['y'] <= self.ball[1] <= b['y']+b['h']):
                self.bricks.remove(b)  # Убираем кирпич
                self.ball[3] *= -1      # Меняем направление мяча
                self.score += 10        # Увеличиваем счет
        
        # Проверка окончания игры
        if self.ball[1] > 400:  # Мяч упал вниз
            self.running = False
        if not self.bricks:  # Все кирпичи разбиты
            self.running = False
        
        self.draw()
        if self.running:
            self.win.after(30, self.update)  # Следующий кадр
    
    def draw(self):
        """Отрисовка игры"""
        self.canvas.delete("all")
        
        # Рисуем кирпичи
        for b in self.bricks:
            self.canvas.create_rectangle(b['x'], b['y'], 
                                        b['x']+b['w'], b['y']+b['h'],
                                        fill=b['color'])
        
        # Ракетка
        self.canvas.create_rectangle(self.paddle, 380, 
                                    self.paddle+100, 395, fill='white')
        
        # Мяч
        self.canvas.create_oval(self.ball[0]-5, self.ball[1]-5,
                               self.ball[0]+5, self.ball[1]+5, fill='white')
        
        self.status.config(text=f"Счет: {self.score}")


# ============= ИГРА 11: FLAPPY BIRD =============
class FlappyBirdGame(BaseGame):
    def setup_ui(self):
        super().setup_ui()
        self.title.config(text="🐦 FLAPPY BIRD")
        self.canvas.config(width=400, height=600, bg='lightblue')
        
        # Пробел для прыжка
        self.win.bind('<space>', lambda e: self.jump())
        self.win.focus_set()
    
    def new_game(self):
        """Начинает новую игру"""
        self.bird = 300  # Позиция птицы по Y
        self.vel = 0     # Вертикальная скорость
        self.pipes = []  # Список труб
        self.score = 0
        self.running = True
        
        self.add_pipe()  # Добавляем первую трубу
        self.update()
    
    def add_pipe(self):
        """Добавляет новую пару труб"""
        h = random.randint(150, 400)  # Высота верхней трубы
        self.pipes.append({
            'x': 400,          # X координата (появляется справа)
            'top': h,          # Высота верхней трубы
            'bottom': h+150,   # Y начала нижней трубы
            'passed': False    # Пролетели ли мимо
        })
    
    def jump(self):
        """Прыжок птицы"""
        if self.running:
            self.vel = -8  # Даем импульс вверх
    
    def update(self):
        """Игровой цикл"""
        if not self.running: return
        
        # Физика птицы
        self.vel += 0.5      # Гравитация
        self.bird += self.vel # Движение
        
        # Движение труб
        for p in self.pipes[:]:
            p['x'] -= 3  # Двигаем влево
            
            # Удаляем трубы за экраном
            if p['x'] < -60:
                self.pipes.remove(p)
            
            # Проверка, пролетели ли мимо трубы
            if not p['passed'] and p['x'] < 50:
                p['passed'] = True
                self.score += 1
        
        # Добавляем новые трубы
        if len(self.pipes) < 3 and random.random() < 0.02:
            self.add_pipe()
        
        # Проверка столкновений с трубами
        for p in self.pipes:
            if (p['x'] < 90 and p['x']+60 > 50):  # Пересечение по X
                if self.bird < p['top'] or self.bird+30 > p['bottom']:
                    self.running = False  # Столкновение
        
        # Проверка выхода за границы
        if self.bird <= 0 or self.bird >= 570:
            self.running = False
        
        self.draw()
        if self.running:
            self.win.after(30, self.update)
    
    def draw(self):
        """Отрисовка игры"""
        self.canvas.delete("all")
        
        # Рисуем трубы
        for p in self.pipes:
            # Верхняя труба
            self.canvas.create_rectangle(p['x'], 0, 
                                        p['x']+60, p['top'], fill='green')
            # Нижняя труба
            self.canvas.create_rectangle(p['x'], p['bottom'], 
                                        p['x']+60, 600, fill='green')
        
        # Рисуем птицу
        self.canvas.create_oval(50, self.bird, 80, self.bird+30, fill='yellow')
        # Глаз
        self.canvas.create_oval(65, self.bird+5, 70, self.bird+10, fill='black')
        
        self.status.config(text=f"Счет: {self.score}")


# ============= ЗАПУСК ПРИЛОЖЕНИЯ =============
if __name__ == "__main__":
    # Создаем экземпляр главного класса и запускаем главный цикл обработки событий
    Game11v1().root.mainloop()