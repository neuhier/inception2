# Contains rendering functions


# --------------------------------------------------------------------------------------------------------------+
# Render the Heads Up Display (Life points, boosts, weapons, ...)
# --------------------------------------------------------------------------------------------------------------+
import math


# --------------------------------------------------------------------------------------------------------------+
# Render textures (just the ones that are needed to fill the screen
# --------------------------------------------------------------------------------------------------------------+
# Get the texture-grid min-and-max indicies for the things to be rendered
def get_render_rect(game):
    x_range = math.ceil(game.screen_w / game.imgMngr.texture_size[0] / 2.0)
    y_range = math.ceil(game.screen_h / game.imgMngr.texture_size[1] / 2.0)

    x_min = max(0, int(game.player.position[0] - x_range) - 1)  # Indices cannot become negative
    x_max = min(int(math.ceil(game.player.position[0] + x_range)) + 1, len(game.level.texture_grid))
    y_min = max(0, int(game.player.position[1] - y_range) - 1)
    y_max = min(int(math.ceil(game.player.position[1] + y_range)) + 1,
                len(game.level.texture_grid[0]))  # Maximum height is number of tiles of texture_grid
    return [x_min, x_max, y_min, y_max]


# Collect all textures that should be rendered and then draw them
def renderTextures(game):
    render_rect = get_render_rect(game)

    for i in range(render_rect[0], render_rect[1]):  # Render each relevant texture
        for j in range(render_rect[2], render_rect[3]):
            screen_pos_x = game.player.rect.centerx - (game.player.position[0] - i + .5) * game.imgMngr.texture_size[
                0]  # Texture position on the screen relative to player
            screen_pos_y = game.player.rect.centery - (game.player.position[1] - j + .5) * game.imgMngr.texture_size[1]
            game.screen.blit(
                game.imgMngr.all_textures[list(game.imgMngr.all_textures.keys())[int(game.level.texture_grid[i, j] - 1)]],
                        (screen_pos_x, screen_pos_y))


# --------------------------------------------------------------------------------------------------------------+
# Render items/villians that are visible on the screen
# --------------------------------------------------------------------------------------------------------------+
# Set the image position of a Sprite to the correct position on the screen
def set_screen_pos(game, item):
    screen_pos_x = game.player.rect.centerx - (game.player.position[0] - item.position[0] - 0.5) * \
                                              game.imgMngr.texture_size[
        0]
    screen_pos_y = game.player.rect.centery - (game.player.position[1] - item.position[1] - 0.5) * \
                                              game.imgMngr.texture_size[
        1]
    item.rect.centerx = screen_pos_x
    item.rect.centery = screen_pos_y


def renderItems(game):
    render_rect = get_render_rect(game)

    # Render all visible items
    for i in game.level.items:
        if render_rect[0] <= i.position[0] <= render_rect[1] and render_rect[2] <= i.position[1] <= render_rect[3]:
            game.level.render_items.add(i)
            set_screen_pos(game, i)
        else:
            game.level.render_items.remove(i)

    # Add projectiles to list of things to render
    for i in game.level.projectiles:
        if render_rect[0] <= i.position[0] <= render_rect[1] and render_rect[2] <= i.position[1] <= render_rect[3]:
            game.level.render_projectiles.add(i)
            set_screen_pos(game, i)
        else:
            game.level.render_projectiles.remove(i)

    # Add villians to list of things to render
    for i in game.level.chars:
        if render_rect[0] <= i.position[0] <= render_rect[1] and render_rect[2] <= i.position[1] <= render_rect[3]:
            game.level.render_chars.add(i)
            set_screen_pos(game, i)
        else:
            game.level.render_chars.remove(i)

    # Now draw the stuff
    game.level.render_chars.draw(game.screen)
    game.level.render_items.draw(game.screen)
    game.level.render_projectiles.draw(game.screen)
