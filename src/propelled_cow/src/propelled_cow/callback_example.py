def cbf(gpio, level, tick):
   print(gpio, level, tick)

cb1 = pi.callback(16, pigpio.EITHER_EDGE, cbf)
