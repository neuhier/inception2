# ------------------------------------------+
# Weapon class
# ------------------------------------------+

class Weapon():
    name = "gun"  # Weapon name is used to get the adequite image for it
    max_range = 50  # Maximum range of weapon in px
    speed = 5  # Movemement speed of projectiles fired by this weapon
    generate_dmgm_fun = None  # A function that will generate the damage of a projectile fired by this weapon

    def __init__(self, name, max_range, speed, reload_time, generate_dmg_fun):
        self.name = name
        self.max_range = max_range
        self.speed = speed
        self.reload_time = reload_time
        self.generate_dmg_fun = generate_dmg_fun
