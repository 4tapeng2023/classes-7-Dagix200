import xml.etree.ElementTree as ET
import json

class FileProcessor:
    def  read_file(filename):
        try:
            tree = ET.parse(filename)
            root = tree.getroot()
        except FileNotFoundError:
            print(f"File {filename} does not exist.")
            return
        
        dane_dict = {}
        for dane in root.findall('dane'):
            id_danych = dane.get('id')
            tekst_danych = dane.text
            dane_dict[id_danych] = tekst_danych

        print("Data in JSON:")
        print(json.dumps(dane_dict, indent=2))
        
    def add_record(filename, record):
        try:
            tree = ET.parse(filename)
            root = tree.getroot()
        except ET.ParseError:
            root = ET.Element("root")
            tree = ET.ElementTree(root)
    
        existing_id = [int(dane.get('id')) for dane in root.findall('dane')]
        new_id = max(existing_id, default=0) + 1
    
        new_element = ET.SubElement(root, 'dane', {'id': str(new_id)})
        new_element.text = record
    
        tree.write(filename)
        
    def delete_record(filename, record_id):
        try:
            tree = ET.parse(filename)
            root = tree.getroot()
        except FileNotFoundError:
            print(f"File {filename} does not exist.")
            return
        
        usuniete = False
        for dane in root.findall('dane'):
            if dane.get('id') == str(record_id):
                root.remove(dane)
                usuniete = True
                break

        if usuniete:
            tree.write(filename)
            print(f"Data with ID {record_id} was deleted succesfully.")
        else:
            print(f"Not found data with ID {record_id}.")
        
    def update_record(filename, record_id, new_record):
        try:
            tree = ET.parse(filename)
            root = tree.getroot()
        except FileNotFoundError:
            print(f"File {filename} does not exist.")
            return

        updated = False
        for dane in root.findall('dane'):
            if dane.get('id') == str(record_id):
                dane.text = new_record
                updated = True
                break

        if updated:
            tree.write(filename)
            print(f"Data with ID {record_id} was updated.")
        else:
            print(f"Not found data with ID {record_id}.")
        
    def display_records(filename):
        try:
            tree = ET.parse(filename)
            root = tree.getroot()
        except FileNotFoundError:
            print(f"File {filename} does not exist.")
            return
        
        print("All data:")
        for data in root.findall('dane'):
            data_id = data.get('id')
            id_text = data.text
            print(f"ID: {data_id}, Data: {id_text}")