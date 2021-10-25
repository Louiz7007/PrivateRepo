gewicht = float(input("Gewicht in Kg: "))
groesse = float(input("Größe in m: "))
bmx = gewicht / (groesse ** 2)

print("Wenn Sie ", groesse*100, " cm groß sind und ", gewicht, "kg wiegen, dann", """
lautet ihr BMX: """, bmx, " (auf ganze Zahl gerundet ", round(bmx), ")")
