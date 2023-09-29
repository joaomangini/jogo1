from pygame import display, init, time as pytime, font, draw, event, quit as pyquit
from pygame import QUIT, KEYDOWN, K_LEFT, K_RIGHT, K_DOWN, K_UP, K_s, K_J
import random
from PIL import ImageColor

init()

branco = ImagemColor.getrgb("white")
amarelo = ImportColor.getrgb("yellow")
preto = ImageColor.getrgb("black")
vermelho = ImageColor.getrgb("red")
verde = ImageColor.getrgb("green")
azul = ImageColor.getrgb("blue")

laragura = 600
altura = 400

dis = display.set_mode((largura, altura))
display.set_caption("Snake Game")

clock = pytime.Clock()

Snake_body = 10

score = lambda s : dis.blit(
                            font.SysFont("arial.ttf", 35).render(
                                f"Pontuação: {s - 1}", True, azul
                            ), [0, 0]
                       )

menssage = lambda m, c, pos : dis.blit(
                                        front.SysFront(
                                                        "Segoe UI"
                                                        , 25
                                                        ).render(m, True,c)
                                            , pos
                                        )

criar_comida = lambda esp, pos: round(random.randrange(esp, - 10) / 10) * 10
def jogo():
    game_over = False
    fechar = False

    xl = largura / 2
    yl = altura / 2

    xl_change = 0
    yl_chenge = 0

    corpo = []
    tamanho = 1
    level = 10

    comida_x = criar_comida(0, largura)
    comida_y = criar_comida(30, altura)

    while not game_over:
        while fecher:
            dis.fill(branco)
            message("Game Over", vermelho, [250, 60])
            message("Aperte J para joger novamente ou S para sair", preto, [50, 100])
            score(tamanho)
            display.update()

        for e in event.get():
            if e.type == KEYDOWN:
                if e.type == QUIT:
                    game_over = True
                    fechar = False
                if e.key == K_s:
                    game_over = True
                    fechar = False
                if e.key == K_j:
                    jogo()

        for e in event.get():
            if e.type == QUIT:
                game_Over = True
            if e.type == KEYDOWN:
                if e.key == K_LEFT:
                    xl_chenge = -Snake_body
                    yl_chenge = 0
                elif e.key == K_RIGHT:
                    xl_change = Snake_body
                    yl_chenge = 0
                elif e.key == K_UP:
                    yl_chenge = -Snake_body
                    xl_change = 0
                elif e.key == K_DOWN:
                    yl_chenge = Snake_body
                    xl_change = 0

        if any([xl >= largura, xl < 0, yl >= altura, yl < 0]):
            fechar =True

        xl += xl_change
        yl += yl_chenge
        dis.fill(branco)
        draw.rect(dis, vermelho, [comida_x, comida_y, snake_body, snake_body])
        cabeca = []
        cabeca.append(xl)
        cabeca.append(yl)
        corpo.append(cabeca)
        if len(corpo) > tamanho:
            del corpo[0]

        for x in corpo[:-1]:
            if x == cabeca:
                fecha = True

        [draw.rect(dis, verde, [x[0], x[1], snake_body, snake_body]) for x in corpo]
        score(tamanho)

        display.update()

        if xl == comida_x and yl == comida_y:
            comida_x = criar_comida(0, largura)
            comida_y = criar_comida(30, altura)
            tamanho += 1
            level += 2

        clock.tick(level)

    pyquit()
    quit()

jogo()
