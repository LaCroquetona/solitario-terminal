# Solitario en terminal

Un solitario Klondike que se juega en la consola. Lo hice en 1º de Bachillerato, cuando solo sabía usar la terminal y listas, al descubrir que Python podía pintar los emojis de la baraja Unicode.

Hecho por **Javier Meneses Perez**.

## Descargar

En [Releases](../../releases) está `Solitario.exe` para Windows, que se abre sin instalar nada. Las cartas se ven mejor en Windows Terminal.

Si tienes Python 3, también puedes abrir `Solitario.bat` o lanzarlo así:

```
python solitario.py
```

## Controles

| Tecla | Qué hace |
|---|---|
| `w` / `s` | Mover el cursor entre columnas |
| `d` | Elegir columna de origen y luego la de destino (otra vez en la misma la suelta) |
| `a` | Mandar la carta de arriba a su fundación |
| `r` | Robar del mazo (si está vacío, el descarte vuelve al mazo) |
| `e` | Coger la carta del descarte para moverla con `d` o `a` |
| `q` | Salir |

Cada tecla se escribe y se confirma con Enter.

## Cómo funciona

- Cada carta es una lista `[palo, valor, símbolo, boca abajo]`.
- `PrepareGame` reparte en escalera: 1 carta en la primera columna y 7 en la última. Lo que sobra es el mazo.
- `PuedeIr` decide si una carta encaja: valor uno menos y color contrario, o un Rey en una columna vacía.
- `CheckCards` busca la carta boca arriba de la columna de origen que encaja en el destino, y se mueve con todo lo que tenga encima.
- Las fundaciones empiezan con una carta "0" de cada palo, así la siguiente que entra siempre es el valor anterior + 1.
- Se gana cuando las cuatro fundaciones llegan al Rey.
