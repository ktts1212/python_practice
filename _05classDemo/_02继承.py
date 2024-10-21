class Phone:
    brand_name = "huawei"

    def check_5g(self):
        print(f"当前手机品牌为{self.brand_name}")
        print("使用5g进行童话")


class Phone2024(Phone):
    brand_name = "xiaomi"

    def check_5g(self):
        print(f"当前手机品牌为{self.brand_name}")

    # 继承父类成员方法时，方法中还有父子类中同名的成员变量，则是子类中成员变量的值
    def last_brand(self):
        print(f"父类的品牌名为{super().brand_name}")
        super().check_5g()
        print("结束了")


# 多态
class AC:
    def cold_wind(self):
        pass

    def hot_wind(self):
        pass

    def swing_l_r(self):
        pass


class MediaAc(AC):
    def cold_wind(self):
        print("美的吹冷风")

    def hot_wind(self):
        print("美的吹热风")

    def swing_l_r(self):
        print("美的摇摆")


class GreeAc(AC):
    def cold_wind(self):
        print("格力吹冷风")

    def hot_wind(self):
        print("格力吹热风")

    def swing_l_r(self):
        print("格力摇摆")


def my_ac(ac: AC):
    ac.cold_wind()
    ac.hot_wind()
    ac.swing_l_r()


if __name__ == '__main__':
    mediaAc = MediaAc()
    greeAc = GreeAc()
    my_ac(mediaAc)
    print("___________")
    my_ac(greeAc)
