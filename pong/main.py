import pygame
import sys

pygame.init()

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

LARGURA_TELA = 800
ALTURA_TELA = 600

tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Pong")

RAQUETE_LARGURA = 10
RAQUETE_ALTURA = 60
TAMANHO_BOLA = 7

VELOCIDADE_BOLA_X = 5
VELOCIDADE_BOLA_Y = 5

rodando = False


def menu_principal():
    global rodando
    while not rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    rodando = True
                    return

        tela.fill(PRETO)

        font = pygame.font.SysFont(None, 50)
        text = font.render("Pong", True, BRANCO)
        text_rect = text.get_rect(
            center=(LARGURA_TELA // 2, ALTURA_TELA // 4 + 50)
        )
        tela.blit(text, text_rect)

        font_blynk = pygame.font.SysFont(None, 26)
        tempo = pygame.time.get_ticks()

        if tempo % 2000 < 1000:
            text_blynk = font_blynk.render(
                "Pressione ESPAÇO para jogar",
                True,
                BRANCO
            )
            text_blynk_rect = text_blynk.get_rect(
                center=(LARGURA_TELA // 2, ALTURA_TELA // 2 + 60)
            )
            tela.blit(text_blynk, text_blynk_rect)

        pygame.display.flip()


clock = pygame.time.Clock()

player1_x = 15
player1_y = ALTURA_TELA // 2 - RAQUETE_ALTURA // 2

player2_x = LARGURA_TELA - 15 - RAQUETE_LARGURA
player2_y = ALTURA_TELA // 2 - RAQUETE_ALTURA // 2

bola_x = LARGURA_TELA // 2 - TAMANHO_BOLA // 2
bola_y = ALTURA_TELA // 2 - TAMANHO_BOLA // 2

velocidade_bola_x = VELOCIDADE_BOLA_X
velocidade_bola_y = VELOCIDADE_BOLA_Y

score_player1 = 0
score_player2 = 0

menu_principal()

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill(PRETO)

    bola_x += velocidade_bola_x
    bola_y += velocidade_bola_y

    bola_rect = pygame.Rect(
        bola_x,
        bola_y,
        TAMANHO_BOLA,
        TAMANHO_BOLA
    )

    player1_rect = pygame.Rect(
        player1_x,
        player1_y,
        RAQUETE_LARGURA,
        RAQUETE_ALTURA
    )

    player2_rect = pygame.Rect(
        player2_x,
        player2_y,
        RAQUETE_LARGURA,
        RAQUETE_ALTURA
    )

    if bola_rect.colliderect(player1_rect) or bola_rect.colliderect(player2_rect):
        velocidade_bola_x = -velocidade_bola_x

    if bola_y <= 0 or bola_y >= ALTURA_TELA - TAMANHO_BOLA:
        velocidade_bola_y = -velocidade_bola_y

    if bola_x <= 0:
        score_player2 += 1
        bola_x = LARGURA_TELA // 2 - TAMANHO_BOLA // 2
        bola_y = ALTURA_TELA // 2 - TAMANHO_BOLA // 2
        velocidade_bola_x = -velocidade_bola_x
        print(f"Player 2: {score_player2}")
        if score_player2 >= 2:
            print("Player 2 venceu!")
            rodando = False

    if bola_x >= LARGURA_TELA - TAMANHO_BOLA:
        score_player1 += 1
        bola_x = LARGURA_TELA // 2 - TAMANHO_BOLA // 2
        bola_y = ALTURA_TELA // 2 - TAMANHO_BOLA // 2
        velocidade_bola_x = -velocidade_bola_x
        print(f"Player 1: {score_player1}")
        if score_player1 >= 10:
            print("Player 1 venceu!")
            rodando = False

    if player2_y + RAQUETE_ALTURA // 2 < bola_y:
        player2_y += 5
    elif player2_y + RAQUETE_ALTURA // 2 > bola_y:
        player2_y -= 5

    if player2_y < 0:
        player2_y = 0
    elif player2_y > ALTURA_TELA - RAQUETE_ALTURA:
        player2_y = ALTURA_TELA - RAQUETE_ALTURA

    pygame.draw.rect(
        tela,
        BRANCO,
        (player1_x, player1_y, RAQUETE_LARGURA, RAQUETE_ALTURA)
    )

    pygame.draw.rect(
        tela,
        BRANCO,
        (player2_x, player2_y, RAQUETE_LARGURA, RAQUETE_ALTURA)
    )

    pygame.draw.circle(
        tela,
        BRANCO,
        (bola_x, bola_y),
        TAMANHO_BOLA
    )

    font_score = pygame.font.SysFont(None, 36)
    score_text = font_score.render(
        f"{score_player1} - {score_player2}",
        True,
        BRANCO
    )

    tela.blit(
        score_text,
        score_text.get_rect(center=(LARGURA_TELA // 2, 30))
    )

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and player1_y > 0:
        player1_y -= 5

    if keys[pygame.K_DOWN] and player1_y < ALTURA_TELA - RAQUETE_ALTURA:
        player1_y += 5

    pygame.display.flip()
    clock.tick(60)
