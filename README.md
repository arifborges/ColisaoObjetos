# 📀 Colisão DVD: Evolução e Refatoração

## 🛠️ Evolução Técnica: O que foi melhorado?

A refatoração transformou um código procedural em uma estrutura escalável e eficiente. Abaixo estão os principais pontos de melhoria:

### 1. Paradigma

- **Código Original:** Utilizava variáveis soltas e lógica repetida. Para adicionar um novo texto, era necessário duplicar blocos inteiros de `if/else`.
- **Código Refatorado:** Centraliza tudo na classe `ColisaoDVD`. Cada objeto é uma instância independente que gerencia sua própria posição, cor e colisões, permitindo escalabilidade.

### 2. Física e Movimentação Estável

- **Código Original:** O uso de `random.randint(-1, 1)` para a velocidade permitia que o objeto recebesse valor `0`, resultando em textos "travados" ou que se moviam apenas em um eixo. O FPS em `512` causava consumo desnecessário de CPU.
- **Código Refatorado:** \* **Velocidade Garantida:** `random.choice([-base, base])` assegura que o objeto sempre tenha movimento diagonal constante.
  - **Performance:** Travado em `60 FPS`, garantindo suavidade visual e eficiência energética do hardware.
  - **Colisão Entre Objetos:** Implementação do método `checar_colisao_com`, permitindo que os textos interajam entre si e não apenas com as bordas.

### 3. Manutenibilidade

- **Código Original:** A lógica de renderização e troca de cor era repetida quatro vezes (uma para cada borda).
- **Código Refatorado:** Criado o método `mudar_cor()`. Qualquer alteração na estética do texto é feita em um único ponto, refletindo em todo o comportamento do objeto.

### 4. Observações

- **Tipagem:** Uso de _Type Hints_ (ex: `tela: pygame.Surface`) para facilitar o desenvolvimento e evitar erros de tipo.
- **Constantes:** Definição clara de `LARGURA`, `ALTURA` e `FPS`.
- **Entry Point:** Uso de `if __name__ == "__main__":` para garantir que o script seja executado de forma segura e organizada.
