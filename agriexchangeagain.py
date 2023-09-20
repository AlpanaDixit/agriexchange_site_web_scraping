import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv
import re

# pattern = r'([^,]+)\n(.+?)\n([\w\s]+)\nPIN\s*:\s*(\d+)\nTel\s*:\s*([\w\d]+)\nEmail\s*:\s*([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)'
pattern = r'([^,]+)\n(.+?)\n([\w\s]+)\nPIN\s*:\s*(\d+)\nTel\s*:\s*([\w\d]+)\nEmail\s*:\s*([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)'

# pattern = r'(?P<Name>.+)\nAddress:\s*(?P<Address>.+)\n(?P<State>[A-Za-z\s]+)\nPIN\s*:\s*(?P<PIN>\d*)\nTel\s*:\s*(?P<Tel>[A-Z\d]*)\nEmail\s*:(?P<Email>[^\n]*)'
name_list = []
address_list = []
state_list = []
pin_list = []
tel_list = []
email_list = []

url = "https://agriexchange.apeda.gov.in/product_profile/ExportersDirectory/exporters_list.aspx?head=0206"
r = requests.get(url)
# print(r)
table_string = ""

soup = BeautifulSoup(r.text, "lxml")

# table = soup.find("table", id= "datalist1")

# Find all tables with the specified structure
tables = soup.find_all('table', attrs={'width': '100%', 'border': '0', 'cellspacing': '0', 'cellpadding': '0'})
# print(tables)
for table in tables:

    names = table.find_all('td')
    for name in names:
        name_text = name.get_text(strip=True)
        # table_text = table.get_text(strip=True)
        cleaned_string = name_text.replace("\t", "")
        # print(cleaned_string)
    # cleaned_string = table_text.replace("\t", "")
        cleaned_string = cleaned_string + "\n"
    # print(cleaned_string)

        table_string = table_string + cleaned_string

# table_string = re.sub(r'^\s+', '', table_string, flags=re.MULTILINE)

# sections = re.split(r'\bName:\s+', table_string.strip())

# print(table_string)

# data_blocks = re.split(r'\n(?=\w+)', table_string.strip())

# Extract information from each block and store it in a list of dictionaries
# formatted_data = []
# for block in data_blocks:
    # match = re.search(pattern, block, re.DOTALL)
    # if match:
        # formatted_data.append(match.groupdict())

# Create a DataFrame from the formatted data
# df = pd.DataFrame(formatted_data)

# Save the data to a CSV file
# df.to_csv('formatted_data.csv', index=False)

# Display the formatted data
# print(df)




# matches = re.findall(pattern, table_string, re.DOTALL)
matches = re.findall(pattern, table_string, flags=re.MULTILINE | re.DOTALL)

# # columns = ["Name", "Address", "State", "Pincode", "Tel", "Email"]
# # df = pd.DataFrame(columns=columns)

for match in matches:
    name, address, state, pincode, tel, email = match
    # print(f"Name: {name.strip()}")
    # print(f"Address: {address.strip()}")
    # print(f"State: {state.strip()}")
    # print(f"PIN Code: {pincode.strip()}")
    # print(f"Tel: {tel.strip()}")
    # print(f"Email: {email.strip()}")
    # print()

    name = f"{name.strip()}"
    address = f"{address.strip()}"
    state = f"{state.strip()}"
    pincode = f"{pincode.strip()}"
    tel = f"{tel.strip()}"
    email = f"{email.strip()}"

    name_list.append(name)
    address_list.append(address)
    state_list.append(state)
    pin_list.append(pincode)
    tel_list.append(tel)
    email_list.append(email)

# print(len(name_list))
# print(len(address_list))
# print(len(state_list))
# print(len(pin_list))
# print(len(tel_list))
# print(len(email_list))

print(address_list)



# dataframe = pd.DataFrame({"Name":name_list, "Address":address_list, "State":state_list, "Pincode":pin_list, "Tel":tel_list, "Email":email_list})
# print(dataframe)    
# dataframe.to_csv("agri_exchange_1.csv")

    
    # data = {
    # 'Name': [name],
    # 'Address': [address],
    # 'State': [state],
    # 'Pincode': [pincode],
    # 'Telephone': [tel],
    # 'Email': [email]
    # }
    
# df = pd.DataFrame(data)

# Display the DataFrame
# print(df)

#     # df.loc[0] = [name, address, state, pincode, tel, email]

#     # print(name)
#     name_list.append(name)
#     # print(address)
#     address_list.append(address)
#     # print(state)
#     state_list.append(state)
#     # print(pincode)
#     pin_list.append(pincode)
#     # print(tel)
#     tel_list.append(tel)
#     # print(email)
#     email_list.append(email)
#     print()


# print(name_list)
# print(address_list)
# print(state_list)
# print(pin_list)
# print(tel_list)
# print(email_list)













































# for match in matches:
#     name, address, state, pin, tel, email = match
#     print("Name:", name)

#     # Split the text into sections based on the "Name:" field
#     sections = re.split(r'\bName:\s+', address.strip())

#     # Define a function to clean up lines
#     def clean_lines(lines):
#         return [line.strip() for line in lines if line.strip()]

#     # Process each section
#     for section in sections[1:]:
#         lines = section.split('\n')
#         address = clean_lines(lines)

#     # Print the extracted information (excluding empty PIN and Email fields)
#     if address:
#         print("Address:", address)
#         # if len(address) > 1:
#         #     print("Additional Address:", ", ".join(address[1:]))
#     if state:
#         print("State:", state)
#     if pin:
#         print("PIN:", pin)
#     if tel:
#         print("Tel:", tel)
#     if email:
#         print("Email:", email)

#     print()










    # print(f"Name: {name.strip()}")
    # print(f"Address: {address.strip()}")
    # print(f"State: {state.strip()}")
    # print(f"PIN Code: {pincode.strip()}")
    # print(f"Tel: {tel.strip()}")
    # print(f"Email: {email.strip()}")
    # print()
    # print("Name:", name)
    # print("Address:", address)

    # address_lines = [line.strip() for line in address.split('\n') if line.strip()]
    # if len(address_lines) > 0:
        # print("Address:", address_lines[0])
    # if len(address_lines) > 1:
        # print("Additional Address:", ", ".join(address_lines[1:]))

    # print("State:", state)
    # print("PIN:", pin)
    # print("Tel:", tel)
    # print("Email:", email)
    # print()

    # name = f"{name.strip()}"
    # address = f"{address.strip()}"
    # state = f"{state.strip()}"
    # pincode = f"{pincode.strip()}"
    # tel = f"{tel.strip()}"
    # email = f"{email.strip()}"

    # df.loc[0] = [name, address, state, pincode, tel, email]

    # print(name)
    # name_list.append(name)
    # print(address)
    # address_list.append(address)
    # print(state)
    # state_list.append(state)
    # print(pincode)
    # pin_list.append(pincode)
    # print(tel)
    # tel_list.append(tel)
    # print(email)
    # email_list.append(email)
    # print()
    
    # print(df)

    
# print(name_list)
# print(len(address_list))
# print(len(state_list))
# print(len(pin_list))
# print(len(tel_list))
# print(len(email_list))

# dataframe = pd.DataFrame({"Name":name_list, "Address":address_list, "State":state_list, "Pincode":pin_list, "Tel":tel_list, "Email":email_list})
# print(dataframe)    
# dataframe.to_csv("agri_exchange.csv")

    # print(tables)

# with open("output_table.txt", "w", encoding="utf-8") as file:
# #     # Iterate through the 'names' elements and extract text with strip=True
#     for table in tables:
#         file.write(tables)

# Process each table
# for table in tables:
#     # Extract data from each table based on the HTML structure
#     name = table.find('td', class_='subhead1').get_text(strip=True)
#     address = table.find('td', class_='hlink').get_text(strip=True)
#     state = table.find('td', class_='hlink').get_text(strip=True)
#     pin_code = table.find('td', class_='hlink', text='PIN :').next_sibling.strip()
#     telephone = table.find('td', class_='hlink', text='Tel :').next_sibling.strip()
#     email = table.find('td', class_='hlink').find('a').get('href').split(':')[1]

#     # Print or store the extracted data as needed
#     print(f"Name: {name}")
#     print(f"Address: {address}")
#     print(f"State: {state}")
#     print(f"PIN Code: {pin_code}")
#     print(f"Telephone: {telephone}")
#     print(f"Email: {email}")
#     print("-" * 20)  # Separation between tables

# td_elements = box.find_all('td', class_=["class1", "class2"])

# soup = BeautifulSoup(html, 'html.parser')
# td_elements = box.select('td.subhead1.hlink')

# print(td_elements)
# names = box.find_all("td")
# print(names)
# for name in names:
#     print(name.get_text(strip=True))
#     name_text =  name.get_text(strip=True)
#     print(name_text)

# Extract data based on the HTML structure
# name = soup.find('td', class_='subhead1').get_text(strip=True)
# address = soup.find('td', class_='hlink').get_text(strip=True)
# state = soup.find('td', class_='hlink').get_text(strip=True)
# pin_code = soup.find('td', class_='hlink', text='PIN :').next_sibling.strip()
# telephone = soup.find('td', class_='hlink', text='Tel :').next_sibling.strip()
# email = soup.find('td', class_='hlink').find('a').get('href').split(':')[1]

# Print the extracted data
# print(f"Name: {name}")
# print(f"Address: {address}")
# print(f"State: {state}")
# print(f"PIN Code: {pin_code}")
# print(f"Telephone: {telephone}")
# print(f"Email: {email}")