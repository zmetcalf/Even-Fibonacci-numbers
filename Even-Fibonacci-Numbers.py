sumEvenValues = 0
fibNumber = 0
val1 = 0
val2 = 1

while True:
    fibNumber = val1 + val2
    if fibNumber > 4000000:
        break;
    else:    
        if (fibNumber % 2) == 0:
            sumEvenValues = sumEvenValues + fibNumber
    val1 = val2
    val2 = fibNumber
    
print sumEvenValues
    
    
