"""
    作者：wcz
    功能：BMR计算
    版本：v2.0
    日期：24/06/2018
"""


def main():
    """
        主函数
    """
    y_or_n = input('是否退出程序(y/n)?')
    while y_or_n != 'y':
        gender = input('性别：')
        weight = float(input('体重(kg)：'))
        height = float(input('身高(cm)：'))
        age = int(input('年龄：'))

        if gender == '男':
            bmr = 13.7 * weight + 5.0 * height - 6.8 * age + 66
        elif gender == '女':
            bmr = 9.6 * weight + 1.8 * height - 4.7 * age + 655
        else:
            bmr = -1

        if bmr != -1:
            print('基础代谢率(大卡)：', bmr)
        else:
            print('不支持该性别')

        print()
        y_or_n = input('是否退出程序(y/n)?')

if __name__ == '__main__':
    main()