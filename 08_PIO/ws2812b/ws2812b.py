import time
from machine import Pin
import rp2

max_lum =100
r=0
g=0
b=0

@rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)
def ws2812():
    T1 = 2
    T2 = 5
    T3 = 3
    wrap_target()
    label("bitloop")
    out(x, 1)               .side(0)    [T3 - 1] 
    jmp(not_x, "do_zero")   .side(1)    [T1 - 1]
    jmp("bitloop")          .side(1)    [T2 - 1]
    label("do_zero")
    nop()                   .side(0)    [T2 - 1]
    wrap()


# Create the StateMachine with the ws2812 program, outputting on Pin(4).
sm = rp2.StateMachine(0, ws2812, freq=8_000_000, sideset_base=Pin(4))

# Start the StateMachine, it will wait for data on its FIFO.
sm.active(1)

# Color change
while True:
    for i in range(0,max_lum):
        r=i
        b=max_lum-i
        rgb =(g<<24) | (r<<16) | (b<<8)
        sm.put(rgb)
        time.sleep_ms(10)
    time.sleep_ms(300)
    for i in range(0,max_lum):
        g=i
        r=max_lum-i
        rgb =(g<<24) | (r<<16) | (b<<8)
        sm.put(rgb)
        time.sleep_ms(10)
    time.sleep_ms(300)
    for i in range(0,max_lum):
        b=i
        g=max_lum-i
        rgb =(g<<24) | (r<<16) | (b<<8)
        sm.put(rgb)
        time.sleep_ms(10)
    time.sleep_ms(300)