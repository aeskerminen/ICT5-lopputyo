def handle_input():
    args = []
    # Need dimensions, a_color, d_color and speed
    dimension_input = input('Anna ruudukon mitat (10-600, 10-600)\n').replace(' ', '')
    dimension_input = dimension_input.split(',')
    if len(dimension_input) < 2:
        print("Annoit vain yhden mitan ruudukkoon")
        exit(1)
    for dim in dimension_input:
        try:
            if not 10 <= int(dim) <= 600:
                print(f"Antamasi mitta '{dim}' ei ole alueen 10-600 sisällä")
                input("Paina jotain nappia aloittaaksesi ohjelman alusta.")
                return [], False
        except ValueError:
            print(f"Antamasi mitta '{dim}' ei ole numero")
            input("Paina jotain nappia aloittaaksesi ohjelman alusta.")
            return [], False
    args.append((int(dimension_input[0]), int(dimension_input[1])))
    print(args[0])

    a_color_input = input('Anna elossa olevan solun väri (0-255, 0-255, 0-255)\n').replace(' ', '')
    a_color_input = a_color_input.split(',')
    for x in a_color_input:
        try:
            if not 0 <= int(x) <= 255:
                print(f"Antamasi arvo '{x}' ei ole 0-255 sisällä")
                input("Paina jotain nappia aloittaaksesi ohjelman alusta.")
                return [], False
        except ValueError:
            print(f"Antamasi arvo '{x}' ei ole numero")
            input("Paina jotain nappia aloittaaksesi ohjelman alusta.")
            return [], False
    args.append((int(a_color_input[0]), int(a_color_input[1]), int(a_color_input[2])))

    d_color_input = input('Anna kuolleen solun väri, muodossa (0-255, 0-255, 0-255)\n').replace(' ', '')
    d_color_input = d_color_input.split(',')
    for x in d_color_input:
        try:
            if not 0 <= int(x) <= 255:
                print(f"Antamasi arvo '{x}' ei ole 0-255 sisällä")
                input("Paina jotain nappia aloittaaksesi ohjelman alusta.")
                return [], False
        except ValueError:
            print(f"Antamasi arvo '{x}' ei ole numero")
            input("Paina jotain nappia aloittaaksesi ohjelman alusta.")
            return [], False
    args.append((int(d_color_input[0]), int(d_color_input[1]), int(d_color_input[2])))

    speed_input = input('Anna uuden generaation laskemiselle nopeus (ms)\n').replace(' ', '')
    try:
        if not int(speed_input) >= 0:
            print(f"Antamasi nopeus '{speed_input}' on negatiivinen")
            input("Paina jotain nappia aloittaaksesi ohjelman alusta.")
            return [], False
    except ValueError:
        print(f'Anatamsi nopes {speed_input} ei ole numero')
        input("Paina jotain nappia aloittaaksesi ohjelman alusta.")
        return [], False
    args.append(int(speed_input))

    return args, True
