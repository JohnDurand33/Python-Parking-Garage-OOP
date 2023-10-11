class parkingGarage():
    def __init__(self, max_tix, max_spaces, parking_database = {}):
        self.tickets = []
        self.parkingSpaces = []
        self.parking_database = parking_database
        
        for x in range(max_tix):
            self.tickets.append(x + 1)
        
        for x in range(max_spaces):
            self.parkingSpaces.append(x + 1)
          
        self.ticket_num = None
        self.park_space = None

    def takeTicket(self):
        if not self.tickets:
            print("I'm sorry, we're out of parking spaces at the moment.")
        if self.tickets:
            self.ticket_num = self.tickets.pop(0)
            self.park_space = self.parkingSpaces.pop(0)
            self.parking_database[self.ticket_num] = {'paid':False, 'space':self.park_space} 
            print(f"Thank you.  Your ticket number is {str(self.ticket_num)} and your parking space number is {str(self.park_space)}.  Enjoy the event!")

    def payForParking(self):
        pay_flag = True
        while pay_flag == True:
            self.ticket_amt = input("To pay, please input the amount exactly as displayed on the screen (\"$10.00\"): ")
            if self.ticket_amt.strip() == '$10.00':
                print("Thank you very much.  You have 15 minutes remaining allowed inside the garage.")
                self.parking_database[self.ticket_num]['paid'] = True
                pay_flag = False
            else:
                print("I'm sorry, that amount is incorrect.")
            

    def leaveGarage(self, park_space, ticket_num) : 
        leave_flag = True
        while leave_flag == True:
            if self.parking_database[self.ticket_num]['paid'] == False:
                self.ticket_amt = input("Excuse me, You still need to pay before leaving.  Please input the amount displayed on the screen (\"$10.00\") or you will be\ntowed.")
                if self.ticket_amt == '$10.00':
                    self.parking_database[self.ticket_num]['paid'] = True
                    print("Thank you very much, and have a great day!")
                    leave_flag = False
            else:
                self.parking_database[self.ticket_num]['space'] = None
                self.tickets.append(self.ticket_num)
                self.parkingSpaces.append(self.park_space)
                print("Thank you very much, and have a great day!")
                leave_flag = False
            
my_garage = parkingGarage(100, 100)
my_garage.takeTicket()
my_garage.payForParking()
my_garage.leaveGarage(1, 1)




            




            


            
                

            


    



