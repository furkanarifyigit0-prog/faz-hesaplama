# Faz hesaplama programı

print("⚡ Faz Hesaplama Programı ⚡")

# Kullanıcıdan değerleri al
R = float(input("Direnç (R) [Ohm]: "))
L = float(input("Endüktans (L) [H]: "))
C = float(input("Kapasitans (C) [F]: "))
f = float(input("Frekans (f) [Hz]: "))

# Açısal frekans
w = 2 * math.pi * f

# Reaktanslar
XL = w * L
XC = 1 / (w * C) if C != 0 else 0

# Toplam empedansın genliği
Z = math.sqrt(R**2 + (XL - XC)**2)

# Faz açısı (radyan ve derece)
phi_rad = math.atan((XL - XC) / R) if R != 0 else math.pi/2
phi_deg = math.degrees(phi_rad)

# Sonuçları yazdır
print("\n--- Sonuçlar ---")
print(f"Endüktif Reaktans (XL): {XL:.2f} Ω")
print(f"Kapasitif Reaktans (XC): {XC:.2f} Ω")
print(f"Toplam Empedans (Z): {Z:.2f} Ω")
print(f"Faz Açısı (φ): {phi_deg:.2f}°")

if phi_deg > 0:
    print("Devre endüktif, akım gerilimin GERİSİNDE.")
elif phi_deg < 0:
    print("Devre kapasitif, akım gerilimin İLERİSİNDE.")
else:
    print("Devre tam dirençli, akım ve gerilim aynı fazda.")
