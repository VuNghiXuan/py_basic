print("------------Đây là chương trình tính giá trị món hàng")
customer_name = input('Nhập tên khách hàng: ')
goods = input('Tên sản phẩm: ')
quantity = float(input('Số lượng: '))
price = int(input('Giá: '))


total = quantity * price

print('----------------Thông tin sản phảm và giá trị-------------')
print("Tên khách hàng là:", customer_name)
print('Món hàng: ', goods)
print('Số lượng: ',quantity)
print('Đơn giá: ',price)

print('Thành tiền',int(total))