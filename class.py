# Базовый класс для всех животных
class Animals:
    def __init__(self, name, age, weight, habitat, diet):
        self.name = name
        self.age = age
        self.weight = weight
        self.habitat = habitat
        self.diet = diet

    def eat(self):
        print(f"{self.name} ест свою еду ({self.diet}).")

    def sleep(self):
        print(f"{self.name} спит, набирая силы.")

    def make_sound(self):
        print(f"{self.name} издает звук.")

    def move(self):
        print(f"{self.name} перемещается по {self.habitat}.")

# Класс для пресмыкающихся, наследуется от Animals
class Reptiles(Animals):
    def __init__(self, name, age, weight, habitat, diet, unique_attr1, unique_attr2):
        super().__init__(name, age, weight, habitat, diet)
        self.unique_attr1 = unique_attr1 
        self.unique_attr2 = unique_attr2

    def crawl(self):
        print(f"{self.name} ползет по земле.")

    def shed_skin(self):
        print(f"{self.name} сбрасывает кожу для обновления.")

    def bask_in_sun(self):
        print(f"{self.name} греется на солнце, чтобы повысить температуру тела.")

    def lay_eggs(self):
        print(f"{self.name} откладывает яйца.")

# Создаем три объекта класса Reptiles с уникальными атрибутами
snake = Reptiles(name="Змея", age=5, weight=2, habitat="джунгли", diet="мясо", unique_attr1="длина 2 м", unique_attr2="ядовитая")
lizard = Reptiles(name="Ящерица", age=3, weight=0.3, habitat="пустыня", diet="насекомые", unique_attr1="зеленая окраска", unique_attr2="длина хвоста 15 см")
turtle = Reptiles(name="Черепаха", age=100, weight=10, habitat="пруд", diet="растения", unique_attr1="размер панциря 30 см", unique_attr2="длительность жизни 150 лет")

# Класс для млекопитающих, наследуется от Animals
class Mammals(Animals):
    def __init__(self, name, age, weight, habitat, diet, unique_attr1, unique_attr2):
        super().__init__(name, age, weight, habitat, diet)
        self.unique_attr1 = unique_attr1
        self.unique_attr2 = unique_attr2

    def run(self):
        print(f"{self.name} бежит с большой скоростью.")

    def hunt(self):
        print(f"{self.name} охотится для пропитания.")

    def nurture_young(self):
        print(f"{self.name} заботится о своем потомстве.")

    def communicate(self):
        print(f"{self.name} общается с другими представителями своего вида.")

# Создаем три объекта класса Mammals с уникальными атрибутами
lion = Mammals(name="Лев", age=8, weight=190, habitat="саванна", diet="мясо", unique_attr1="размер гривы большой", unique_attr2="сила 10")
elephant = Mammals(name="Слон", age=25, weight=5000, habitat="лес", diet="растения", unique_attr1="длина хобота 2 м", unique_attr2="размер бивней большой")
kangaroo = Mammals(name="Кенгуру", age=6, weight=85, habitat="степь", diet="растения", unique_attr1="высота прыжка 3 м", unique_attr2="размер сумки 15 см")

# Класс для шоу в зоопарке
class ZooShow:
    def __init__(self, show_name, ticket_price, animal_performer):
        self.show_name = show_name
        self.ticket_price = ticket_price
        self.animal_performer = animal_performer
        self.tickets_sold = 0

    def perform_show(self):
        print(f"Шоу '{self.show_name}' начинается!")
        self.animal_performer.make_sound()
        self.animal_performer.move()

    def display_info(self):
        print(f"Название шоу: {self.show_name}")
        print(f"Цена билета: {self.ticket_price}")
        print(f"Участник шоу: {self.animal_performer.name}, возраст: {self.animal_performer.age}")

    def sell_ticket(self, quantity=1):
        self.tickets_sold += quantity
        print(f"Продано билетов: {quantity}")

    def calculate_revenue(self):
        revenue = self.ticket_price * self.tickets_sold
        print(f"Общая выручка от продажи билетов: {revenue}")
        return revenue

# Пример создания шоу с участием одного из животных
lion_show = ZooShow(show_name="Королевское Рычание", ticket_price=15, animal_performer=lion)
lion_show.display_info()
lion_show.sell_ticket(30)
lion_show.perform_show()
lion_show.calculate_revenue()
