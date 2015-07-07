from Data import *
#take an object of DESdata(KEY,TEXT)
object=DESdata("133457799BBCDFF1", "0123456789ABCDEF")
#TO DO TASKS performs are operations Must be in order
object.init_ip()
object.intit_R0andL0()
object.initkey()
object.ROunds()
#in this function returns data in bits
data=object.final_ip()
#in this function return Data In Hex Decimal
print(object.finato(data)) # Final Output
# after this if you would Like to display keys or R or  L
object.RofRounds  #displays R From R0 To R16
object.LofRounds  ##displays L From L0 To L16
object.Keysafterpermulation #Displays Keys
print(object.RofRounds)

