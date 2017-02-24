# ----------------------------------------------+
# Functions to create different weapons
# ----------------------------------------------+
import random

from gameObjects.weapon import Weapon


# ----------------------------------------------+
# Function to create the basic weapon: Gun
# ----------------------------------------------+
def generate_gun_dmg():
    dmg = random.randint(10, 30)
    return dmg


def generateGun():
    return Weapon("gun", 5, 0.3, 0.25, generate_gun_dmg)


# ----------------------------------------------+
# Function to create the basic weapon: Rifle
# ----------------------------------------------+
def generate_rifle_dmg():
    dmg = random.randint(25, 50)
    return dmg


def generateRifle():
    return Weapon("rifle", 8, 0.3, 0.35, generate_rifle_dmg)

# ----------------------------------------------+
# Function that generates a random weapon
# ----------------------------------------------+
