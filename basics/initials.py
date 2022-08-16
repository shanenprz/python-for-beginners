alpha = {}
alpha['S'] = " SS  S  S        S S       S S       S  S SSS   "
alpha['P'] = "BBBB   B   B  B   B  BBBB   B   B  B   B  BBBB   "

for i in range(7):
  print (alpha['S'][i*7:i*7+7], alpha['P'][i*7:i*7+7])