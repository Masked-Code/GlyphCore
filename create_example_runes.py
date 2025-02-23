from utils import RuneGenerator
from known_spells import get_fireball, get_cure_wounds, get_wish

def create_runes():
    fireball = get_fireball()
    fireball_rune_gen = RuneGenerator(fireball)
    fireball_rune_gen.generate_rune("fireball_rune_example.png")

    cure_wounds = get_cure_wounds()
    cure_wounds_rune_gen = RuneGenerator(cure_wounds)
    cure_wounds_rune_gen.generate_rune("cure_wounds_rune_example.png")

    wish = get_wish()
    cure_wounds_rune_gen = RuneGenerator(wish)
    cure_wounds_rune_gen.generate_rune("wish_rune_example.png")

    print(fireball)
    print("\n" + "-"*50 + "\n")
    print(cure_wounds)
    print("\n" + "-"*50 + "\n")
    print(wish)

if __name__ == "__main__":
    create_runes()