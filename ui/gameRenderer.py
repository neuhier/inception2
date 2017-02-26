# Contains rendering functions


# --------------------------------------------------------------------------------------------------------------+
# Render the Heads Up Display (Life points, boosts, weapons, ...)
# --------------------------------------------------------------------------------------------------------------+
import datetime
import math

import pygame

import Constants
import util


# Render the weapons in the inventory
def renderInventory(level, screen, x_offset, y_offset):
    # Background
    #    pygame.draw.rect(screen, Constants.GRAY, (11,11,50,32))
    # Show equiped weapon
    wpn_img = level.all_images[level.player.get_current_weapon().name]
    screen.blit(wpn_img, (10 + x_offset, 10 + y_offset))


# Render how long it will take to load the weapon
def renderLoadingTime(level, screen, width, height, x_offset, y_offset):
    pygame.draw.rect(screen, Constants.WHITE, (5 + x_offset, 5 + y_offset, width + 2, height + 2), 0)
    # Calculate loading time left
    max_loading_time = level.player.get_current_weapon().reload_time
    time_left = max_loading_time - (datetime.datetime.now() - level.player.last_shot).total_seconds()
    if time_left > 0:
        pygame.draw.rect(screen, Constants.BLACK, (6 + x_offset,
                                                   6 + y_offset,
                                                   width,
                                                   height / (max_loading_time) * time_left))


# Return the position of the text displayed on the top right corner
def textPosition(text, n, screen_w):
    new_x = screen_w - text.get_width()
    new_y = 0 + text.get_height() * n + (n + 1) * 10
    return [new_x, new_y]


def renderHUD(level, screen, screen_w, screen_h, font):
    # Render player info
    player_htps = font.render("Hitpoints: " + str(level.player.hitpoints[0]) + "/" + str(level.player.hitpoints[1]),
                              True, util.Constants.WHITE)
    screen.blit(player_htps, textPosition(player_htps, 0, screen_w))
    player_pos = font.render(
        "Pos: [" + str(round(level.player.position[0], 1)) + "/" + str(round(level.player.position[1], 1)) + "]", True,
        util.Constants.WHITE)
    screen.blit(player_pos, textPosition(player_pos, 1, screen_w))

    renderInventory(level, screen, 10, 0)
    renderLoadingTime(level, screen, 5, 18, 0, 10)



# --------------------------------------------------------------------------------------------------------------+
# Render textures (just the ones that are needed to fill the screen
# --------------------------------------------------------------------------------------------------------------+
# Get the texture-grid min-and-max indicies for the things to be rendered
def get_render_rect(level, screen_width, screen_height):
    # Get the parts of the texture_grid that need to be rendered
    x_range = math.ceil(screen_width / level.texture_size[0] / 2.0)
    y_range = math.ceil(screen_height / level.texture_size[1] / 2.0)

    x_min = max(0, int(level.player.position[0] - x_range) - 1)  # Indices cannot become negative
    x_max = min(int(math.ceil(level.player.position[0] + x_range)) + 1, len(level.texture_grid))
    y_min = max(0, int(level.player.position[1] - y_range) - 1)
    y_max = min(int(math.ceil(level.player.position[1] + y_range)) + 1,
                len(level.texture_grid[0]))  # Maximum height is number of tiles of texture_grid
    return [x_min, x_max, y_min, y_max]


# Collect all textures that should be rendered and then draw them
def renderTextures(level, screen_width, screen_height, screen):
    render_rect = get_render_rect(level, screen_width, screen_height)

    for i in range(render_rect[0], render_rect[1]):  # Render each relevant texture
        for j in range(render_rect[2], render_rect[3]):
            screen_pos_x = level.player.rect.centerx - (level.player.position[0] - i + .5) * level.texture_size[
                0]  # Texture position on the screen relative to player
            screen_pos_y = level.player.rect.centery - (level.player.position[1] - j + .5) * level.texture_size[1]
            screen.blit(level.all_textures[level.all_textures.keys()[int(level.texture_grid[i, j] - 1)]],
                        (screen_pos_x, screen_pos_y))


# --------------------------------------------------------------------------------------------------------------+
# Render items/villians that are visible on the screen
# --------------------------------------------------------------------------------------------------------------+
# Set the image position of a Sprite to the correct position on the screen
def set_screen_pos(level, item):
    screen_pos_x = level.player.rect.centerx - (level.player.position[0] - item.position[0] - 0.5) * level.texture_size[
        0]
    screen_pos_y = level.player.rect.centery - (level.player.position[1] - item.position[1] - 0.5) * level.texture_size[
        1]
    item.rect.centerx = screen_pos_x
    item.rect.centery = screen_pos_y


def renderItems(level, screen_width, screen_height, screen):
    render_rect = get_render_rect(level, screen_width, screen_height)

    # Render all visible items
    for i in level.items:
        if render_rect[0] <= i.position[0] <= render_rect[1] and render_rect[2] <= i.position[1] <= render_rect[3]:
            level.render_items.add(i)
            set_screen_pos(level, i)
        else:
            level.render_items.remove(i)

    # Add projectiles to list of things to render
    for i in level.projectiles:
        if render_rect[0] <= i.position[0] <= render_rect[1] and render_rect[2] <= i.position[1] <= render_rect[3]:
            level.render_projectiles.add(i)
            set_screen_pos(level, i)
        else:
            level.render_projectiles.remove(i)

    # Add villians to list of things to render
    for i in level.chars:
        if render_rect[0] <= i.position[0] <= render_rect[1] and render_rect[2] <= i.position[1] <= render_rect[3]:
            level.render_chars.add(i)
            set_screen_pos(level, i)
        else:
            level.render_chars.remove(i)

    # Now draw the stuff
    level.render_chars.draw(screen)
    level.render_items.draw(screen)
    level.render_projectiles.draw(screen)


# --------------------------------------------------------------------------------------------------------------+
# Function that renders all
# --------------------------------------------------------------------------------------------------------------+
def renderAll(level, screen_w, screen_h, screen, font):
    renderTextures(level, screen_w, screen_h, screen)
    renderItems(level, screen_w, screen_h, screen)
    renderHUD(level, screen, screen_w, screen_h, font)
