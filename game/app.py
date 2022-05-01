from functools import wraps

from flask import Flask, request, render_template, redirect, url_for

from data.equipment.EquipmentData import EquipmentData
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

arena = Arena()


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
    return render_template("index.html")


@app.route("/fight/")
def start_fight():
    if not ("player" in heroes and "enemy" in heroes):
        return redirect(url_for("/"))
    arena.game_start(player=heroes["player"], enemy=heroes["enemy"])
    return render_template("fight.html", heroes=heroes, result="Fight!")
    pass


@app.route("/fight/hit")
@game_is_on
def hit():
    res = arena.player_hit()
    return render_template("fight.html", heroes=heroes, result=res)
    pass


@app.route("/fight/use-skill")
@game_is_on
def use_skill():
    return render_template("fight.html", heroes=heroes, result=arena.player_skill())


@app.route("/fight/pass-turn")
@game_is_on
def pass_turn():
    return render_template("fight.html", heroes=heroes, result=arena.next_turn())


@app.route("/fight/end-fight")
def end_fight():
    return redirect(url_for("menu_page"))


@app.route("/choose-hero/", methods=['post', 'get'])
def choose_hero():
    if request.method == "GET":
        char_render_data["header"] = "Выберите героя!"
        char_render_data["choice"] = "Выбрать врага"
        return render_template(
            "hero_choosing.html",
            result=char_render_data,
        )

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
    if request.method == "GET":
        char_render_data["header"] = "Выберите врага!"
        char_render_data["choice"] = "Начать игру"
        return render_template(
            "hero_choosing.html",
            result=char_render_data,
        )
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
