due = 50
while True:
    print(f"Amount due: {due}")
    coin = int(input("Insert Coin: ").strip())
    if coin not in [5, 10, 25]:
        continue
    due -= coin
    if due <= 0:
        print(f"Change owed: {-due}")
        break
