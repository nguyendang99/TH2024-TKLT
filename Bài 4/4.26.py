print("DANG NGUYEN DANG")
print("MSSV: 235752021610010")
print("#############################")
######################################
def calculate_balance(transactions):
    balance = 0  
    for transaction in transactions:
        action, amount = transaction.split()  
        amount = int(amount)  
        if action == 'D': 
            balance += amount
        elif action == 'W':  
            balance -= amount
    return balance
transactions = []
print("Nhập nhật ký giao dịch (gõ 'x' để dừng):")
while True:
    entry = input()
    if entry.lower() == 'x':  
        break
    transactions.append(entry)
final_balance = calculate_balance(transactions)
print("Số tiền thực của tài khoản là:", final_balance)
