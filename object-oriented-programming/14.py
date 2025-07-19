def  displayPerson( name="John", gender="male", age=20 ):
     if age <= 70:
          print( "Young:" if age<30 and gender=="male"or age<40 and gender=="female"
            else "Middle:" if age<60 else "Senior:", name, gender )
     else: print( "Aged:", name, gender )

print('displayPerson()', displayPerson())
print('displayPerson( "Amanda", "female" )', displayPerson( "Amanda", "female" ))
print('displayPerson( age=32, name="Ken" ) ', displayPerson( age=32, name="Ken" ) )
print('displayPerson( "Cassie", "female", 39 ) ', displayPerson( "Cassie", "female", 39 ) )
print('displayPerson( name="Sir. Smith", age=89 ) ', displayPerson( name="Sir. Smith", age=89 ) )
