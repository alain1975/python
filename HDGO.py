"""
1. 商品列表
2. 把商品加入购物车
3. 结账

"""

import collections

def list_goods(goods_dict):

    sorted_goods_dict = collections.OrderedDict(sorted(goods_dict.items(),key=lambda t:t[0]))
    print("----------------商品列表-----------------")
    print("商品编号     商品名称        商品价格")
    for key in sorted_goods_dict.keys():
        print(key,"       ", sorted_goods_dict[key]["name"],"      ",sorted_goods_dict[key]["price"])

def add_cart(key,amount):

    pass


def list_cart(cart_list)
    print("-----------------欢迎您来到订单结算页面-----------")
    print("您当前的购物车商品信息为:")
    print("商品名称：{}          商品单价：{}              数量：{}              商品总价：{}".format(name,unitprice,unit,totalprice))




def main():
    goods_dict = {

        "001": {"name": "爱马仕腰带", "price": 1999},

        "002": {"name": "劳力士男表", "price": 19999},

        "003": {"name": "巴宝莉眼镜", "price": 4999},

        "004": {"name": "路虎发现四", "price": 99999}
    }
    list_goods(goods_dict)
    key_input = input("请根据商品列表信息输入商品编号，退出购物请输入q：")
    while key_input != 'q':
        if key_input in goods_dict.keys():
            amount = input ("请输入您要购买的数量：")

            while amount.isdigit() == False or int(amount) < 0:
                amount = input("请输入您要购买的数量：")
            if int(amount) > 0:
                add_cart(key_input,int(amount))
            list_goods(goods_dict)
            key_input = input("请根据商品列表信息输入商品编号，退出购物请输入q：")
        else:
            print("商品编号不存在，请重新输入！")
            list_goods(goods_dict)
            key_input = input("请根据商品列表信息输入商品编号，退出购物请输入q：")

    list_cart()


if __name__ == '__main__':
    main()

