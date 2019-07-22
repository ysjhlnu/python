#！/bin/usr/env python
# -*- coding:utf-8 -*-

# 将十进制的IP地址转换成二进制的IP地址，去掉其中的'.',再将二进制转换成十进制
ip = input('Please input an IP address:')
ip_list = ip.split('.')
result = []
for item in ip_list:
    new_ip =bin(int(item))
    v = new_ip.lstrip('0b')
    if len(v) < 8 :
        add = (8-len(v))
        v = add * '0' + v
        result.append(v)
    else:
        result.append(v)
new_result = ''.join(result)
dec_num = int(new_result,base=2)
print("Binary:%s"%(new_result))
print("Converted decimal:%s"%(dec_num))
