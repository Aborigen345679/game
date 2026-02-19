import tkinter as tk  # Импортируем библиотеку для создания графического интерфейса
import random  # Импортируем модуль для генерации случайных чисел

# ============================================================================
# ГЛАВНЫЙ КЛАСС ПРИЛОЖЕНИЯ - Game11v1
# ============================================================================
# Этот класс создает главное окно с меню из 11 игр. Он отвечает за:
# 1. Создание главного окна с темной темой
# 2. Отображение сетки с карточками всех доступных игр (3 колонки)
# 3. Открытие выбранной игры в новом окне
# ============================================================================

class Game11v1:
    def __init__(self):
        """Конструктор класса - инициализирует главное окно и создает меню"""
        # Создаем главное окно приложения
        self.root = tk.Tk()  # Tk() - корневое окно программы
        self.root.title("11v1 GAMING HUB")  # Устанавливаем заголовок окна
        self.root.geometry("1200x700")  # Размер окна: ширина 1200px, высота 700px
        self.root.configure(bg='#0a0a0a')  # Устанавливаем темно-серый фон окна
        
        # Словарь с цветовой схемой приложения
        # Все цвета хранятся в одном месте для единообразия и легкой смены темы
        self.colors = {
            'bg': '#0a0a0a',      # Основной темный фон (почти черный)
            'card': '#1a1a1a',     # Фон для карточек игр (чуть светлее основного)
            'primary': '#00ff88',   # Основной акцентный цвет (ярко-зеленый неон)
            'secondary': '#ff3366', # Второстепенный акцентный цвет (ярко-розовый)
            'text': '#ffffff',      # Основной цвет текста (белый)
            'text2': '#b0b0b0'      # Второстепенный цвет текста (светло-серый)
        }
        
        # Вызываем метод создания главного меню
        self.create_menu()
    
    def create_menu(self):
        """
        Создает главное меню с карточками всех игр.
        Игры располагаются в сетке 3 колонки.
        Каждая карточка содержит: эмодзи, название и кнопку "ИГРАТЬ".
        """
        # Создаем заголовок меню - большой текст в верхней части окна
        tk.Label(self.root, 
                text="⚡ 11v1 GAMING HUB ⚡",  # Текст заголовка с эмодзи
                font=('Helvetica', 28, 'bold'),  # Шрифт Helvetica, размер 28, жирный
                bg=self.colors['bg'],  # Фон из словаря цветов
                fg=self.colors['primary']  # Цвет текста (зеленый неон)
               ).pack(pady=20)  # Размещаем с отступом сверху/снизу 20 пикселей
        
        # Создаем фрейм-контейнер для сетки с играми
        # Frame - это прямоугольная область для группировки виджетов
        game_grid = tk.Frame(self.root, bg=self.colors['bg'])
        game_grid.pack(expand=True)  # expand=True - фрейм будет расширяться при изменении окна
        
        # Список всех игр в формате: (эмодзи, название, класс игры)
        # Класс игры - это ссылка на класс, который будет создан при нажатии кнопки
        games = [
            ("🐍", "Змейка", SnakeGame),                    # Игра 1
            ("🧩", "Тетрис", TetrisGame),                    # Игра 2
            ("🎯", "2048", Game2048),                        # Игра 3
            ("💣", "Сапер", MinesweeperGame),                # Игра 4
            ("⚓", "Морской бой", BattleshipGame),            # Игра 5
            ("●", "Шашки", CheckersGame),                    # Игра 6
            ("◉", "Реверси", ReversiGame),                   # Игра 7
            ("❌⭕", "Крестики-нолики", TicTacToeGame),       # Игра 8 (вместо Пинг-понга)
            ("🧱", "Арканоид", ArkanoidGame),                 # Игра 9
            ("🐦", "Flappy Bird", FlappyBirdGame),            # Игра 10
            ("✂️", "Камень-ножницы-бумага", RPSGame)          # Игра 11
        ]
        
        # Создаем карточки для каждой игры в цикле
        # enumerate возвращает индекс (i) и значение (emoji, name, game) для каждого элемента
        for i, (emoji, name, game_class) in enumerate(games):
            # Создаем карточку - отдельный фрейм для каждой игры
            card = tk.Frame(game_grid, 
                           bg=self.colors['card'],  # Цвет фона карточки
                           width=300,  # Ширина карточки 300px
                           height=180  # Высота карточки 180px
                          )
            
            # Размещаем карточку в сетке:
            # row = i//3 (целочисленное деление) - определяет строку (0,1,2,3...)
            # column = i%3 (остаток от деления) - определяет колонку (0,1,2)
            # Это создает сетку с 3 колонками и автоматическим количеством строк
            card.grid(row=i//3, column=i%3, padx=10, pady=10)
            
            # pack_propagate(False) запрещает изменение размера карточки под содержимое
            # Без этого карточка могла бы сжаться до размеров внутренних виджетов
            card.pack_propagate(False)
            
            # Добавляем эмодзи игры в верхней части карточки
            tk.Label(card, 
                    text=emoji,  # Эмодзи из списка
                    font=('Segoe UI Emoji', 40),  # Специальный шрифт для поддержки эмодзи
                    bg=self.colors['card'],  # Фон карточки
                    fg=self.colors['primary']  # Цвет эмодзи (зеленый)
                   ).pack(pady=10)  # Отступ сверху/снизу 10 пикселей
            
            # Добавляем название игры под эмодзи
            tk.Label(card, 
                    text=name,  # Название из списка
                    font=('Helvetica', 14, 'bold'),  # Шрифт Helvetica, размер 14, жирный
                    bg=self.colors['card'],  # Фон карточки
                    fg=self.colors['text']  # Белый цвет текста
                   ).pack()  # Размещаем без дополнительных отступов
            
            # Добавляем кнопку "ИГРАТЬ" в нижней части карточки
            # lambda g=game_class: self.open_game(g) - создает функцию, которая при нажатии
            # вызывает open_game с текущим классом игры. Используем g=game_class для 
            # "замыкания" значения, чтобы каждая кнопка запомнила свою игру
            tk.Button(card, 
                     text="ИГРАТЬ",  # Текст на кнопке
                     font=('Helvetica', 12, 'bold'),  # Шрифт Helvetica, размер 12, жирный
                     bg=self.colors['primary'],  # Зеленый фон кнопки
                     fg=self.colors['bg'],  # Темный цвет текста
                     command=lambda g=game_class: self.open_game(g)  # Функция при нажатии
                    ).pack(side='bottom', fill='x', ipady=5)  # side='bottom' - внизу, fill='x' - растянуть по ширине, ipady=5 - внутренний отступ по вертикали
    
    def open_game(self, game_class):
        """
        Открывает окно с выбранной игрой.
        Создает новое окно поверх главного и запускает в нем игру.
        
        Аргументы:
            game_class: класс игры, экземпляр которого нужно создать
        """
        # Создаем новое окно поверх главного (Toplevel - дочернее окно)
        game_window = tk.Toplevel(self.root)
        game_window.title("11v1 - Игра")  # Заголовок окна
        game_window.geometry("800x600")  # Размер окна игры
        game_window.configure(bg=self.colors['bg'])  # Устанавливаем темный фон
        
        # Делаем окно модальным - блокирует взаимодействие с главным окном
        game_window.transient(self.root)  # Указываем, что это окно - временное по отношению к главному
        game_window.grab_set()  # Захватываем все события мыши и клавиатуры
        
        # Создаем экземпляр выбранной игры, передавая окно и цвета
        game_class(game_window, self.colors)


# ============================================================================
# БАЗОВЫЙ КЛАСС ДЛЯ ВСЕХ ИГР - BaseGame
# ============================================================================
# Этот класс является родительским для всех игр. Он содержит общую логику:
# - Создание базового интерфейса (заголовок, холст, панель с кнопками)
# - Отображение счета и статуса игры
# - Кнопку новой игры
# 
# Все конкретные игры наследуются от этого класса и переопределяют методы:
# - setup_ui() - для создания специфического интерфейса
# - new_game() - для инициализации новой игры
# - draw() - для отрисовки текущего состояния
# ============================================================================

class BaseGame:
    def __init__(self, window, colors):
        """
        Конструктор базового класса.
        
        Аргументы:
            window: окно, в котором будет отображаться игра
            colors: словарь с цветовой схемой
        """
        self.win = window  # Сохраняем ссылку на окно для использования в дочерних классах
        self.c = colors    # Сохраняем цветовую схему для использования в дочерних классах
        
        self.setup_ui()    # Создаем пользовательский интерфейс
        self.new_game()    # Запускаем новую игру
    
    def setup_ui(self):
        """
        Создает общие элементы интерфейса для всех игр:
        - Заголовок игры
        - Холст для рисования
        - Нижнюю панель со статусом, счетом и кнопкой новой игры
        """
        # Заголовок игры (будет изменен в конкретных играх через self.title.config())
        self.title = tk.Label(self.win, 
                              font=('Helvetica', 24, 'bold'),  # Крупный жирный шрифт
                              bg=self.c['bg'],  # Темный фон
                              fg=self.c['primary'])  # Зеленый цвет текста
        self.title.pack(pady=10)  # Отступ сверху/снизу 10 пикселей
        
        # Холст для рисования игры
        # Canvas - это область, на которой можно рисовать графические примитивы
        self.canvas = tk.Canvas(self.win, 
                                bg=self.c['bg'],  # Темный фон
                                highlightthickness=2,  # Толщина рамки вокруг холста
                                highlightbackground=self.c['card'])  # Цвет рамки
        self.canvas.pack(pady=10)  # Отступ сверху/снизу 10 пикселей
        
        # Нижняя панель с информацией и кнопками
        # Frame для группировки элементов управления
        control_frame = tk.Frame(self.win, bg=self.c['bg'])
        control_frame.pack()  # Размещаем панель
        
        # Метка для отображения статуса игры (например, "Ваш ход" или "Игра окончена")
        self.status = tk.Label(control_frame, 
                               font=('Helvetica', 12),  # Обычный шрифт
                               bg=self.c['bg'],  # Темный фон
                               fg=self.c['text2'])  # Серый цвет текста
        self.status.pack(side='left', padx=10)  # Слева, с отступом 10px
        
        # Метка для отображения счета
        self.score_label = tk.Label(control_frame, 
                                    font=('Helvetica', 12, 'bold'),  # Жирный шрифт
                                    bg=self.c['bg'],  # Темный фон
                                    fg=self.c['primary'])  # Зеленый цвет текста
        self.score_label.pack(side='left', padx=10)  # Слева, с отступом 10px
        
        # Кнопка новой игры (перезапуска)
        # При нажатии вызывает метод new_game() для перезапуска игры
        tk.Button(control_frame, 
                  text="🔄 Новая игра",  # Текст с эмодзи
                  font=('Helvetica', 11, 'bold'),  # Жирный шрифт
                  bg=self.c['primary'],  # Зеленый фон
                  fg=self.c['bg'],  # Темный текст
                  command=self.new_game  # Функция при нажатии
                 ).pack(side='right', padx=10)  # Справа, с отступом 10px
    
    def new_game(self):
        """
        Метод для переопределения в конкретных играх.
        Должен инициализировать новую игру: создать начальное состояние,
        сбросить счет и т.д.
        """
        pass  # pass означает "ничего не делать" - это заглушка


# ============================================================================
# ИГРА 1: ЗМЕЙКА (SnakeGame)
# ============================================================================


class SnakeGame(BaseGame):
    def setup_ui(self):
        """Настройка специфического интерфейса для Змейки"""
        super().setup_ui()  # Вызываем метод родительского класса для создания базового интерфейса
        self.title.config(text="🐍 ЗМЕЙКА")  # Устанавливаем заголовок с эмодзи
        self.cell_size = 20  # Размер одной клетки в пикселях
        self.canvas.config(width=400, height=400)  # Размер холста 400x400 пикселей (20x20 клеток)
        
        # Привязываем нажатия клавиш к методу key
        # <KeyPress> - событие нажатия любой клавиши
        self.win.bind('<KeyPress>', self.key)
        self.win.focus_set()  # Устанавливаем фокус на окно для приема клавиш
    
    def new_game(self):
        """Начинает новую игру - инициализирует все переменные"""
        # Начальная позиция змейки: список кортежей (x, y)
        # Голова - первый элемент, хвост - последний
        self.snake = [(10,10), (9,10), (8,10)]  # Змейка из трех клеток
        self.direction = (1,0)  # Направление движения: (dx, dy) - (1,0) означает вправо
        self.food = self.spawn_food()  # Создаем еду в случайном месте
        self.score = 0  # Начальный счет
        self.game_over = False  # Флаг окончания игры
        
        self.update()  # Запускаем игровой цикл
    
    def spawn_food(self):
        """
        Создает еду в случайном месте, где нет змейки.
        Использует бесконечный цикл while True, который прерывается только
        когда найдено свободное место.
        """
        while True:  # Бесконечный цикл
            # random.randint(0,19) генерирует случайное целое число от 0 до 19
            food_x = random.randint(0, 19)
            food_y = random.randint(0, 19)
            food_pos = (food_x, food_y)
            
            # Если клетка свободна (не занята змейкой)
            if food_pos not in self.snake:
                return food_pos  # Возвращаем координаты и выходим из цикла
    
    def key(self, event):
        """
        Обрабатывает нажатия клавиш.
        Поддерживаются стрелки и WASD.
        Запрещает разворот на 180 градусов.
        
        Аргументы:
            event: объект события, содержащий информацию о нажатой клавише
        """
        # Словарь соответствия клавиш направлениям
        # Ключ - название клавиши, значение - вектор направления (dx, dy)
        key_directions = {
            'Up': (0, -1), 'Down': (0, 1), 'Left': (-1, 0), 'Right': (1, 0),
            'w': (0, -1), 's': (0, 1), 'a': (-1, 0), 'd': (1, 0)
        }
        
        # Проверяем, есть ли нажатая клавиша в словаре
        if event.keysym in key_directions:
            new_direction = key_directions[event.keysym]  # Получаем новое направление
            
            # Запрещаем разворот на 180 градусов
            # Проверяем, что новое направление не противоположно текущему
            # Противоположное направление: (dx, dy) -> (-dx, -dy)
            if (new_direction[0] != -self.direction[0] or 
                new_direction[1] != -self.direction[1]):
                self.direction = new_direction  # Меняем направление
    
    def update(self):
        """
        Игровой цикл - обновляет состояние игры каждые 150 мс.
        Вычисляет новую позицию головы, проверяет столкновения,
        обрабатывает съедание еды и рост змейки.
        """
        if self.game_over:  # Если игра окончена, ничего не делаем
            return
        
        # Вычисляем новую голову змейки
        # Текущая голова: self.snake[0]
        # Прибавляем вектор направления
        head_x = self.snake[0][0] + self.direction[0]
        head_y = self.snake[0][1] + self.direction[1]
        new_head = (head_x, head_y)
        
        # Проверка столкновения со стенами
        # Если голова выходит за границы поля (0-19)
        if (head_x < 0 or head_x >= 20 or  # Выход за левую/правую границу
            head_y < 0 or head_y >= 20):   # Выход за верхнюю/нижнюю границу
            self.game_over = True
            self.draw()  # Перерисовываем для отображения сообщения о конце игры
            return
        
        # Проверка столкновения с самой собой
        if new_head in self.snake:
            self.game_over = True
            self.draw()
            return
        
        # Добавляем новую голову в начало списка
        self.snake.insert(0, new_head)
        
        # Проверка, съела ли змейка еду
        if new_head == self.food:
            self.score += 10  # Увеличиваем счет
            self.food = self.spawn_food()  # Создаем новую еду
            # Хвост не удаляем - змейка растет
        else:
            # Если еда не съедена, удаляем хвост (последний элемент)
            self.snake.pop()
        
        self.draw()  # Перерисовываем экран
        
        # Планируем следующий вызов update через 150 миллисекунд
        # Это создает бесконечный цикл обновления
        self.win.after(150, self.update)
    
    def draw(self):
        """Отрисовывает текущее состояние игры на холсте"""
        self.canvas.delete("all")  # Очищаем холст (удаляем все нарисованные объекты)
        
        # Рисуем сетку (клетки поля)
        for i in range(20):  # Проходим по всем x
            for j in range(20):  # Проходим по всем y
                # Вычисляем координаты на холсте
                x1 = i * self.cell_size
                y1 = j * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                
                # Чередуем цвета клеток для шахматного эффекта
                # (i+j)%2 дает чередование: 0,1,0,1...
                color = '#2a2a2a' if (i + j) % 2 else '#1a1a1a'
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='')
        
        # Рисуем змейку
        for i, segment in enumerate(self.snake):
            # Координаты сегмента с отступом 2px для создания промежутков между сегментами
            x1 = segment[0] * self.cell_size + 2
            y1 = segment[1] * self.cell_size + 2
            x2 = x1 + self.cell_size - 4
            y2 = y1 + self.cell_size - 4
            
            # Голова - основным цветом (зеленым), тело - вторичным (розовым)
            color = self.c['primary'] if i == 0 else self.c['secondary']
            
            # Рисуем овал (круг) - сегмент змейки
            self.canvas.create_oval(x1, y1, x2, y2, fill=color, outline='')
        
        # Рисуем еду (в виде кружка)
        # Вычисляем центр клетки с едой
        food_center_x = self.food[0] * self.cell_size + self.cell_size // 2
        food_center_y = self.food[1] * self.cell_size + self.cell_size // 2
        
        # Рисуем круг радиусом 6px
        self.canvas.create_oval(food_center_x - 6, food_center_y - 6,
                                food_center_x + 6, food_center_y + 6,
                                fill=self.c['secondary'], outline='')
        
        # Если игра окончена, показываем сообщение
        if self.game_over:
            self.canvas.create_text(200, 200,  # Центр холста (400/2=200)
                                   text=f"ИГРА ОКОНЧЕНА\nСчет: {self.score}",
                                   fill='red', 
                                   font=('Helvetica', 20, 'bold'), 
                                   justify='center')  # Выравнивание текста по центру
        
        # Обновляем текст статуса и счета
        self.score_label.config(text=f"Счет: {self.score}")


# ============================================================================
# ИГРА 2: ТЕТРИС (TetrisGame)
# ============================================================================


class TetrisGame(BaseGame):
    def setup_ui(self):
        """Настройка интерфейса для Тетриса"""
        super().setup_ui()
        self.title.config(text="🧩 ТЕТРИС")
        self.cell_size = 25  # Размер одной клетки в пикселях
        self.canvas.config(width=250, height=500)  # Поле 10x20 клеток
        
        # Словарь всех возможных фигур тетриса (тетрамино)
        # Каждая фигура представлена матрицей: 1 - есть блок, 0 - пусто
        self.shapes = {
            'I': [[1, 1, 1, 1]],  # Палочка - 4 блока в ряд
            'O': [[1, 1], [1, 1]],  # Квадрат - 2x2 блока
            'T': [[0, 1, 0], [1, 1, 1]],  # Т-образная
            'S': [[0, 1, 1], [1, 1, 0]],  # S-образная
            'Z': [[1, 1, 0], [0, 1, 1]],  # Z-образная
            'L': [[1, 0, 0], [1, 1, 1]],  # Г-образная (поворот влево)
            'J': [[0, 0, 1], [1, 1, 1]]   # Г-образная (поворот вправо)
        }
        
        # Цвета для каждой фигуры
        self.shape_colors = {
            'I': '#00ffff', 'O': '#ffff00', 'T': '#ff00ff',
            'S': '#00ff00', 'Z': '#ff0000', 'L': '#ff8800', 'J': '#0000ff'
        }
        
        # Привязываем клавиши управления
        self.win.bind('<Left>', lambda e: self.move_piece(-1))   # Стрелка влево
        self.win.bind('<Right>', lambda e: self.move_piece(1))   # Стрелка вправо
        self.win.bind('<Down>', lambda e: self.soft_drop())      # Стрелка вниз (ускорение)
        self.win.bind('<Up>', lambda e: self.rotate_piece())     # Стрелка вверх (поворот)
        self.win.focus_set()
    
    def new_game(self):
        """Начинает новую игру - создает пустое поле и первую фигуру"""
        # Создаем пустое игровое поле 10x20
        # board[y][x] - значение: 0 - пусто, иначе - цвет фигуры
        self.board = [[0] * 10 for _ in range(20)]
        self.score = 0
        self.game_over = False
        self.current_piece = None  # Текущая падающая фигура
        self.spawn_new_piece()  # Создаем первую фигуру
        self.update()
    
    def spawn_new_piece(self):
        """Создает новую случайную фигуру в верхней части поля"""
        piece_name = random.choice(list(self.shapes.keys()))
        
        # Создаем словарь с информацией о фигуре
        self.current_piece = {
            'shape': self.shapes[piece_name],  # Матрица фигуры
            'color': self.shape_colors[piece_name],  # Цвет фигуры
            'x': 5 - len(self.shapes[piece_name][0]) // 2,  # Центрируем по горизонтали
            'y': 0  # Начинаем с верхней границы
        }
        
        # Проверяем, не накладывается ли новая фигура на уже занятые клетки
        if self.check_collision():
            self.game_over = True  # Если да - игра окончена
    
    def check_collision(self):
        """
        Проверяет столкновение текущей фигуры с границами или другими фигурами.
        Возвращает True, если есть столкновение.
        """
        for y, row in enumerate(self.current_piece['shape']):
            for x, cell in enumerate(row):
                if cell:  # Если клетка фигуры не пуста
                    # Вычисляем координаты на поле
                    board_x = self.current_piece['x'] + x
                    board_y = self.current_piece['y'] + y
                    
                    # Проверяем выход за границы
                    if (board_x < 0 or board_x >= 10 or board_y >= 20):
                        return True
                    
                    # Проверяем столкновение с другой фигурой
                    if board_y >= 0 and self.board[board_y][board_x]:
                        return True
        return False
    
    def move_piece(self, dx):
        """Перемещает фигуру по горизонтали"""
        if self.game_over or not self.current_piece:
            return
        
        self.current_piece['x'] += dx
        
        if self.check_collision():
            self.current_piece['x'] -= dx
    
    def rotate_piece(self):
        """Поворачивает фигуру на 90 градусов по часовой стрелке"""
        if self.game_over or not self.current_piece:
            return
        
        old_shape = self.current_piece['shape']
        # Поворачиваем матрицу на 90 градусов по часовой стрелке
        rotated = [list(row) for row in zip(*old_shape[::-1])]
        self.current_piece['shape'] = rotated
        
        if self.check_collision():
            self.current_piece['shape'] = old_shape
    
    def soft_drop(self):
        """Опускает фигуру на одну клетку вниз (мягкое падение)"""
        if self.game_over or not self.current_piece:
            return
        
        self.current_piece['y'] += 1
        
        if self.check_collision():
            self.current_piece['y'] -= 1
            self.lock_piece()
            self.spawn_new_piece()
    
    def lock_piece(self):
        """Фиксирует текущую фигуру на игровом поле"""
        for y, row in enumerate(self.current_piece['shape']):
            for x, cell in enumerate(row):
                if cell:
                    board_y = self.current_piece['y'] + y
                    board_x = self.current_piece['x'] + x
                    if 0 <= board_y < 20:
                        self.board[board_y][board_x] = self.current_piece['color']
        
        self.clear_lines()
    
    def clear_lines(self):
        """Проверяет и удаляет заполненные линии, начисляет очки"""
        lines_cleared = 0
        y = 19  # Начинаем с нижней строки
        
        while y >= 0:
            if all(self.board[y]):  # Если вся строка заполнена
                del self.board[y]  # Удаляем текущую строку
                self.board.insert(0, [0] * 10)  # Добавляем новую пустую строку сверху
                lines_cleared += 1
            else:
                y -= 1
        
        # Начисляем очки за линии: 1 - 100, 2 - 300, 3 - 500, 4 - 800
        line_scores = [0, 100, 300, 500, 800]
        self.score += line_scores[lines_cleared]
    
    def update(self):
        """Игровой цикл - обновляется каждые 500 мс"""
        if not self.game_over and self.current_piece:
            self.soft_drop()
            self.draw()
            self.win.after(500, self.update)
    
    def draw(self):
        """Отрисовка игры"""
        self.canvas.delete("all")
        
        # Рисуем игровое поле
        for y in range(20):
            for x in range(10):
                x1 = x * self.cell_size
                y1 = y * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                
                if self.board[y][x]:
                    color = self.board[y][x]
                else:
                    color = '#2a2a2a' if (x + y) % 2 else '#1a1a1a'
                
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='')
        
        # Рисуем текущую падающую фигуру
        if self.current_piece and not self.game_over:
            for y, row in enumerate(self.current_piece['shape']):
                for x, cell in enumerate(row):
                    if cell:
                        x1 = (self.current_piece['x'] + x) * self.cell_size
                        y1 = (self.current_piece['y'] + y) * self.cell_size
                        x2 = x1 + self.cell_size
                        y2 = y1 + self.cell_size
                        self.canvas.create_rectangle(x1, y1, x2, y2,
                                                    fill=self.current_piece['color'],
                                                    outline='')
        
        self.score_label.config(text=f"Счет: {self.score}")
        
        if self.game_over:
            self.canvas.create_text(125, 250,
                                   text="ИГРА ОКОНЧЕНА",
                                   fill='red', font=('Helvetica', 16, 'bold'))


# ============================================================================
# ИГРА 3: 2048 (Game2048)
# ============================================================================


class Game2048(BaseGame):
    def setup_ui(self):
        """Настройка интерфейса для 2048"""
        super().setup_ui()
        self.title.config(text="🎯 2048")
        self.cell_size = 100  # Размер клетки в пикселях
        self.canvas.config(width=400, height=400)  # Поле 4x4
        
        # Цвета для разных чисел
        self.number_colors = {
            0: '#cdc1b4', 2: '#eee4da', 4: '#ede0c8', 8: '#f2b179',
            16: '#f59563', 32: '#f67c5f', 64: '#f65e3b', 128: '#edcf72',
            256: '#edcc61', 512: '#edc850', 1024: '#edc53f', 2048: '#edc22e'
        }
        
        # Привязываем клавиши управления
        self.win.bind('<Left>', lambda e: self.move('left'))
        self.win.bind('<Right>', lambda e: self.move('right'))
        self.win.bind('<Up>', lambda e: self.move('up'))
        self.win.bind('<Down>', lambda e: self.move('down'))
        self.win.focus_set()
    
    def new_game(self):
        """Начинает новую игру"""
        self.board = [[0] * 4 for _ in range(4)]
        self.score = 0
        self.add_random_tile()
        self.add_random_tile()
        self.draw()
    
    def add_random_tile(self):
        """Добавляет новую плитку (2 или 4) в случайную пустую клетку"""
        empty_cells = []
        for row in range(4):
            for col in range(4):
                if self.board[row][col] == 0:
                    empty_cells.append((row, col))
        
        if empty_cells:
            row, col = random.choice(empty_cells)
            # 90% - 2, 10% - 4
            self.board[row][col] = 2 if random.random() < 0.9 else 4
    
    def move(self, direction):
        """Перемещает все плитки в указанном направлении"""
        old_board = [row[:] for row in self.board]
        
        if direction == 'left':
            for row in range(4):
                self.board[row] = self.merge_row(self.board[row])
        elif direction == 'right':
            for row in range(4):
                self.board[row] = self.merge_row(self.board[row][::-1])[::-1]
        elif direction == 'up':
            # Транспонируем матрицу (строки становятся столбцами)
            self.board = list(map(list, zip(*self.board)))
            for row in range(4):
                self.board[row] = self.merge_row(self.board[row])
            self.board = list(map(list, zip(*self.board)))
        elif direction == 'down':
            self.board = list(map(list, zip(*self.board)))
            for row in range(4):
                self.board[row] = self.merge_row(self.board[row][::-1])[::-1]
            self.board = list(map(list, zip(*self.board)))
        
        if old_board != self.board:
            self.add_random_tile()
            self.draw()
    
    def merge_row(self, row):
        """Объединяет одинаковые числа в строке"""
        # Убираем нули
        new_row = [x for x in row if x != 0]
        
        # Объединяем соседние одинаковые числа
        i = 0
        while i < len(new_row) - 1:
            if new_row[i] == new_row[i + 1]:
                new_row[i] *= 2
                self.score += new_row[i]
                del new_row[i + 1]
            i += 1
        
        # Дополняем нулями до длины 4
        while len(new_row) < 4:
            new_row.append(0)
        
        return new_row
    
    def draw(self):
        """Отрисовка игры"""
        self.canvas.delete("all")
        
        for row in range(4):
            for col in range(4):
                x1 = col * self.cell_size + 5
                y1 = row * self.cell_size + 5
                x2 = x1 + self.cell_size - 10
                y2 = y1 + self.cell_size - 10
                
                value = self.board[row][col]
                color = self.number_colors.get(value, '#3c3a32')
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='')
                
                if value != 0:
                    text_x = x1 + (self.cell_size - 10) // 2
                    text_y = y1 + (self.cell_size - 10) // 2
                    font_size = 24 if value < 1000 else 18
                    self.canvas.create_text(text_x, text_y, text=str(value),
                                           font=('Helvetica', font_size, 'bold'))
        
        self.score_label.config(text=f"Счет: {self.score}")


# ============================================================================
# ИГРА 4: САПЕР (MinesweeperGame)
# ============================================================================


class MinesweeperGame(BaseGame):
    def setup_ui(self):
        """Настройка интерфейса для Сапера"""
        super().setup_ui()
        self.title.config(text="💣 САПЕР")
        self.cell_size = 40  # Размер клетки в пикселях
        self.canvas.config(width=320, height=320)  # Поле 8x8
        
        # Привязываем левую и правую кнопки мыши
        self.canvas.bind('<Button-1>', self.left_click)   # Левый клик
        self.canvas.bind('<Button-3>', self.right_click)  # Правый клик
    
    def new_game(self):
        """Начинает новую игру"""
        self.rows = self.cols = 8
        self.total_mines = 10  # Количество мин
        
        self.board = [[0] * 8 for _ in range(8)]
        self.revealed = [[False] * 8 for _ in range(8)]
        self.flags = [[False] * 8 for _ in range(8)]
        self.game_over = False
        self.score = 0  # Счет (количество открытых безопасных клеток)
        
        # Расставляем мины случайно
        mines_placed = 0
        while mines_placed < self.total_mines:
            row = random.randint(0, 7)
            col = random.randint(0, 7)
            if self.board[row][col] != -1:
                self.board[row][col] = -1
                mines_placed += 1
        
        # Вычисляем числа для каждой клетки
        for row in range(8):
            for col in range(8):
                if self.board[row][col] != -1:
                    mine_count = 0
                    for dr in [-1, 0, 1]:
                        for dc in [-1, 0, 1]:
                            nr, nc = row + dr, col + dc
                            if 0 <= nr < 8 and 0 <= nc < 8 and self.board[nr][nc] == -1:
                                mine_count += 1
                    self.board[row][col] = mine_count
        
        self.draw()
    
    def left_click(self, event):
        """Обработка левого клика - открыть клетку"""
        if self.game_over:
            return
        
        col = event.x // self.cell_size
        row = event.y // self.cell_size
        
        if 0 <= row < 8 and 0 <= col < 8:
            if not self.flags[row][col]:
                if self.board[row][col] == -1:
                    self.game_over = True
                    self.revealed[row][col] = True
                else:
                    self.reveal_cell(row, col)
                self.draw()
    
    def right_click(self, event):
        """Обработка правого клика - поставить/убрать флаг"""
        if self.game_over:
            return
        
        col = event.x // self.cell_size
        row = event.y // self.cell_size
        
        if 0 <= row < 8 and 0 <= col < 8:
            if not self.revealed[row][col]:
                self.flags[row][col] = not self.flags[row][col]
                self.draw()
    
    def reveal_cell(self, row, col):
        """Рекурсивно открывает клетки (если число 0 - открывает соседние)"""
        if not (0 <= row < 8 and 0 <= col < 8) or self.revealed[row][col] or self.flags[row][col]:
            return
        
        self.revealed[row][col] = True
        
        if self.board[row][col] != -1:
            self.score += 1
        
        if self.board[row][col] == 0:
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr != 0 or dc != 0:
                        self.reveal_cell(row + dr, col + dc)
    
    def draw(self):
        """Отрисовка игры"""
        self.canvas.delete("all")
        
        for row in range(8):
            for col in range(8):
                x1 = col * self.cell_size
                y1 = row * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                
                if self.revealed[row][col]:
                    if self.board[row][col] == -1:
                        self.canvas.create_rectangle(x1, y1, x2, y2, fill='red')
                        self.canvas.create_text(x1 + 20, y1 + 20, text='💣',
                                               font=('Segoe UI Emoji', 20))
                    else:
                        self.canvas.create_rectangle(x1, y1, x2, y2, fill='#c0c0c0')
                        if self.board[row][col] > 0:
                            colors = ['', 'blue', 'green', 'red', 'purple', 'maroon',
                                     'turquoise', 'black', 'gray']
                            color = colors[self.board[row][col]]
                            self.canvas.create_text(x1 + 20, y1 + 20,
                                                   text=str(self.board[row][col]),
                                                   fill=color,
                                                   font=('Helvetica', 16, 'bold'))
                else:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill='#808080')
                    if self.flags[row][col]:
                        self.canvas.create_text(x1 + 20, y1 + 20, text='🚩',
                                               font=('Segoe UI Emoji', 20))
        
        self.score_label.config(text=f"Счет: {self.score}")
        
        if self.game_over:
            self.canvas.create_text(160, 160, text="ИГРА ОКОНЧЕНА",
                                   fill='red', font=('Helvetica', 20, 'bold'))


# ============================================================================
# ИГРА 5: МОРСКОЙ БОЙ (BattleshipGame)
# ============================================================================


class BattleshipGame(BaseGame):
    def setup_ui(self):
        """Настройка интерфейса для морского боя"""
        super().setup_ui()
        self.title.config(text="⚓ МОРСКОЙ БОЙ")
        self.cell_size = 35
        self.canvas.config(width=750, height=350)
        
        # Размеры кораблей
        self.ship_sizes = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
        
        # Панель с кнопками управления
        self.control_frame = tk.Frame(self.win, bg=self.c['bg'])
        self.control_frame.pack(pady=5)
        
        # Кнопка автоматической расстановки
        tk.Button(self.control_frame, text="🚢 Авторасстановка",
                 command=self.auto_place_player,
                 bg=self.c['primary'], fg=self.c['bg']).pack(side='left', padx=5)
        
        # Кнопка сброса
        tk.Button(self.control_frame, text="🔄 Сброс",
                 command=self.new_game,
                 bg=self.c['secondary'], fg=self.c['bg']).pack(side='left', padx=5)
        
        # Кнопка начала боя (изначально скрыта)
        self.start_battle_btn = tk.Button(self.control_frame, text="⚔ НАЧАТЬ БОЙ",
                                          command=self.start_battle,
                                          bg='#ffaa00', fg='black',
                                          font=('Helvetica', 10, 'bold'))
        self.start_battle_btn.pack(side='left', padx=5)
        self.start_battle_btn.pack_forget()  # Скрываем кнопку
        
        # Метка для отображения текущего режима
        self.mode_label = tk.Label(self.control_frame,
                                   text="Режим: расстановка",
                                   font=('Helvetica', 10),
                                   bg=self.c['bg'],
                                   fg=self.c['text'])
        self.mode_label.pack(side='left', padx=20)
        
        self.canvas.bind('<Button-1>', self.on_click)
    
    def new_game(self):
        """Начинает новую игру"""
        self.player_board = [[0] * 8 for _ in range(8)]
        self.computer_board = [[0] * 8 for _ in range(8)]
        
        self.player_shots = [[False] * 8 for _ in range(8)]
        self.computer_shots = [[False] * 8 for _ in range(8)]
        
        self.placement_mode = True
        self.battle_mode = False
        self.game_over = False
        self.player_turn = True
        
        self.player_score = 0
        self.computer_score = 0
        
        self.current_ship_index = 0
        self.ship_sizes_player = self.ship_sizes.copy()
        self.placing_horizontal = True
        
        self.auto_place_computer()
        
        self.start_battle_btn.pack_forget()
        
        self.status.config(text="Расставьте корабли (клик для размещения, R для поворота)")
        self.mode_label.config(text="Режим: расстановка")
        self.win.bind('<KeyPress-r>', lambda e: self.toggle_orientation())
        self.win.focus_set()
        self.draw()
    
    def toggle_orientation(self):
        """Меняет ориентацию корабля"""
        if self.placement_mode:
            self.placing_horizontal = not self.placing_horizontal
            self.status.config(
                text=f"Ориентация: {'горизонтально' if self.placing_horizontal else 'вертикально'}")
    
    def auto_place_player(self):
        """Автоматически расставляет корабли игрока"""
        self.player_board = [[0] * 8 for _ in range(8)]
        self.ship_sizes_player = self.ship_sizes.copy()
        self.current_ship_index = 0
        
        for size in self.ship_sizes:
            placed = False
            attempts = 0
            while not placed and attempts < 1000:
                attempts += 1
                row = random.randint(0, 7)
                col = random.randint(0, 7)
                horizontal = random.choice([True, False])
                
                if self.can_place_ship(self.player_board, row, col, size, horizontal):
                    self.place_ship(self.player_board, row, col, size, horizontal, 1)
                    placed = True
        
        self.current_ship_index = len(self.ship_sizes)
        self.status.config(text="Корабли расставлены! Нажмите 'НАЧАТЬ БОЙ'")
        self.start_battle_btn.pack(side='left', padx=5)
        self.draw()
    
    def auto_place_computer(self):
        """Автоматически расставляет корабли компьютера"""
        self.computer_board = [[0] * 8 for _ in range(8)]
        
        for size in self.ship_sizes:
            placed = False
            attempts = 0
            while not placed and attempts < 1000:
                attempts += 1
                row = random.randint(0, 7)
                col = random.randint(0, 7)
                horizontal = random.choice([True, False])
                
                if self.can_place_ship(self.computer_board, row, col, size, horizontal):
                    self.place_ship(self.computer_board, row, col, size, horizontal, 1)
                    placed = True
    
    def can_place_ship(self, board, row, col, size, horizontal):
        """Проверяет, можно ли поставить корабль"""
        if horizontal:
            if col + size > 8:
                return False
            
            for i in range(size):
                if board[row][col + i] != 0:
                    return False
                
                # Проверяем соседние клетки (корабли не должны касаться)
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        nr, nc = row + dr, col + i + dc
                        if 0 <= nr < 8 and 0 <= nc < 8 and board[nr][nc] != 0:
                            return False
        else:
            if row + size > 8:
                return False
            
            for i in range(size):
                if board[row + i][col] != 0:
                    return False
                
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        nr, nc = row + i + dr, col + dc
                        if 0 <= nr < 8 and 0 <= nc < 8 and board[nr][nc] != 0:
                            return False
        
        return True
    
    def place_ship(self, board, row, col, size, horizontal, value):
        """Ставит корабль на доску"""
        if horizontal:
            for i in range(size):
                board[row][col + i] = value
        else:
            for i in range(size):
                board[row + i][col] = value
    
    def on_click(self, event):
        """Обработка кликов мыши"""
        x, y = event.x, event.y
        
        # Левое поле игрока
        if x < 8 * self.cell_size:
            col = x // self.cell_size
            row = y // self.cell_size
            
            if 0 <= row < 8 and 0 <= col < 8:
                if self.placement_mode:
                    self.place_player_ship(row, col)
        
        # Правое поле компьютера
        elif x > 8 * self.cell_size + 40 and x < 2 * 8 * self.cell_size + 40:
            adj_x = x - (8 * self.cell_size + 40)
            col = adj_x // self.cell_size
            row = y // self.cell_size
            
            if 0 <= row < 8 and 0 <= col < 8:
                if self.battle_mode and self.player_turn and not self.game_over:
                    self.player_shoot(row, col)
        
        self.draw()
    
    def place_player_ship(self, row, col):
        """Размещает корабль игрока"""
        if self.current_ship_index >= len(self.ship_sizes):
            return
        
        size = self.ship_sizes_player[self.current_ship_index]
        
        if self.can_place_ship(self.player_board, row, col, size, self.placing_horizontal):
            self.place_ship(self.player_board, row, col, size, self.placing_horizontal, 1)
            self.current_ship_index += 1
            
            if self.current_ship_index >= len(self.ship_sizes):
                self.status.config(text="Все корабли расставлены! Нажмите 'НАЧАТЬ БОЙ'")
                self.start_battle_btn.pack(side='left', padx=5)
    
    def start_battle(self):
        """Начинает бой"""
        self.placement_mode = False
        self.battle_mode = True
        self.player_turn = True
        self.game_over = False
        self.status.config(text="Ваш ход! Стреляйте по правому полю")
        self.mode_label.config(text="Режим: бой")
        
        self.start_battle_btn.pack_forget()
        
        self.draw()
    
    def player_shoot(self, row, col):
        """Выстрел игрока по компьютеру"""
        if self.player_shots[row][col]:
            self.status.config(text="Сюда уже стреляли!")
            return
        
        self.player_shots[row][col] = True
        
        if self.computer_board[row][col] == 1:
            self.computer_board[row][col] = 2
            self.player_score += 10
            self.status.config(text="Попадание! Стреляйте еще!")
            
            if self.check_ship_sunk(self.computer_board, row, col):
                self.status.config(text="Корабль потоплен! +50 очков")
                self.player_score += 50
            
            if self.check_win(self.computer_board):
                self.game_over = True
                self.status.config(text="ПОБЕДА! Вы потопили все корабли!")
        else:
            self.status.config(text="Мимо... Ход компьютера")
            self.player_turn = False
            self.win.after(500, self.computer_shoot)
    
    def computer_shoot(self):
        """Выстрел компьютера по игроку"""
        if self.game_over:
            return
        
        available = []
        for r in range(8):
            for c in range(8):
                if not self.computer_shots[r][c]:
                    available.append((r, c))
        
        if available:
            row, col = random.choice(available)
            self.computer_shots[row][col] = True
            
            if self.player_board[row][col] == 1:
                self.player_board[row][col] = 2
                self.computer_score += 10
                self.status.config(text="Компьютер попал! Он стреляет еще...")
                
                if self.check_ship_sunk(self.player_board, row, col):
                    self.computer_score += 50
                
                if not self.check_win(self.player_board):
                    self.win.after(500, self.computer_shoot)
                else:
                    self.game_over = True
                    self.status.config(text="Поражение... Компьютер победил")
            else:
                self.status.config(text="Компьютер промахнулся. Ваш ход!")
                self.player_turn = True
        
        self.draw()
    
    def check_ship_sunk(self, board, row, col):
        """
        Проверяет, потоплен ли корабль
        Использует BFS для поиска всех клеток корабля
        """
        if board[row][col] != 2:
            return False
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ship_cells = set()
        ship_cells.add((row, col))
        queue = [(row, col)]
        
        while queue:
            r, c = queue.pop(0)
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < 8 and 0 <= nc < 8:
                    if board[nr][nc] in [1, 2] and (nr, nc) not in ship_cells:
                        ship_cells.add((nr, nc))
                        queue.append((nr, nc))
        
        for r, c in ship_cells:
            if board[r][c] == 1:
                return False
        
        return True
    
    def check_win(self, board):
        """Проверяет, остались ли на доске неподбитые корабли"""
        for r in range(8):
            for c in range(8):
                if board[r][c] == 1:
                    return False
        return True
    
    def draw(self):
        """Отрисовка игры"""
        self.canvas.delete("all")
        
        # Разделитель между полями
        self.canvas.create_line(8 * self.cell_size + 20, 0,
                                8 * self.cell_size + 20, 8 * self.cell_size,
                               fill=self.c['primary'], width=3)
        
        # Подписи полей
        self.canvas.create_text(8 * self.cell_size // 2, 8 * self.cell_size + 20,
                               text="ВАШЕ ПОЛЕ", fill=self.c['primary'],
                               font=('Helvetica', 12, 'bold'))
        self.canvas.create_text(8 * self.cell_size + 40 + 8 * self.cell_size // 2,
                               8 * self.cell_size + 20,
                               text="ПОЛЕ ПРОТИВНИКА", fill=self.c['secondary'],
                               font=('Helvetica', 12, 'bold'))
        
        # Левое поле (игрока)
        for r in range(8):
            for c in range(8):
                x1 = c * self.cell_size
                y1 = r * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                
                if self.player_board[r][c] == 1:
                    color = self.c['primary']
                elif self.player_board[r][c] == 2:
                    color = '#ff6b6b'
                else:
                    color = '#2a2a2a' if (r + c) % 2 else '#1a1a1a'
                
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='#333')
                
                if self.computer_shots[r][c]:
                    if self.player_board[r][c] == 2:
                        self.canvas.create_text(x1 + self.cell_size // 2,
                                               y1 + self.cell_size // 2,
                                               text='💥', font=('Segoe UI Emoji', 16))
                    elif self.player_board[r][c] == 0:
                        self.canvas.create_oval(x1 + self.cell_size // 2 - 3,
                                               y1 + self.cell_size // 2 - 3,
                                               x1 + self.cell_size // 2 + 3,
                                               y1 + self.cell_size // 2 + 3,
                                               fill='black')
        
        # Правое поле (компьютера)
        offset_x = 8 * self.cell_size + 40
        for r in range(8):
            for c in range(8):
                x1 = offset_x + c * self.cell_size
                y1 = r * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                
                if self.player_shots[r][c]:
                    if self.computer_board[r][c] == 2:
                        color = '#ff6b6b'
                        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='#333')
                        self.canvas.create_text(x1 + self.cell_size // 2,
                                               y1 + self.cell_size // 2,
                                               text='💥', font=('Segoe UI Emoji', 16))
                    else:
                        color = '#2a2a2a' if (r + c) % 2 else '#1a1a1a'
                        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='#333')
                        self.canvas.create_oval(x1 + self.cell_size // 2 - 3,
                                               y1 + self.cell_size // 2 - 3,
                                               x1 + self.cell_size // 2 + 3,
                                               y1 + self.cell_size // 2 + 3,
                                               fill='black')
                else:
                    color = '#2a2a2a' if (r + c) % 2 else '#1a1a1a'
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='#333')
        
        if self.battle_mode and not self.game_over:
            turn_text = "Ваш ход" if self.player_turn else "Ход компьютера..."
            self.status.config(text=turn_text)
        
        self.score_label.config(text=f"Вы: {self.player_score}  Комп: {self.computer_score}")


# ============================================================================
# ИГРА 6: ШАШКИ (CheckersGame)
# ============================================================================


class CheckersGame(BaseGame):
    def setup_ui(self):
        super().setup_ui()
        self.title.config(text="● ШАШКИ")
        self.cell_size = 50
        self.canvas.config(width=400, height=400)
        self.canvas.bind('<Button-1>', self.on_click)
    
    def new_game(self):
        """Начальная расстановка шашек"""
        self.board = [[None] * 8 for _ in range(8)]
        
        for r in range(8):
            for c in range(8):
                if (r + c) % 2 == 1:
                    if r < 3:
                        self.board[r][c] = 'b'
                    elif r > 4:
                        self.board[r][c] = 'w'
        
        self.selected = None
        self.player_turn = True
        self.game_over = False
        self.player_score = 0
        self.computer_score = 0
        
        self.draw()
        self.status.config(text="Ваш ход")
    
    def on_click(self, event):
        """Обработка клика мыши"""
        if not self.player_turn or self.game_over:
            return
        
        col = event.x // self.cell_size
        row = event.y // self.cell_size
        
        if 0 <= row < 8 and 0 <= col < 8:
            if self.selected:
                if self.make_move(self.selected[0], self.selected[1], row, col):
                    self.selected = None
                    self.player_turn = False
                    self.draw()
                    self.win.after(500, self.computer_move)
                else:
                    self.selected = None
            elif self.board[row][col] == 'w':
                self.selected = (row, col)
            
            self.draw()
    
    def make_move(self, r1, c1, r2, c2):
        """Выполняет ход шашкой"""
        if not (0 <= r2 < 8 and 0 <= c2 < 8) or self.board[r2][c2] or (r2 + c2) % 2 == 0:
            return False
        
        dr, dc = r2 - r1, c2 - c1
        
        if abs(dr) == 1 and abs(dc) == 1:
            if (self.board[r1][c1] == 'w' and dr < 0) or \
               (self.board[r1][c1] == 'b' and dr > 0):
                self.board[r2][c2] = self.board[r1][c1]
                self.board[r1][c1] = None
                return True
        
        elif abs(dr) == 2 and abs(dc) == 2:
            mr, mc = (r1 + r2) // 2, (c1 + c2) // 2
            
            if (self.board[mr][mc] and
                ((self.board[r1][c1] == 'w' and self.board[mr][mc] == 'b') or
                 (self.board[r1][c1] == 'b' and self.board[mr][mc] == 'w'))):
                
                self.board[r2][c2] = self.board[r1][c1]
                self.board[r1][c1] = None
                self.board[mr][mc] = None
                
                if self.board[r2][c2] == 'w':
                    self.player_score += 10
                else:
                    self.computer_score += 10
                
                return True
        
        return False
    
    def computer_move(self):
        """ИИ для черных шашек"""
        if self.game_over:
            return
        
        moves = []
        captures = []
        
        for r in range(8):
            for c in range(8):
                if self.board[r][c] == 'b':
                    for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                        nr, nc = r + dr, c + dc
                        
                        if 0 <= nr < 8 and 0 <= nc < 8 and not self.board[nr][nc]:
                            moves.append((r, c, nr, nc))
                        
                        nr2, nc2 = r + dr * 2, c + dc * 2
                        mr, mc = r + dr, c + dc
                        if (0 <= nr2 < 8 and 0 <= nc2 < 8 and not self.board[nr2][nc2] and
                            self.board[mr][mc] == 'w'):
                            captures.append((r, c, nr2, nc2))
        
        if captures:
            r1, c1, r2, c2 = random.choice(captures)
            self.make_move(r1, c1, r2, c2)
        elif moves:
            r1, c1, r2, c2 = random.choice(moves)
            self.make_move(r1, c1, r2, c2)
        else:
            self.game_over = True
            self.status.config(text="Вы выиграли!")
            self.draw()
            return
        
        self.player_turn = True
        self.status.config(text="Ваш ход")
        self.draw()
    
    def draw(self):
        """Отрисовка доски"""
        self.canvas.delete("all")
        
        colors = ['#f0d9b5', '#b58863']
        
        for r in range(8):
            for c in range(8):
                x1 = c * self.cell_size
                y1 = r * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                
                self.canvas.create_rectangle(x1, y1, x2, y2,
                                            fill=colors[(r + c) % 2])
                
                if self.board[r][c]:
                    color = 'black' if self.board[r][c][0] == 'b' else 'white'
                    self.canvas.create_oval(x1 + 5, y1 + 5, x2 - 5, y2 - 5,
                                          fill=color, outline='gray', width=2)
                
                if self.selected == (r, c):
                    self.canvas.create_rectangle(x1 + 2, y1 + 2, x2 - 2, y2 - 2,
                                                outline=self.c['primary'], width=3)
        
        self.score_label.config(text=f"Вы: {self.player_score}  Комп: {self.computer_score}")


# ============================================================================
# ИГРА 7: РЕВЕРСИ (ReversiGame)
# ============================================================================


class ReversiGame(BaseGame):
    def setup_ui(self):
        super().setup_ui()
        self.title.config(text="◉ РЕВЕРСИ")
        self.cell_size = 50
        self.canvas.config(width=400, height=400, bg='green')
        self.canvas.bind('<Button-1>', self.on_click)
    
    def new_game(self):
        """Начальная расстановка"""
        self.board = [[None] * 8 for _ in range(8)]
        
        # Стартовые 4 фишки в центре
        self.board[3][3] = 'white'
        self.board[3][4] = 'black'
        self.board[4][3] = 'black'
        self.board[4][4] = 'white'
        
        self.player_turn = True
        self.game_over = False
        self.player_score = 2
        self.computer_score = 2
        
        self.status.config(text="Ваш ход (черные)")
        self.draw()
    
    def on_click(self, event):
        """Обработка клика"""
        if not self.player_turn or self.game_over:
            return
        
        col = event.x // self.cell_size
        row = event.y // self.cell_size
        
        if self.is_valid_move(row, col, 'black'):
            self.place_piece(row, col, 'black')
            self.player_turn = False
            self.draw()
            self.win.after(500, self.computer_move)
    
    def is_valid_move(self, row, col, color):
        """Проверяет, можно ли поставить фишку"""
        if not (0 <= row < 8 and 0 <= col < 8) or self.board[row][col]:
            return False
        
        opp = 'white' if color == 'black' else 'black'
        
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),           (0, 1),
                      (1, -1),  (1, 0),  (1, 1)]
        
        for dr, dc in directions:
            r, c = row + dr, col + dc
            
            if 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] == opp:
                r += dr
                c += dc
                
                while 0 <= r < 8 and 0 <= c < 8:
                    if self.board[r][c] is None:
                        break
                    if self.board[r][c] == color:
                        return True
                    r += dr
                    c += dc
        
        return False
    
    def place_piece(self, row, col, color):
        """Ставит фишку и переворачивает захваченные"""
        self.board[row][col] = color
        opp = 'white' if color == 'black' else 'black'
        
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),           (0, 1),
                      (1, -1),  (1, 0),  (1, 1)]
        
        for dr, dc in directions:
            pieces_to_flip = []
            r, c = row + dr, col + dc
            
            while 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] == opp:
                pieces_to_flip.append((r, c))
                r += dr
                c += dc
            
            if 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] == color:
                for fr, fc in pieces_to_flip:
                    self.board[fr][fc] = color
        
        self.update_score()
    
    def update_score(self):
        """Обновляет счет"""
        black_count = 0
        white_count = 0
        
        for r in range(8):
            for c in range(8):
                if self.board[r][c] == 'black':
                    black_count += 1
                elif self.board[r][c] == 'white':
                    white_count += 1
        
        self.player_score = black_count
        self.computer_score = white_count
    
    def computer_move(self):
        """ИИ для белых фишек"""
        if self.game_over:
            return
        
        moves = []
        for r in range(8):
            for c in range(8):
                if self.is_valid_move(r, c, 'white'):
                    moves.append((r, c))
        
        if moves:
            r, c = random.choice(moves)
            self.place_piece(r, c, 'white')
            
            # Проверка на окончание игры
            player_moves = []
            for r in range(8):
                for c in range(8):
                    if self.is_valid_move(r, c, 'black'):
                        player_moves.append((r, c))
            
            if not player_moves:
                self.game_over = True
                if self.player_score > self.computer_score:
                    self.status.config(text="Вы выиграли!")
                elif self.player_score < self.computer_score:
                    self.status.config(text="Компьютер выиграл!")
                else:
                    self.status.config(text="Ничья!")
        else:
            self.game_over = True
            if self.player_score > self.computer_score:
                self.status.config(text="Вы выиграли!")
            elif self.player_score < self.computer_score:
                self.status.config(text="Компьютер выиграл!")
            else:
                self.status.config(text="Ничья!")
        
        self.player_turn = True
        self.draw()
    
    def draw(self):
        """Отрисовка доски"""
        self.canvas.delete("all")
        
        for r in range(8):
            for c in range(8):
                x1 = c * self.cell_size
                y1 = r * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                
                self.canvas.create_rectangle(x1, y1, x2, y2, outline='black')
                
                if self.board[r][c]:
                    color = 'black' if self.board[r][c] == 'black' else 'white'
                    self.canvas.create_oval(x1 + 5, y1 + 5, x2 - 5, y2 - 5,
                                          fill=color, outline='gray', width=2)
                elif self.is_valid_move(r, c, 'black') and self.player_turn and not self.game_over:
                    self.canvas.create_oval(x1 + 15, y1 + 15, x2 - 15, y2 - 15,
                                          fill='yellow')
        
        self.score_label.config(text=f"Вы: {self.player_score}  Комп: {self.computer_score}")


# ============================================================================
# ИГРА 8: КРЕСТИКИ-НОЛИКИ (TicTacToeGame) - НОВАЯ ИГРА
# ============================================================================


class TicTacToeGame(BaseGame):
    def setup_ui(self):
        """Настройка интерфейса для Крестиков-ноликов"""
        super().setup_ui()
        self.title.config(text="❌⭕ КРЕСТИКИ-НОЛИКИ")
        self.cell_size = 150  # Размер клетки в пикселях
        self.canvas.config(width=450, height=450)  # Поле 3x3 (3*150=450)
        
        # Привязываем клик мыши к холсту
        self.canvas.bind('<Button-1>', self.on_click)
        
        # Счет игры
        self.player_wins = 0  # Победы игрока
        self.computer_wins = 0  # Победы компьютера
        self.draws = 0  # Ничьи
    
    def new_game(self):
        """Начинает новую игру"""
        # Создаем пустое поле 3x3
        # Каждая клетка может быть: None (пусто), 'X' (игрок) или 'O' (компьютер)
        self.board = [[None for _ in range(3)] for _ in range(3)]
        
        # Игрок ходит первым (крестики)
        self.player_turn = True
        self.game_over = False
        
        # Обновляем статус
        self.status.config(text="Ваш ход (❌)")
        self.draw()
    
    def on_click(self, event):
        """
        Обрабатывает клик мыши по холсту.
        Определяет клетку, в которую кликнули, и делает ход игрока.
        """
        if self.game_over or not self.player_turn:
            return
        
        # Определяем координаты клетки по позиции клика
        col = event.x // self.cell_size
        row = event.y // self.cell_size
        
        # Проверяем, что клик в пределах поля и клетка свободна
        if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] is None:
            # Делаем ход игрока
            self.board[row][col] = 'X'
            self.player_turn = False
            self.draw()
            
            # Проверяем, не выиграл ли игрок после своего хода
            if self.check_winner('X'):
                self.game_over = True
                self.player_wins += 1
                self.status.config(text="Вы выиграли! 🎉")
            elif self.is_board_full():
                self.game_over = True
                self.draws += 1
                self.status.config(text="Ничья! 🤝")
            else:
                # Если игра не окончена, ходит компьютер
                self.status.config(text="Ход компьютера...")
                # Делаем ход компьютера через 500 мс для плавности
                self.win.after(500, self.computer_move)
            
            self.draw()
    
    def computer_move(self):
        """
        Ход компьютера.
        Использует простую стратегию:
        1. Если может выиграть - выигрывает
        2. Если игрок может выиграть следующим ходом - блокирует
        3. Иначе ставит в центр или случайную клетку
        """
        if self.game_over:
            return
        
        # 1. Проверяем, может ли компьютер выиграть
        for r in range(3):
            for c in range(3):
                if self.board[r][c] is None:
                    # Пробуем поставить нолик
                    self.board[r][c] = 'O'
                    if self.check_winner('O'):
                        # Компьютер выигрывает
                        self.player_turn = True
                        self.game_over = True
                        self.computer_wins += 1
                        self.status.config(text="Компьютер выиграл! 💻")
                        self.draw()
                        return
                    # Отменяем ход
                    self.board[r][c] = None
        
        # 2. Проверяем, может ли игрок выиграть следующим ходом (блокировка)
        for r in range(3):
            for c in range(3):
                if self.board[r][c] is None:
                    # Пробуем поставить крестик (как будто игрок)
                    self.board[r][c] = 'X'
                    if self.check_winner('X'):
                        # Нужно заблокировать эту клетку
                        self.board[r][c] = None
                        self.board[r][c] = 'O'
                        self.player_turn = True
                        
                        # Проверяем, не выиграл ли компьютер после блокировки
                        if self.check_winner('O'):
                            self.game_over = True
                            self.computer_wins += 1
                            self.status.config(text="Компьютер выиграл! 💻")
                        elif self.is_board_full():
                            self.game_over = True
                            self.draws += 1
                            self.status.config(text="Ничья! 🤝")
                        else:
                            self.status.config(text="Ваш ход (❌)")
                        
                        self.draw()
                        return
                    # Отменяем ход
                    self.board[r][c] = None
        
        # 3. Если центр свободен - ставим туда
        if self.board[1][1] is None:
            self.board[1][1] = 'O'
            self.player_turn = True
            
            # Проверяем результат после хода
            if self.check_winner('O'):
                self.game_over = True
                self.computer_wins += 1
                self.status.config(text="Компьютер выиграл! 💻")
            elif self.is_board_full():
                self.game_over = True
                self.draws += 1
                self.status.config(text="Ничья! 🤝")
            else:
                self.status.config(text="Ваш ход (❌)")
            
            self.draw()
            return
        
        # 4. Иначе ставим в случайную свободную клетку
        empty_cells = []
        for r in range(3):
            for c in range(3):
                if self.board[r][c] is None:
                    empty_cells.append((r, c))
        
        if empty_cells:
            r, c = random.choice(empty_cells)
            self.board[r][c] = 'O'
            self.player_turn = True
            
            # Проверяем результат после хода
            if self.check_winner('O'):
                self.game_over = True
                self.computer_wins += 1
                self.status.config(text="Компьютер выиграл! 💻")
            elif self.is_board_full():
                self.game_over = True
                self.draws += 1
                self.status.config(text="Ничья! 🤝")
            else:
                self.status.config(text="Ваш ход (❌)")
            
            self.draw()
    
    def check_winner(self, symbol):
        """
        Проверяет, выиграл ли игрок с указанным символом.
        
        Аргументы:
            symbol: 'X' или 'O'
            
        Returns:
            True если есть три символа в ряд
        """
        # Проверка горизонталей
        for r in range(3):
            if all(self.board[r][c] == symbol for c in range(3)):
                return True
        
        # Проверка вертикалей
        for c in range(3):
            if all(self.board[r][c] == symbol for r in range(3)):
                return True
        
        # Проверка диагоналей
        if all(self.board[i][i] == symbol for i in range(3)):
            return True
        
        if all(self.board[i][2 - i] == symbol for i in range(3)):
            return True
        
        return False
    
    def is_board_full(self):
        """Проверяет, заполнено ли все поле"""
        for r in range(3):
            for c in range(3):
                if self.board[r][c] is None:
                    return False
        return True
    
    def draw(self):
        """Отрисовка игрового поля"""
        self.canvas.delete("all")
        
        # Рисуем сетку 3x3
        for i in range(1, 3):
            # Вертикальные линии
            x = i * self.cell_size
            self.canvas.create_line(x, 0, x, 450, fill=self.c['primary'], width=3)
            
            # Горизонтальные линии
            y = i * self.cell_size
            self.canvas.create_line(0, y, 450, y, fill=self.c['primary'], width=3)
        
        # Рисуем крестики и нолики
        for r in range(3):
            for c in range(3):
                x_center = c * self.cell_size + self.cell_size // 2
                y_center = r * self.cell_size + self.cell_size // 2
                
                if self.board[r][c] == 'X':
                    # Рисуем крестик
                    size = 40
                    self.canvas.create_line(x_center - size, y_center - size,
                                           x_center + size, y_center + size,
                                           fill=self.c['primary'], width=5)
                    self.canvas.create_line(x_center + size, y_center - size,
                                           x_center - size, y_center + size,
                                           fill=self.c['primary'], width=5)
                
                elif self.board[r][c] == 'O':
                    # Рисуем нолик
                    self.canvas.create_oval(x_center - 40, y_center - 40,
                                           x_center + 40, y_center + 40,
                                           outline=self.c['secondary'], width=5)
        
        # Обновляем счет
        self.score_label.config(text=f"Вы: {self.player_wins}  Комп: {self.computer_wins}  Ничьи: {self.draws}")


# ============================================================================
# ИГРА 9: АРКАНОИД (ArkanoidGame)
# ============================================================================


class ArkanoidGame(BaseGame):
    def setup_ui(self):
        super().setup_ui()
        self.title.config(text="🧱 АРКАНОИД")
        self.canvas.config(width=600, height=400, bg='black')
        
        self.win.bind('<Left>', lambda e: self.move_paddle(-20))
        self.win.bind('<Right>', lambda e: self.move_paddle(20))
        self.win.focus_set()
    
    def new_game(self):
        self.paddle_x = 250
        self.paddle_width = 100
        self.paddle_height = 15
        
        self.ball = [300, 350, 4, -4]
        
        self.bricks = []
        colors = ['red', 'orange', 'yellow', 'green', 'blue']
        
        for row in range(5):
            for col in range(8):
                self.bricks.append({
                    'x': col * 75 + 5,
                    'y': row * 25 + 30,
                    'width': 70,
                    'height': 20,
                    'color': colors[row],
                    'active': True
                })
        
        self.score = 0
        self.running = True
        self.game_over = False
        
        self.update()
    
    def move_paddle(self, dx):
        if not self.running or self.game_over:
            return
        
        new_x = self.paddle_x + dx
        if 0 <= new_x <= 600 - self.paddle_width:
            self.paddle_x = new_x
    
    def update(self):
        if not self.running or self.game_over:
            return
        
        self.ball[0] += self.ball[2]
        self.ball[1] += self.ball[3]
        
        if self.ball[0] <= 0 or self.ball[0] >= 600 - 10:
            self.ball[2] *= -1
        
        if self.ball[1] <= 0:
            self.ball[3] *= -1
        
        if (self.ball[1] >= 370 and
            self.paddle_x <= self.ball[0] <= self.paddle_x + self.paddle_width):
            self.ball[3] = -abs(self.ball[3])
            
            relative_hit = (self.ball[0] - self.paddle_x) / self.paddle_width - 0.5
            self.ball[2] += relative_hit * 2
        
        for brick in self.bricks[:]:
            if brick['active']:
                if (brick['x'] <= self.ball[0] <= brick['x'] + brick['width'] and
                    brick['y'] <= self.ball[1] <= brick['y'] + brick['height']):
                    
                    brick['active'] = False
                    self.ball[3] *= -1
                    self.score += 10
                    self.bricks.remove(brick)
        
        if self.ball[1] > 400:
            self.game_over = True
            self.status.config(text="ИГРА ОКОНЧЕНА!")
        
        if not self.bricks:
            self.game_over = True
            self.status.config(text="ВЫ ПОБЕДИЛИ!")
        
        self.draw()
        
        if not self.game_over:
            self.win.after(30, self.update)
    
    def draw(self):
        self.canvas.delete("all")
        
        for brick in self.bricks:
            if brick['active']:
                self.canvas.create_rectangle(brick['x'], brick['y'],
                                           brick['x'] + brick['width'],
                                           brick['y'] + brick['height'],
                                           fill=brick['color'], outline='white')
        
        self.canvas.create_rectangle(self.paddle_x, 380,
                                    self.paddle_x + self.paddle_width, 395,
                                    fill='white')
        
        self.canvas.create_oval(self.ball[0] - 5, self.ball[1] - 5,
                               self.ball[0] + 5, self.ball[1] + 5,
                               fill='white')
        
        self.score_label.config(text=f"Счет: {self.score}")
        
        if self.game_over:
            self.canvas.create_text(300, 200,
                                   text=f"ИГРА ОКОНЧЕНА\nСчет: {self.score}",
                                   fill='red', font=('Helvetica', 20, 'bold'),
                                   justify='center')


# ============================================================================
# ИГРА 10: FLAPPY BIRD (FlappyBirdGame)
# ============================================================================


class FlappyBirdGame(BaseGame):
    def setup_ui(self):
        super().setup_ui()
        self.title.config(text="🐦 FLAPPY BIRD")
        self.canvas.config(width=400, height=600, bg='lightblue')
        
        self.win.bind('<space>', lambda e: self.jump())
        self.win.focus_set()
    
    def new_game(self):
        self.bird_x = 100
        self.bird_y = 300
        self.bird_vel = 0
        self.bird_size = 30
        
        self.pipes = []
        self.pipe_width = 60
        self.pipe_gap = 180
        self.pipe_speed = 3
        self.min_pipe_distance = 200
        
        self.score = 0
        self.running = True
        self.game_over = False
        
        self.add_pipe()
        
        self.status.config(text="Нажмите ПРОБЕЛ чтобы лететь!")
        self.update()
    
    def add_pipe(self):
        min_top = 50
        max_top = 600 - self.pipe_gap - 50
        
        top_height = random.randint(min_top, max_top)
        
        self.pipes.append({
            'x': 400,
            'top_height': top_height,
            'bottom_y': top_height + self.pipe_gap,
            'passed': False
        })
    
    def jump(self):
        if self.running and not self.game_over:
            self.bird_vel = -8
    
    def update(self):
        if not self.running or self.game_over:
            return
        
        self.bird_vel += 0.5
        self.bird_y += self.bird_vel
        
        if self.bird_y <= 0 or self.bird_y + self.bird_size >= 600:
            self.game_over = True
            self.status.config(text="ИГРА ОКОНЧЕНА!")
            self.draw()
            return
        
        for pipe in self.pipes[:]:
            pipe['x'] -= self.pipe_speed
            
            if pipe['x'] + self.pipe_width < 0:
                self.pipes.remove(pipe)
            
            bird_left = self.bird_x
            bird_right = self.bird_x + self.bird_size
            bird_top = self.bird_y
            bird_bottom = self.bird_y + self.bird_size
            
            pipe_left = pipe['x']
            pipe_right = pipe['x'] + self.pipe_width
            
            if bird_right > pipe_left and bird_left < pipe_right:
                if bird_top < pipe['top_height'] or bird_bottom > pipe['bottom_y']:
                    self.game_over = True
                    self.status.config(text="ИГРА ОКОНЧЕНА!")
                    self.draw()
                    return
            
            if not pipe['passed'] and pipe['x'] + self.pipe_width < self.bird_x:
                pipe['passed'] = True
                self.score += 1
        
        if len(self.pipes) < 3:
            if not self.pipes or self.pipes[-1]['x'] < 400 - self.min_pipe_distance:
                if random.random() < 0.02:
                    self.add_pipe()
        
        self.draw()
        
        if not self.game_over:
            self.win.after(30, self.update)
    
    def draw(self):
        self.canvas.delete("all")
        
        for pipe in self.pipes:
            self.canvas.create_rectangle(pipe['x'], 0,
                                       pipe['x'] + self.pipe_width, pipe['top_height'],
                                       fill='green', outline='darkgreen')
            self.canvas.create_rectangle(pipe['x'], pipe['bottom_y'],
                                       pipe['x'] + self.pipe_width, 600,
                                       fill='green', outline='darkgreen')
        
        self.canvas.create_oval(self.bird_x, self.bird_y,
                               self.bird_x + self.bird_size, self.bird_y + self.bird_size,
                               fill='yellow', outline='orange')
        self.canvas.create_oval(self.bird_x + 15, self.bird_y + 8,
                               self.bird_x + 20, self.bird_y + 13,
                               fill='black')
        
        self.score_label.config(text=f"Счет: {self.score}")
        
        if self.game_over:
            self.canvas.create_text(200, 300,
                                   text=f"ИГРА ОКОНЧЕНА!\nСчет: {self.score}",
                                   fill='red', font=('Helvetica', 20, 'bold'),
                                   justify='center')


# ============================================================================
# ИГРА 11: КАМЕНЬ-НОЖНИЦЫ-БУМАГА (RPSGame)
# ============================================================================

class RPSGame(BaseGame):
    def setup_ui(self):
        super().setup_ui()
        self.title.config(text="✂️ КАМЕНЬ-НОЖНИЦЫ-БУМАГА")
        self.canvas.config(width=400, height=300)
        
        button_frame = tk.Frame(self.win, bg=self.c['bg'])
        button_frame.pack(pady=20)
        
        tk.Button(button_frame, text="🪨 Камень", font=('Helvetica', 14),
                 bg=self.c['primary'], fg=self.c['bg'],
                 command=lambda: self.play('rock')).pack(side='left', padx=10)
        
        tk.Button(button_frame, text="✂️ Ножницы", font=('Helvetica', 14),
                 bg=self.c['secondary'], fg=self.c['bg'],
                 command=lambda: self.play('scissors')).pack(side='left', padx=10)
        
        tk.Button(button_frame, text="📄 Бумага", font=('Helvetica', 14),
                 bg=self.c['primary'], fg=self.c['bg'],
                 command=lambda: self.play('paper')).pack(side='left', padx=10)
        
        self.result_label = tk.Label(self.win, font=('Helvetica', 16),
                                     bg=self.c['bg'], fg=self.c['text'])
        self.result_label.pack(pady=20)
        
        self.emoji = {'rock': '🪨', 'scissors': '✂️', 'paper': '📄'}
    
    def new_game(self):
        self.player_score = 0
        self.computer_score = 0
        self.result_label.config(text="Сделайте выбор!")
        self.draw()
    
    def play(self, player_choice):
        choices = ['rock', 'scissors', 'paper']
        computer_choice = random.choice(choices)
        
        if player_choice == computer_choice:
            result = "Ничья!"
        elif ((player_choice == 'rock' and computer_choice == 'scissors') or
              (player_choice == 'scissors' and computer_choice == 'paper') or
              (player_choice == 'paper' and computer_choice == 'rock')):
            result = "Вы выиграли!"
            self.player_score += 1
        else:
            result = "Компьютер выиграл!"
            self.computer_score += 1
        
        result_text = f"Вы: {self.emoji[player_choice]}  vs  Комп: {self.emoji[computer_choice]}\n{result}"
        self.result_label.config(text=result_text)
        
        self.draw()
    
    def draw(self):
        self.score_label.config(text=f"Вы: {self.player_score}  Комп: {self.computer_score}")


# ============================================================================
# ЗАПУСК ПРИЛОЖЕНИЯ
# ============================================================================
if __name__ == "__main__":
    # Создаем экземпляр главного класса и запускаем главный цикл обработки событий
    Game11v1().root.mainloop()