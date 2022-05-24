fabrica = 30.000


if fabrica <= 12.000:
    distribuidor = fabrica * 0.05
    print(fabrica + distribuidor)
elif fabrica > 12.000 and fabrica <= 25.000:
    distribuidor = fabrica * 0.1
    imposto = fabrica * 0.15
    print(fabrica + distribuidor + imposto)
else:
    distribuidor = fabrica * 0.15
    imposto = fabrica * 0.2
    print(fabrica + distribuidor + imposto)


