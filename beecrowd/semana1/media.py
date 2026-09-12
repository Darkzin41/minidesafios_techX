A = float(input())
B = float(input())
if A < 0 or A > 10 or B < 0 or B > 10:
    print("Nota(s) invalidas")
else:
    media = (A * 3.5 + B * 7.5) / 11
    print(f"MEDIA = {media:.5f}")

