# единая функция для всех заданий можно и символы менять и толщину
def pic(w, h, f, c):
    for i in range(h):
        if i in range(f) or i in range(h - f, h):
            print(c * w)
        else:
            print((c * f) + (" " * (w - f - f)) + (c * f))
    print()


if __name__ == '__main__':
    pic(7, 6, 2, '*')