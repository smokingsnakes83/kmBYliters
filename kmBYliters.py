"""KmBYliters"""

km_full_tank = float(input("Km com o tanque cheio: "))
km_partial_tank = float(input("Km com o tanque usado: "))
liters = float(input("Quantidade de litros usados para encher o tanque: "))

km_l = (km_partial_tank- km_full_tank) / liters

print()
print(f"Consumo de {km_l:.1f}km/l")
print()
    
op = input("Calcular quantidade de litros usados em uma viagem, s[sim], n[não] ")

if op == 's':
    km_BY_liters = float(input("Digite o km/l: "))
    travel_time = float(input("Digite o tempo de viagem(h): "))
    mean_speed = int(input("Digite a velocidade média: "))

    distance = travel_time * mean_speed
    used_liters = distance / km_BY_liters

    print()
    print(f"Velocidade media: {mean_speed}Km")
    print(f"Tempo de viagem: {travel_time}H")
    print(f"distância percorrida: {distance}Km")  
    print(f"Quantidade de litros usados na viagem: {used_liters:.1f}L")
    print()
     