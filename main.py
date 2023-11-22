from xml_file_processor import FileProcessor
import xml.etree.ElementTree as ET

def main():
    print("1. Read XML file | 2. Add record to file | 3. Delete record from file | 4. Update record | 5. Display records | 6. Exit")
    f = FileProcessor
    filename = "data.xml"
    choice = input("Input what do you want to do:\n")
    
    while True:
        if int(choice) == 1:
            f.read_file(filename)
        elif int(choice) == 2:
            new_record = input("Enter new record:\n")
            f.add_record(filename, new_record)
        elif int(choice) == 3:
            id = input("Enter record id to delete\n")
            f.delete_record(filename, id)
        elif int(choice) == 4:
            id = input("Enter record id to update\n")
            new_record = input("Enter new record:\n")
            f.update_record(filename, id, new_record)
        elif int(choice) == 5:
            f.display_records(filename)
        elif int(choice) == 6:
            break
        else:
            print("Invalid choice")

main()