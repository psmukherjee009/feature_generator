import feat
# Raw data
# Date,Open,High,Low,Close,Adj Close,Volume
Date = INPUT[0]
S_Open = INPUT[1]
S_High = INPUT[2]
S_Low = INPUT[3]
S_Close = INPUT[4]
S_AdjClose = INPUT[5]
S_Volume = INPUT[6]

Open = float(S_Open)
Close = float(S_Close)
High = float(S_High)
Low = float(S_Low)

Atr = feat.atr(High, Low, Close)
Volume = int(S_Volume)
PivotPoint = (High + Close + Low)/3
PivotPointS1 = (PivotPoint * 2) - High
PivotPointS2 = PivotPoint - High + Low
PivotPointR1 = (PivotPoint * 2) - Low
PivotPointR2 = PivotPoint + High - Low

def computed_features():
    return ",".join([str(Date),str(S_Open),str(S_High),str(S_Low),str(S_Close),str(S_AdjClose),str(S_Volume),str(Open),str(Close),str(High),str(Low),str(Atr),str(Volume),str(PivotPoint),str(PivotPointS1),str(PivotPointS2),str(PivotPointR1),str(PivotPointR2)])
