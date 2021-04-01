# Muista requirements .txt
import grid
import pygame
from label import Label
from input_handler import handle_input


def init():
    print("Conway's game of life", "\nOhjeet: Space = pysäytä/jatka generoimista, R = generoi uusi aloitustila")
    args, successful = handle_input()
    if not successful:
        init()
    else:
        main(args)


def main(args):
    pygame.init()
    screen = pygame.display.set_mode((600, 630))
    pygame.display.set_caption("Conway's game of life")
    running = True

    cur_grid = grid.CellGrid(args[0], args[1], args[2], args[3], screen)
    # cur_grid = grid.CellGrid((50, 50), (255, 255, 255), (0, 0, 0), 0, screen)

    font = pygame.font.SysFont('Sans', 20)
    gen_text = Label(f"Generation 0", font, (255, 255, 255), screen, (5, 605))

    while running:
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    cur_grid.change_running_state()
                elif e.key == pygame.K_r:
                    cur_grid.generate_new_starting_grid()
                elif e.key == pygame.K_ESCAPE:
                    exit(1)

        gen_text.update_label(f"Generation {cur_grid.cur_generation}")
        gen_text.render_label()

        cur_grid.generate_next_generation()
        cur_grid.render_grid()

        pygame.display.flip()
        pygame.time.wait(cur_grid.sim_speed)


if __name__ == "__main__":
    init()
