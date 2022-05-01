from functools import wraps

from flask import Flask, request, render_template, redirect, url_for

from data.equipment.EquipmentData import EquipmentData
from data.units.BaseUnit import BaseUnit
from data.units.Enemy import Enemy
from data.units.Player import Player
from data.utils import classes_list, load_equip
from game.arena import Arena

app = Flask(__name__)
app.url_map.strict_slashes = False

equipment: EquipmentData = load_equip()

char_render_data = {
    "classes": classes_list,
    "weapons": equipment.weapons,
    "armors": equipment.armor,
}

heroes = {
    "player": Player,
    "enemy": Enemy
}

arena = Arena() # TODO инициализируем класс арены


def game_is_on(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if arena.game_is_on:
            return func(*args, **kwargs)
        if arena.game_results:
            return render_template("fight.html", heroes=heroes, result=arena.game_results)
        return redirect(url_for("menu_page"))
    return wrapper

@app.route("/")
def menu_page():
    # TODO рендерим главное меню (шаблон index.html)
    return render_template("index.html")


@app.route("/fight/")
def start_fight():
    # TODO выполняем функцию start_game экземпляра класса арена и передаем ему необходимые аргументы
    if not ("player" in heroes and "enemy" in heroes):
        return redirect(url_for("/"))
    arena.game_start(player=heroes["player"], enemy=heroes["enemy"])
    return render_template("fight.html", heroes=heroes, result="Fight!")
    # TODO рендерим экран боя (шаблон fight.html)
    pass

@app.route("/fight/hit")
@game_is_on
def hit():
    # TODO кнопка нанесения удара
    # TODO обновляем экран боя (нанесение удара) (шаблон fight.html)

    res = arena.player_hit()
    return render_template("fight.html", heroes=heroes, result=res)
    # TODO если игра идет - вызываем метод player.hit() экземпляра класса арены
    # TODO если игра не идет - пропускаем срабатывание метода (простот рендерим шаблон с текущими данными)
    pass


@app.route("/fight/use-skill")
@game_is_on
def use_skill():


    return render_template("fight.html", heroes=heroes, result=arena.player_skill())
    # TODO кнопка использования скилла
    # TODO логика пркатикчески идентична предыдущему эндпоинту



@app.route("/fight/pass-turn")
@game_is_on
def pass_turn():


    return render_template("fight.html", heroes=heroes, result=arena.next_turn())
    # TODO кнопка пропус хода
    # TODO логика пркатикчески идентична предыдущему эндпоинту
    # TODO однако вызываем здесь функцию следующий ход (arena.next_turn())



@app.route("/fight/end-fight")
def end_fight():
    # TODO кнопка завершить игру - переход в главное меню
    # return render_template("index.html", heroes=heroes)
    return redirect(url_for("menu_page"))


@app.route("/choose-hero/", methods=['post', 'get'])
def choose_hero():
    # TODO кнопка выбор героя. 2 метода GET и POST
    # TODO на GET отрисовываем форму.
    if request.method == "GET":
        char_render_data["header"] = "Выберите героя!"
        char_render_data["choice"] = "Выбрать врага"
        return render_template(
            "hero_choosing.html",
            result=char_render_data,
        )

    # TODO на POST отправляем форму и делаем редирект на эндпоинт choose enemy
    if request.method == "POST":
        heroes["player"] = Player(
            char_class=classes_list[request.form["class"]],
            weapon=equipment.get_weapon(request.form["weapon"]),
            armor=equipment.get_armor(request.form["armor"]),
            name=request.form["name"],
        )

        return redirect(url_for("choose_enemy"))


@app.route("/choose-enemy/", methods=['post', 'get'])
def choose_enemy():
    # TODO кнопка выбор соперников. 2 метода GET и POST
    # TODO также на GET отрисовываем форму.
    if request.method == "GET":
        char_render_data["header"] = "Выберите врага!"
        char_render_data["choice"] = "Начать игру"
        return render_template(
            "hero_choosing.html",
            result=char_render_data,
        )
    # TODO а на POST отправляем форму и делаем редирект на начало битвы
    if request.method == "POST":
        heroes["enemy"] = Enemy(
            char_class=classes_list[request.form["class"]],
            weapon=equipment.get_weapon(request.form["weapon"]),
            armor=equipment.get_armor(request.form["armor"]),
            name=request.form["name"],
        )

        return redirect(url_for("start_fight"))


if __name__ == "__main__":
    app.run()
