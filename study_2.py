money = 20000
items = {'apel': 1250, 'pisang': 2000, 'jeruk': 1000}
for item_name in items:
    print('--------------------------------------------------')
    print('Anda memiliki Rp.' + str(money) + ' di dompet Anda')
    print('Harga setiap ' + item_name + ' Rp.' + str(items[item_name]))

    input_count = input('Mau berapa ' + item_name + '? ')
    print('Anda akan membeli ' + input_count + ' ' + item_name)

    count = int(input_count)
    total_price = items[item_name] * count
    print('Harga total adalah Rp.' + str(total_price))

    if money >= total_price:
        print('Anda telah membeli ' + input_count + ' ' + item_name)
        money -= total_price
        
        if money == 0:
            print('--------------------------------------------------')
            print('Dompet Anda kosong')
            break
    
    else:
        print('Uang Anda tidak mencukupi')
        print('Anda tidak dapat membeli ' + item_name + ' sebanyak itu')

print('Uang Anda sisa Rp.' + str(money))
