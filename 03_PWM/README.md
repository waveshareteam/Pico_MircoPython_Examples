# PWM
## 器件清单
器件 | 数量
---|---
Pico | 1

## 实现功能
使用PWM驱动LED（GPIO25）逐渐变亮，再逐渐熄灭。
## machine.PWM类
* machine.PWM(pin):
    * PWM对象构造函数
    * pin：需要设置为PWM输出的GPIO对象；
* PWM.deinit():
    * PWM反初始化
* PWM.freq([value]):
    * 设置PWM输出频率函数。
    * value: PWM输出频率，数值应符合PWM频率计算公式，过大或过小都会导致分辨率变小；
* PWM.duty_u16([value]):
    * 设定计数器比较值，
    * value: 设置占空比比例，数值应在0-65536间；
* PWM.duty_ns([value]):
    * 设定高电平的时间；
    * value: 设置高电平时间，单位为ns