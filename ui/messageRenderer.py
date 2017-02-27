# --------------------------------------------+
# Rendering messages
# --------------------------------------------+

# x and y are the center of the message
import Constants


def renderMessages(game, screen, screen_w, screen_h, font):
    for i in range(0, len(game.activeMessages)):
        txt = font.render(game.activeMessages[i].text, True, Constants.WHITE)
        print str(txt.get_height())
        new_x = screen_w / 2 - txt.get_width() / 2
        new_y = screen_h / 2 - (i + 1) * 1.25 * txt.get_height()
        screen.blit(txt, (new_x, new_y))
