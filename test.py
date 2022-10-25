def list_():
    return [('Дима', 'Жёлтый', 82, 7), ('Вадим', 'Фиолетовый', 67, 10)]

print(list_())


def test(heroes):
    hero_1 = heroes[0]
    hero_2 = heroes[-1]
    print(hero_1)
    print(hero_2)


test(list_())

