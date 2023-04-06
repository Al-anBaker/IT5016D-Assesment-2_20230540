#By Alan Baker 20230540 
#2023 Apr 6th

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
	#print("---------------") is used as a seperator
        print("---------------")
	#print statements here print the ticket information
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
	#changedpwp1 takes the first two letters of the Staff Id
        changedpwp1 = self.ID[0:2]
	#changedpwp2 takes the first three letters of the Ticket Creator name
        changedpwp2 = self.Creator[0:3]
	#changedpw is a combination of changedpwp1 and changedpwp2 and makes the new auto generated password
        changedpw = changedpwp2.join(changedpwp1)
	#this changes the response to the new passwor
        self.Response = "Password Updated to ", changedpw'
	#this automaticly closes the ticket
        self.Status = "Closed"
        resolved += 1
        solve -= 1
        
        
#ticketstats() displays how many tickets are open or closed
def ticketstats():
    global solve
    global resolved
    print("---------------")
	#print here run through the ticket stats
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
	#userNum is made of the last used id and added 1 to it to make the new id
    userNum = used_ids[-1] + 1
	#tid is the indexed version so it can be called from a list
    tid = userNum - 2001
    print("---------------")
	#input()s here asks the user for details for the new ticket
    userCreator = input("Please input your name: ")
    userID = input("Please input your Staff ID: ")
    userEmail = input("Please input your Email: ")
    userDescription = input("Please add a Description: ")
	#ticket4 is a temporary ticket that contains al the user varibles and makes a new ticket instance
    ticket4 = Ticket(userNum, userCreator, userID, userEmail, userDescription, "Not Yet Provided", "Open")
	#ticket_list.append(ticket4) adds the new ticket to the list system
    ticket_list.append(ticket4)
	#Ticket.ticketprint prints the newly made ticket
    Ticket.ticketprint(ticket_list[tid])
	#if the description contains "Password Change" then
    if "Password Change" in userDescription:
		#Ticket.change_password is a method thats runs the auto change password 
        Ticket.change_password(ticket_list[tid])
		#print here notifies the user that the Password has changed
        print("Password Changed New Password in Response")
    else:
		#else then it just igones this if statment
        pass
	#Goes back to the main menu
    main()

    
#view_tickets() allows the end-user to the data of a selected ticket or if "All" is inputed will display Every Saved Ticket
def view_tickets():
    global used_ids
    global ticket_list
    x = 0
    print("---------------")
	#sel_ticket askes the user what ticket they would like to see
    sel_ticket = input("Which Ticket would you like to see or see (A)ll: ")
	#if the user inputs "A" then
    if sel_ticket == "A":
		#for every item in the used_ids list run
        for x in used_ids:
			#tid = x - 2001 gets the index number of the used ids 
            tid = x - 2001
			#prints the information from the tickets
            Ticket.ticketprint(ticket_list[tid])
	#else 
    else:
		#sel_ticket = int(sel_ticket) makes the sel_ticket a number
        sel_ticket = int(sel_ticket)
		#tid gets the list index varible
        tid = sel_ticket - 2001
		#if the selected ticket exists in the used_ids list then
        if sel_ticket in used_ids:
			#print the selected ticket
            Ticket.ticketprint(ticket_list[tid])
		#else
		else:
			#notify the user that the ticket does not exist
			print("Ticket Does not exist in the system")
			#go back to main menu
			main()
	#go back to main menu
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
	#if the selected ticket exists in the used_ids list then
    if sel_ticket in used_ids:
		#get the indexed number
        tid = sel_ticket - 2001
		#prints the selected ticket
        Ticket.ticketprint(ticket_list[tid])
		#asks the user how they would like to edit the ticket
        edit_choice = input("Would you like to Re(O)pen, (C)lose, (R)espond or (D)elete a ticket: ")
		#if the edit_choice is Reopen then
        if edit_choice == "O":
			#sets the selected tickets status to "Open"
            ticket_list[tid].Status = "Open"
			#increments the solve value
            solve += 1
			#decrements the resolved value
            resolved -= 1
		#else if the edit_choice is Close then
        elif edit_choice == "C":
			#sets the selected tickets status to "Closed"
            ticket_list[tid].Status = "Closed"
			#increments the resolved value
            resolved += 1
			#decrements the solve value
            solve -= 1
		#elif the edit_choice is Respond then
        elif edit_choice == "R":
			#ask the user for a new response
            userResponse = input("Please Enter a Response: ")
			#set the selected ticket to the userResponse
            ticket_list[tid].Response = userResponse
		#else if the edit_choice is Delete then
        elif edit_choice == "D":
			#asks the user if they are sure they want to delete the ticket
            confirmation = input("Are you Sure (Y/N): ")
			#if the user confirms that they want to delete the ticket then
            if confirmation == "Y":
				#if that tickets status was "Closed" then
                if ticket_list[tid].Status == "Closed":
					#decrement the resolved value
                    resolved -= 1
				#else if the tickets status was "Open" then
                elif ticket_list[tid].Status == "Open":
					#decrement the solve value
                    solve -= 1
				#delete the ticket from the ticket list
                ticket_list.pop(tid)
				#delete the ticket id from used_ids as its now avalable
                used_ids.pop(tid)
				#notifies the user that the ticket is deleted
                print("Ticket Deleted")
				#decrements the tickets_created value
                tickets_created -= 1
				#go back to main menu
                main()
			#else if the user has not confirmed their deletion then
            elif confirmation == "N":
				#notify the user that no changes have been made
                print("No Changes have been made")
		#print the newly edited ticket
        Ticket.ticketprint(ticket_list[tid])
		#go back to main menu
        main()
	#if the ticket does not exist in the used_ids then
    else:
		#notify the user that the ticket does not exist
        print("No Ticket of that ID Exists")
		#ask the user again
        edit_ticket()
       
    
#main() the function at acts as the root of the program and it branches into other functions
def main():
	#ticketstats() displays how many tickets exist and how many are opened or closed
	ticketstats()
	print("---------------")
	#ask the user if they would like to view tickets, make a new one or edit a ticket
	usertask = input("Would you Like to (M)ake a new ticket, (V)iew Tickets or (E)dit a Ticket: ")
	#if the user wants to view the tickets then
	if usertask == "V":
		#run the view_tickets() function
		view_tickets()
	#else if the user wants to make a new ticket then
	elif usertask == "M":
		#run the make_ticket() function
		make_ticket()
	#else if the user wants to edit an existing ticket then
	elif usertask == "E":
		#run the edit_ticket() function
		edit_ticket()
	#if the user did not input an option then 
	else:
		#reask the user
		main()
            
            
#main() here initalises the program
main()
