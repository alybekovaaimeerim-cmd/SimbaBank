"""контрольная работа №1"""
class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        return f"{self.name} готов к бою!"


class MageHero(Hero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp

    def action(self):
        return f"Маг {self.name} кастует заклинание! MP: {self.mp}"


class WarriorHero(MageHero):
    def action(self):
        return f"Воин {self.name} рубит мечом! Уровень: {self.lvl}"


class BankAccount:
    def __init__(self, hero, balance, password, bank_name):
        self.hero = hero
        self._balance = balance
        self.__password = password
        self.bank_name = bank_name

    def login(self, password):
        return password == self.__password

    @property
    def full_info(self):
        return f"{self.hero.name} | Баланс: {self._balance} SOM"

    def get_bank_name(self):
        return self.bank_name

    def bonus_for_level(self):
        return self.hero.lvl * 10

    def __str__(self):
        return f"{self.hero.name} | Баланс: {self._balance} SOM"

    def __add__(self, other):
        if type(self.hero) == type(other.hero):
            return self._balance + other._balance
        else:
            return "Ошибка: Нельзя сложить счета героев разных классов!"

    def __eq__(self, other):
        if not isinstance(other, BankAccount):
            return False

        return (
            type(self.hero) == type(other.hero)
            and self.hero.lvl == other.hero.lvl
        )


# --- Создание героев из Solo Leveling ---

jin_woo1 = MageHero(
    name="Сон Джин-Ву",
    lvl=50,
    hp=1000,
    mp=150
)

jin_woo2 = MageHero(
    name="Сон Джин-Ву",
    lvl=50,
    hp=1000,
    mp=200
)

igris = WarriorHero(
    name="Игрис",
    lvl=50,
    hp=1500,
    mp=50
)


# --- Создание банковских счетов ---

acc1 = BankAccount(
    hero=jin_woo1,
    balance=5000,
    password="1234",
    bank_name="Simba"
)

acc2 = BankAccount(
    hero=jin_woo2,
    balance=3000,
    password="5678",
    bank_name="Simba"
)

acc3 = BankAccount(
    hero=igris,
    balance=2000,
    password="9999",
    bank_name="Simba"
)


# --- Проверка action() ---

print(acc1.hero.action())
print(acc3.hero.action())


# --- Проверка __str__ ---

print(acc1)
print(acc2)


# --- Проверка методов BankAccount ---

print("Банк:", acc1.get_bank_name())
print("Бонус за уровень:", acc1.bonus_for_level(), "SOM")


# --- Магический метод __add__ ---

print("\n=== Проверка __add__ ===")

print("Сумма счетов двух магов:", acc1 + acc2)
print("Сумма Джин-Ву и Игриса:", acc1 + acc3)


# --- Магический метод __eq__ ---

print("\n=== Проверка __eq__ ===")

print("Jin-Woo1 == Jin-Woo2 ?", acc1 == acc2)
print("Jin-Woo == Igris ?", acc1 == acc3)