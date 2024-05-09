
import math

def main():
    x = float(input("Başlangıç parasını girin (TL): "))
    y = float(input("Günlük artış oranını girin (%): "))
    z = int(input("Kaçıncı günde paramı öğrenmek istediğinizi girin: "))

    # Artış oranını yüzde cinsinden alıp ondalık hale getiriyoruz
    y = y / 100

    # Paramızın z gün sonra ne kadar olacağını hesaplıyoruz
    param = x * math.pow(1 + y, z)

    print(f"{z}. günde paramız {param:.2f} TL olur.")

if __name__ == "__main__":
    main()