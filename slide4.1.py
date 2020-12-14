
def km_to_m(value_dlina):
    return (value_dlina * 1000)
def mm_to_m(value_dlina):
    return (value_dlina / 1000)
def miles_to_m(value_dlina):
    return (value_dlina * 1609)
def m_to_km(value_dlina):
    return (value_dlina / 1000)
def m_to_mm(value_dlina):
    return (value_dlina * 1000)
def m_to_miles(value_dlina):
    return (value_dlina / 1609)


if __name__ == '__main__':
    convertation = int(input('Что считаем: \n 1. Из киллометров в метры\n 2. Из миллиметров в метры\n 3. Из миль в метры\n 4. Из метров в киллометры\n 5. Из метров в миллиметры\n 6. Из метров в мили\n 7. Из километров в мили\n'))
    if convertation==1:
        value_dlina = float(input('Сколько километров? :\n'))
        value_dlina_new = km_to_m(value_dlina)
    elif convertation==2:
        value_dlina = float(input('Сколько миллиметров? :\n'))
        value_dlina_new = mm_to_m(value_dlina)
    elif convertation==3:
        value_dlina = float(input('Сколько миль? :\n'))
        value_dlina_new = miles_to_m(value_dlina)
    elif convertation==4:
        value_dlina = float(input('Сколько метров? :\n'))
        value_dlina_new = m_to_km(value_dlina)
    elif convertation==5:
        value_dlina = float(input('Сколько метров? :\n'))
        value_dlina_new = m_to_mm(value_dlina)
    elif convertation==6:
        value_dlina = float(input('Сколько метров? :\n'))
        value_dlina_new = m_to_miles(value_dlina)
    elif convertation==7:
        value_dlina = float(input('Сколько километров? :\n'))
        value_dlina_new = km_to_m(value_dlina)
        value_dlina_new = m_to_miles(value_dlina_new)
    else:
        print("Ошибка")
    print(value_dlina_new)