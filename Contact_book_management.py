import re
import csv

class ContactBook():
    def __init__(self):
        self.contacts = {} #dictionary to store contacts 
        self.next_id = 1 # To track the next available ids 


    def add_contact(self, name, company, phone, email, birthday, address, label, notes):
       
        ''' To add new conatact to the database along with validation'''
        if self.validate_email(email) and self.validate_phone(phone):
            contact_id = self.next_id
            self.contacts[contact_id] = {
                            'Name': name, 
                            'Company': company, 
                            'Phone' : phone, 
                            'Email' : email, 
                            'Birthday' : birthday, 
                            'Address' : address, 
                            'Label' : label, 
                            'Notes' : notes }
            self.next_id += 1
            print(f"Cotact added with ID : {contact_id}")
        else:
            print("Invalid contact details")

        
    def edit_contact(self, contact_id, **kwargs):
        '''To edit the existing contact's information.'''
        if contact_id in self.contacts:
            for key, value in kwargs.items():
                if key in self.contacts[contact_id]:
                    self.contacts[contact_id][key] = value
            print(f"Contact {contact_id} updated !")
            return True
        else:
            print(f"Contact {contact_id} not found for update.")
            return False
        
    def delete_contacts(self, contact_id):
        '''To delete a contact from the contact book'''
        if contact_id in self.contacts:
            del self.contacts[contact_id]
            print(f"Contact {contact_id} deleted")
            return True
        else:
            print(f"Contact  {contact_id} not found. ")
            return False
        
    
    def search_contact_by_name(self, name):
        '''To search contacts by name'''
        results = {id : contact for id, contact in self.contacts.items() if contact['Name'].lower() == name.lower()}
        return results
    
    def search_contact_by_label(self, label):
        '''To search contacts by label'''
        results = {id : contact for id, contact in self.contacts.items() if contact['Label'].lower() == label.lower()}
        return results                     

    @staticmethod
    def validate_email(email):
        '''To validate if the format of given email is correct'''
        return re.match(r'[^@]+@[^@]+\.[^@]+', email) is not None
    
    @staticmethod
    def validate_phone(phone):
        '''To validate the format of phone number.'''
        return re.match(r"^[0-9]{10}$", phone) is not None
    


# using class
# Example Usage
if __name__ == "__main__":

    manager = ContactBook()

    # Add a contact
    contact_id = manager.add_contact("Anurag", "Google", "7571876100", "singh2907anurag@gmail.com", 
                                     "29july199", "India", "Personal", "You are blessed!")

    # Edit a contact
    manager.edit_contact(contact_id, phone="1234567890", notes="Updated notes")

    # Search by name
    search_results = manager.search_contact_by_name("Anurag")
    print("Search Results:", search_results)
    