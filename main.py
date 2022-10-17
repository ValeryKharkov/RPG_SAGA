import random


class Hero:
    def __init__(self, first_name, last_name, health_points, attack_points):
        self.first_name = first_name
        self.last_name = last_name
        self.health_points = health_points
        self.attack_points = attack_points

    def set(self, hit_points):
        self.health_points -= hit_points

    def get_health_points(self):
        return self.health_points

    def get_attack_points(self):
        return self.attack_points

    # def __repr__(self):
    #     return f'{self.first_name} {self.last_name}: hp={self.health_points} ap={self.attack_points}'


class Knight(Hero):
    def __init__(self, first_name, last_name, health_points, attack_points):
        super().__init__(first_name, last_name, health_points, attack_points)


class Archer(Hero):
    def __init__(self, first_name, last_name, health_points, attack_points):
        super().__init__(first_name, last_name, health_points, attack_points)


class Wizard(Hero):
    def __init__(self, first_name, last_name, health_points, attack_points):
        super().__init__(first_name, last_name, health_points, attack_points)


class Battle:
    def game_round(self, hero_1, hero_2):
        while hero_1.health_points > 0 and hero_2.health_points > 0:
            print('--Раунд--')
            hero_1.set(hero_2.get_attack_points())
            print(hero_1.first_name, hero_1.health_points, hero_2.health_points, hero_2.first_name)
            hero_2.set(hero_1.get_attack_points())
            print(hero_1.first_name, hero_1.health_points, hero_2.health_points, hero_2.first_name)

            if hero_1.health_points < 0:
                return hero_2
            if hero_2.health_points < 0:
                return hero_1


def hero_selection():
    """
    Формирование героя из случайных данных
    :return: данные на героя в виде списка
    """
    hero_number = 2
    names = ['Рома', 'Петя', 'Женя', 'Коля', 'Дима', 'Денис', 'Вадим']
    surnames = ['Красный', 'Оранжевый', 'Жёлтый', 'Зелёный', 'Голубой', 'Синий', 'Фиолетовый']
    hero_selection_list = []
    for _ in range(hero_number):
        hero_selection_list.append(
            Hero(random.choice(names), random.choice(surnames), random.randint(50, 100), random.randint(5, 10))
        )
    return hero_selection_list


print(hero_selection())


knight_player = Knight('Рома', 'Красный', 120, 10)
archer_player = Archer('Лучник', 'Синий', 100, 5)
print(knight_player)

battle = Battle()
battle.game_round(knight_player, archer_player)


# unit test
# assert len(w) == e
#
# #Round
# while len(w) > 1:
#     w.append(Duel.draka(w.pop(), w.pop()))
# # print(w[0].first_name)
