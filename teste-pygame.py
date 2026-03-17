import pygame
import sys
import random

LARGURA, ALTURA = 800, 600
COR_FUNDO = (0, 0, 0)
FPS = 60

class ColisaoDVD:    
    def __init__(self, texto: str, fonte: pygame.font.Font, pos_inicial: tuple, velocidade_base: int = 3):
        self.texto_str = texto
        self.fonte = fonte
        self.texto_renderizado = None
        
        self.mudar_cor() 
        self.rect = self.texto_renderizado.get_rect(center=pos_inicial)
        
        self.vel_x = random.choice([-velocidade_base, velocidade_base])
        self.vel_y = random.choice([-velocidade_base, velocidade_base])

    def mudar_cor(self):
        cor = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
        self.texto_renderizado = self.fonte.render(self.texto_str, True, cor)

    def atualizar_posicao(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        bateu_na_borda = False

        if self.rect.left <= 0:
            self.rect.left = 0 
            self.vel_x *= -1 
            bateu_na_borda = True

        elif self.rect.right >= LARGURA:
            self.rect.right = LARGURA
            self.vel_x *= -1
            bateu_na_borda = True

        if self.rect.top <= 0:
            self.rect.top = 0
            self.vel_y *= -1
            bateu_na_borda = True
            
        elif self.rect.bottom >= ALTURA:
            self.rect.bottom = ALTURA
            self.vel_y *= -1
            bateu_na_borda = True

        if bateu_na_borda:
            self.mudar_cor()

    def desenhar(self, tela: pygame.Surface):
        tela.blit(self.texto_renderizado, self.rect)

    def checar_colisao_com(self, TextoDVD2: 'ColisaoDVD'):
        if self.rect.colliderect(TextoDVD2.rect):
            self.vel_x *= -1
            self.vel_y *= -1
            TextoDVD2.vel_x *= -1
            TextoDVD2.vel_y *= -1
            
            self.rect.x += self.vel_x * 2
            self.rect.y += self.vel_y * 2
            TextoDVD2.rect.x += TextoDVD2.vel_x * 2
            TextoDVD2.rect.y += TextoDVD2.vel_y * 2
            
            self.mudar_cor()
            TextoDVD2.mudar_cor()

def main():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Simulação DVD Pygame")
    clock = pygame.time.Clock()
    
    fonte = pygame.font.SysFont(None, 50)

    texto1 = ColisaoDVD("DVD", fonte, (LARGURA // 3, ALTURA // 3))
    texto2 = ColisaoDVD("DVD", fonte, (int(LARGURA / 1.5), int(ALTURA / 1.5)))

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