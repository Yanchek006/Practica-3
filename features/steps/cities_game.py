from behave import *

use_step_matcher("re")


@given("игрок начинает новую игру")
def step_impl(context):
    from cities_game import CityGame
    context.game: CityGame = CityGame()
    if not context.game:
        raise AssertionError(f'Игра не создана')


@when('игрок добавляет город "Moscow"')
def step_impl(context):
    from cities_game import CityGame
    context.game: CityGame
    context.game.add_city('Moscow')
    if len(context.game.cities) == 0:
        raise AssertionError(f'Игрок не смог добавить Moscow')


@then('"Moscow" должна быть в списке городов')
def step_impl(context):
    from cities_game import CityGame
    context.game: CityGame
    result = context.game.check_city_exists('Moscow')
    if not result:
        raise AssertionError(f'Moscow не существует в списке')


@when('игрок добавляет город "London_AXFDHGJH"')
def step_impl(context):
    from cities_game import CityGame
    context.game: CityGame
    context.game.add_city('London_AXFDHGJH')
    if len(context.game.cities) != 0:
        raise AssertionError(f'Игрок смог добавить London_AXFDHGJH')



@then('"London_AXFDHGJH" не должна быть в списке городов')
def step_impl(context):
    from cities_game import CityGame
    context.game: CityGame
    result = context.game.check_city_exists('London_AXFDHGJH')
    if result:
        raise AssertionError(f'London_AXFDHGJH существует в списке')



@step('игрок добавляет город "Moscow"')
def step_impl(context):
    from cities_game import CityGame
    context.game: CityGame
    context.game.add_city('Moscow')
    if len(context.game.cities) == 0:
        raise AssertionError(f'Игрок не смог добавить Moscow')


@when('игрок проверяет город "Moscow"')
def step_impl(context):
    from cities_game import CityGame
    context.game: CityGame
    result = context.game.is_valid_city('Moscow')
    if not result:
        raise AssertionError(f'Moscow не прошел проверку как город')


@then('"Moscow" должна существовать в списке городов')
def step_impl(context):
    from cities_game import CityGame
    context.game: CityGame
    result = context.game.check_city_exists('Moscow')
    if not result:
        raise AssertionError(f'Moscow не существует в списке')


@when('игрок проверяет город "London_AXFDHGJH"')
def step_impl(context):
    from cities_game import CityGame
    context.game: CityGame
    result = context.game.is_valid_city('London_AXFDHGJH')
    if result:
        raise AssertionError(f'London_AXFDHGJH прошел проверку как город')


@then('"London_AXFDHGJH" не должна существовать в списке городов')
def step_impl(context):
    from cities_game import CityGame
    context.game: CityGame
    result = context.game.check_city_exists('London_AXFDHGJH')
    if result:
        raise AssertionError(f'London_AXFDHGJH существует в списке')
