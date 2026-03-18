import pygame
import sys
import random

LARGURA_TELA = 800
ALTURA_TELA = 600
COR_FUNDO = (0, 0, 0)
FPS = 60


class ColisaoDVD:
    def __init__(
        self,
        texto: str,
        fonte: pygame.font.Font,
        pos_inicial: tuple,
        velocidade_base: int = 3
    ):
        self.texto_str = texto
        self.fonte = fonte
        self.texto_renderizado = None

        self.mudar_cor()
        self.rect = self.texto_renderizado.get_rect(center=pos_inicial)

        self.vel_x = random.choice([-velocidade_base, velocidade_base])
        self.vel_y = random.choice([-velocidade_base, velocidade_base])

    def mudar_cor(self):
        cor = (
            random.randint(50, 255),
            random.randint(50, 255),
            random.randint(50, 255)
        )
        self.texto_renderizado = self.fonte.render(
            self.texto_str,
            True,
            cor
        )

    def atualizar_posicao(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        bateu_na_borda = False

        if self.rect.left <= 0:
            self.rect.left = 0
            self.vel_x *= -1
            bateu_na_borda = True

        elif self.rect.right >= LARGURA_TELA:
            self.rect.right = LARGURA_TELA
            self.vel_x *= -1
            bateu_na_borda = True

        if self.rect.top <= 0:
            self.rect.top = 0
            self.vel_y *= -1
            bateu_na_borda = True

        elif self.rect.bottom >= ALTURA_TELA:
            self.rect.bottom = ALTURA_TELA
            self.vel_y *= -1
            bateu_na_borda = True

        if bateu_na_borda:
            self.mudar_cor()

    def desenhar(self, tela: pygame.Surface):
        tela.blit(self.texto_renderizado, self.rect)

    def checar_colisao_com(self, texto_dvd2: "ColisaoDVD"):
        if self.rect.colliderect(texto_dvd2.rect):
            self.vel_x *= -1
            self.vel_y *= -1
            texto_dvd2.vel_x *= -1
            texto_dvd2.vel_y *= -1

            self.rect.x += self.vel_x * 2
            self.rect.y += self.vel_y * 2
            texto_dvd2.rect.x += texto_dvd2.vel_x * 2
            texto_dvd2.rect.y += texto_dvd2.vel_y * 2

            self.mudar_cor()
            texto_dvd2.mudar_cor()


def main():
    pygame.init()

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption("Simulação DVD Pygame")

    clock = pygame.time.Clock()
    fonte = pygame.font.SysFont(None, 50)

    texto1 = ColisaoDVD(
        "DVD",
        fonte,
        (LARGURA_TELA // 3, ALTURA_TELA // 3)
    )

    texto2 = ColisaoDVD(
        "DVD",
        fonte,
        (int(LARGURA_TELA / 1.5), int(ALTURA_TELA / 1.5))
    )

    rodando = True

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        texto1.atualizar_posicao()
        texto2.atualizar_posicao()

        texto1.checar_colisao_com(texto2)

        tela.fill(COR_FUNDO)

        texto1.desenhar(tela)
        texto2.desenhar(tela)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
