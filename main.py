import random


class Hero:

    def set_hero_data(self, first_name_list, last_name_list, health_points, attack_points): # характеристики героя
        self.first_name = random.choice(first_name_list)
        self.last_name = random.choice(last_name_list)
        self.health_points = health_points
        self.attack_points = attack_points

    def set_health(self, hit_points):
        self.health_points -= hit_points

    def get_health_points(self):
        return self.health_points

    def get_attack_points(self):
        return self.attack_points


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
        print(f'ГЕРОЙ №1: {hero_1.first_name} {hero_1.last_name} // ОЗ: {hero_1.health_points} // ОА: {hero_1.attack_points}')
        print(f'ГЕРОЙ №2: {hero_2.first_name} {hero_2.last_name} // ОЗ: {hero_2.health_points} // ОА: {hero_2.attack_points}')

        while hero_1.health_points > 0 and hero_2.health_points > 0:
            print('\n', '-' * 10, 'РАУНД', '-' * 10)

            n = random.randint(1, 2) # случайный выбор того героя, который будет бить первый
            if n == 1:
                hero_2.set_health(hero_1.get_attack_points())
                print(f'{hero_1.first_name} {hero_1.last_name} ударил {hero_2.first_name} {hero_2.last_name}')
            else:
                hero_1.set_health(hero_2.get_attack_points())
                print(f'{hero_2.first_name} {hero_2.last_name} ударил {hero_1.first_name} {hero_1.last_name}')

            print(' ' * 10, 'РЕЗУЛЬТАТ', ' ' * 10)
            print(f'ГЕРОЙ №1: {hero_1.first_name} {hero_1.last_name} // ОЗ: {hero_1.health_points} // ОА: {hero_1.attack_points}')
            print(f'ГЕРОЙ №2: {hero_2.first_name} {hero_2.last_name} // ОЗ: {hero_2.health_points} // ОА: {hero_2.attack_points}')


        if hero_1.health_points < 0:
            print(f'Победил: {hero_2.first_name} {hero_2.last_name}')
        if hero_2.health_points < 0:
            print(f'Победил: {hero_1.first_name} {hero_1.last_name}')


if __name__ == '__main__':

    unit_1 = Hero()
    unit_2 = Hero()
    b = Battle()

    first_names = ['Петя', 'Рома', 'Денис', 'Коля', 'Стас', 'Женя', 'Саша', 'Костя']
    last_names = ['Красный', 'Оранжевый', 'Жёлтый', 'Зелёный', 'Голубой', 'Синий', 'Фиолетовый', 'Розовый']

    def health_points():
        return random.randint(10, 20)

    def attack_points():
        return random.randint(1, 5)

    unit_1.set_hero_data(first_names, last_names, health_points(), attack_points())
    unit_2.set_hero_data(first_names, last_names, health_points(), attack_points())
    print(unit_1.__dict__)
    print(unit_2.__dict__)

    b.game_round(unit_1, unit_2)




# unit test
# assert len(w) == e
#
# #Round
# while len(w) > 1:
#     w.append(Duel.draka(w.pop(), w.pop()))
# # print(w[0].first_name)
