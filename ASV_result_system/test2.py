all_accounts = [('ПАО «Невский банк»', '40702810953000000412'), ('АО «Кемсоцинбанк»', '60312810700000000022'), ('АО «Кемсоцинбанк»', '60324810600000000563')]
bank_accounts = {}
for i in all_accounts:
    if bank_accounts.get(i[0], None) == None:
        bank_accounts[i[0]] = str(i[1])
    else:
        bank_accounts[i[0]] = str(bank_accounts.get(i[0])) + ', ' + str(i[1])
print(bank_accounts)