import re
import pandas as pd
from bs4 import BeautifulSoup

# Read the HTML file from storage
with open("test_page.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, "html.parser")

# Initialize lists to store extracted data
names = []
addresses = []
states = []
pins = []
tels = []
emails = []

# Find all elements with class "subhead1" to extract names
name_elements = soup.find_all(class_="subhead1")
for name_element in name_elements:
    name = name_element.get_text(strip=True)
    names.append(name)

    # Find the parent table for each name and extract corresponding information
    parent_table = name_element.find_parent("table")
    address = parent_table.find(class_="hlink").get_text(strip=True)
    addresses.append(address)

    state_pin_tel_email = parent_table.find_all(class_="hlink")
    state = state_pin_tel_email[1].get_text(strip=True)
    pin = re.search(r'PIN\s*:\s*(\d+)', state_pin_tel_email[2].get_text()).group(1)
    tel = state_pin_tel_email[3].get_text(strip=True)
    email = state_pin_tel_email[4].find("a")["href"].split(":")[1].strip()
    
    states.append(state)
    pins.append(pin)
    tels.append(tel)
    emails.append(email)

# Ensure that all lists have the same length
min_length = min(len(names), len(addresses), len(states), len(pins), len(tels), len(emails))
names = names[:min_length]
addresses = addresses[:min_length]
states = states[:min_length]
pins = pins[:min_length]
tels = tels[:min_length]
emails = emails[:min_length]

# Create a DataFrame
data = {
    "Name": names,
    "Address": addresses,
    "State": states,
    "PIN": pins,
    "Tel": tels,
    "Email": emails
}

df = pd.DataFrame(data)

# Print the DataFrame
print(df)

df.to_csv('data_1.csv', index=False)
