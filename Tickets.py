#By Alan Baker 20230540 
#2023 Apr 4th

#this is a list of used_ids
used_ids = []

#this is a list of tickets
ticket_list = []

#0 is the default value of solve
solve = 0

#0 is the default value of resolved
resolved = 0

#0 is the default value of tickets_created
tickets_created = 0

#the Ticket() class contains the attributes and methods of the Ticket() object
class Ticket():
    
    #this method runs of first program startup
    def __init__(self, Num, Creator, ID, Email, Description, Response, Status):
        global solve
        global resolved
        global reopened
        global tickets_created
        
        #self.Num to self.Status defines the attributes of the Ticket Class
        self.Num = Num
        self.Creator = Creator
        self.ID = ID
        self.Email = Email
        self.Description = Description
        self.Response = Response
        self.Status = Status
        
        #if the Status is open increment solve by 1
        if self.Status == "Open":
            solve += 1
            
        #else if the Status is Closed, increment resolved by 1
        elif self.Status == "Closed":
            resolved += 1
            
        #increment tickets_created by 1
        tickets_created += 1
        
        #add the Ticket ID to the used ID's list
        used_ids.append(self.Num)
        
    #ticketprint() prints the information of the ticket picked in a clean and readble format
    def ticketprint(self):
        print("---------------")
        print("Ticket Number:", self.Num)
        print("Ticket Creator:", self.Creator)
        print("Staff ID:", self.ID)
        print("Staff Email:", self.Email)
        print("Description:", self.Description)
        print("Response:", self.Response)
        print("Status:", self.Status)
        
    #change_password() is a method that handles automatic password changing
    def change_password(self):
        global solve
        global resolved
        changedpwp1 = self.ID[0:2]
        changedpwp2 = self.Creator[0:3]
        changedpw = changedpwp2.join(changedpwp1)
        self.Response = "Password Updated to ", changedpw
        self.Status = "Closed"
        resolved += 1
        solve -= 1
        
        
#ticketstats() displays how many tickets are open or closed
def ticketstats():
    global solve
    global resolved
    print("---------------")
    print("Tickets Created:", tickets_created)
    print("Tickets Resolved:", resolved)
    print("Tickets to Solve:", solve)
        
        
#ticket1 is an example ticket
ticket1 = Ticket(2001, "Inna", "INNAM", "inna@whitecliffe.co.nz", "My monitor stopped working", "Not Yet Provided", "Open")
#ticket_list.append adds the ticket to the ticket list
ticket_list.append(ticket1)

#ticket2 is an example ticket
ticket2 = Ticket(2002, "Maria", "MARIAH", "maria@whitecliffe.co.nz", "Request for a videocamera to conduct webinars", "Not Yet Provided", "Open")
#ticket_list.append adds the ticket to the ticket list
ticket_list.append(ticket2)

#ticket3 is an example ticket
ticket3 = Ticket(2003, "John", "JOHNS", "john@whitecliffe.co.nz", "Password Change", "New password generated: JOJoh", "Closed")
#ticket_list.append adds the ticket to the ticket list
ticket_list.append(ticket3)


#make_ticket() is a function that allows the user to make custom tickets
def make_ticket():
    global used_ids
    global ticket_list
    userNum = used_ids[-1] + 1
    tid = userNum - 2001
    print("---------------")
    userCreator = input("Please input your name: ")
    userID = input("Please input your Staff ID: ")
    userEmail = input("Please input your Email: ")
    userDescription = input("Please add a Description: ")
    ticket4 = Ticket(userNum, userCreator, userID, userEmail, userDescription, "Not Yet Provided", "Open")
    ticket_list.append(ticket4)
    Ticket.ticketprint(ticket_list[tid])
    if "Password Change" in userDescription:
        Ticket.change_password(ticket_list[tid])
        print("Password Changed New Password in Response")
    else:
        pass
    main()

    
#view_tickets() allows the end-user to the data of a selected ticket 
def view_tickets():
    global used_ids
    global ticket_list
    print("---------------")
    sel_ticket = int(input("Which Ticket would you like to view: "))
    tid = sel_ticket - 2001
    if sel_ticket in used_ids:
        Ticket.ticketprint(ticket_list[tid])
    main()

    
#edit_tickets() allows an admin to modify the status or response to a ticket
def edit_ticket():
    global used_ids
    global ticket_list
    global solve
    global resolved
    global tickets_created
    print("---------------")
	#sel_ticket asks the User for a ticket ID to edit
    sel_ticket = int(input("Which Ticket would you like to edit: "))
    if sel_ticket in used_ids:
        tid = sel_ticket - 2001
        Ticket.ticketprint(ticket_list[tid])
        edit_choice = input("Would you like to Re(O)pen, (C)lose, (R)espond or (D)elete a ticket: ")
        if edit_choice == "O":
            ticket_list[tid].Status = "Open"
            solve += 1
            resolved -= 1
        elif edit_choice == "C":
            ticket_list[tid].Status = "Closed"
            resolved += 1
            solve -= 1
        elif edit_choice == "R":
            userResponse = input("Please Enter a Response: ")
            ticket_list[tid].Response = userResponse
        elif edit_choice == "D":
            confirmation = input("Are you Sure (Y/N): ")
            if confirmation == "Y":
                if ticket_list[tid].Status == "Closed":
                    resolved -= 1
                elif ticket_list[tid].Status == "Open":
                    solve -= 1
                ticket_list.pop(tid)
                used_ids.pop(tid)
                print("Ticket Deleted")
                tickets_created -= 1
                main()
            elif confirmation == "N":
                print("No Changes have been made")
        Ticket.ticketprint(ticket_list[tid])
        main()
    else:
        print("No Ticket of that ID Exists")
        edit_ticket()
       
    
#main() the function at acts as the root of the program and it branches into other functions
def main():
	ticketstats()
	print("---------------")
	usertask = input("Would you Like to (M)ake a new ticket, (V)iew Tickets or (E)dit a Ticket: ")
	if usertask == "V":
		view_tickets()
	elif usertask == "M":
		make_ticket()
	elif usertask == "E":
		edit_ticket()
	else:
		main()
            
            
#main() here initalises the program
main()
