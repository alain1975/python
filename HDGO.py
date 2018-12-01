"""
1. 商品列表
2. 把商品加入购物车
3. 列出购物车详情
4. 结账

"""

import collections

#商品列表
def list_goods(goods_dict):

    sorted_goods_dict = collections.OrderedDict(sorted(goods_dict.items(),key=lambda t:t[0]))
    print("----------------商品列表-----------------")
    print("商品编号     商品名称        商品价格")
    for key in sorted_goods_dict.keys():
        print(key,"       ", sorted_goods_dict[key]["name"],"      ",sorted_goods_dict[key]["price"])

#把商品加入购物车
def add_cart(name,price,amount,cart_list):
    subtotal_price = price * amount
    cart = [name,price,amount,subtotal_price]
    cart_list.append(cart)

#列出购物车详情
def list_cart(cart_list):
    print("-----------------欢迎您来到订单结算页面-----------")
    print("您当前的购物车商品信息为:")
    total_price = 0
    for i in range(len(cart_list)):
        print("商品名称：{}          商品单价：{}              数量：{}              商品总价：{}".format(cart_list[i][0],cart_list[i][1],cart_list[i][2],cart_list[i][3]))
        total_price = cart_list[i][3] + total_price
    print("订单总额：",total_price)
    return total_price

#结账
def payment(payment_amount):

    while True:
        amount =input("请您付款：")
        if amount.isdigit() == False or int(amount) < 0:
            amount = input("输入有误，请输入合法金额：")
        elif int(amount) < payment_amount:
           print("付款失败，输入金额小于订单总额！")
        else:
            print("付款成功，找您{}元".format(int(amount)-payment_amount))
            print("---------------------本次购物结束，期待您的下次光临---------------")
            break



def main():
    goods_dict = {

        "001": {"name": "爱马仕腰带", "price": 1999},

        "002": {"name": "劳力士男表", "price": 19999},

        "003": {"name": "巴宝莉眼镜", "price": 4999},

        "004": {"name": "路虎发现四", "price": 99999}
    }
    list_goods(goods_dict)
    cart_list = []
    key_input = input("请根据商品列表信息输入商品编号，退出购物请输入q：")
    while key_input != 'q':
        if key_input in goods_dict.keys():
            amount = input ("请输入您要购买的数量：")

            while amount.isdigit() == False or int(amount) < 0:
                amount = input("请输入您要购买的数量：")
            if int(amount) > 0:
                add_cart(goods_dict[key_input]['name'],goods_dict[key_input]['price'],int(amount),cart_list)
            list_goods(goods_dict)
            key_input = input("请根据商品列表信息输入商品编号，退出购物请输入q：")
        else:
            print("商品编号不存在，请重新输入！")
            list_goods(goods_dict)
            key_input = input("请根据商品列表信息输入商品编号，退出购物请输入q：")

    payment_amount = list_cart(cart_list)
    payment(payment_amount)

if __name__ == '__main__':
    main()

