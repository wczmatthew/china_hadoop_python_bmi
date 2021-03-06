"""
    作者：wcz
    功能：BMR计算
    版本：v3.0
    日期：24/06/2018
    功能：
"""


def main():
    """
        主函数
    """
    y_or_n = input('是否退出程序(y/n)?')
    while y_or_n != 'y':
        print('请输入以下信息，用空格分割')
        input_str = input('性别 体重(kg) 身高(cm) 年龄：')
        str_list = input_str.split(' ')

        gender = str_list[0]
        weight = float(str_list[1])
        height = float(str_list[2])
        age = int(str_list[3])

        if gender == '男':
            bmr = 13.7 * weight + 5.0 * height - 6.8 * age + 66
        elif gender == '女':
            bmr = 9.6 * weight + 1.8 * height - 4.7 * age + 655
        else:
            bmr = -1

        if bmr != -1:
            print('性别：{}， 体重：{}， 身高：{}， 年龄：{}'.format(gender, weight, height, age))
            print('基础代谢率: {}大卡'.format(bmr))
        else:
            print('不支持该性别')

        print()
        y_or_n = input('是否退出程序(y/n)?')

if __name__ == '__main__':
    main()