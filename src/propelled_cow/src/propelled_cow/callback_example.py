def cbf(gpio, level, tick):
   print(gpio, level, tick)

cb1 = pi.callback(18, pigpio.EITHER_EDGE, cbf)
