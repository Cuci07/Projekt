from cryptography.fernet import Fernet
import json
import requests
from bs4 import BeautifulSoup

# Funksioni për të krijuar një çelës të ri dhe për të ruajtur atë në një skedar
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Çelësi u krijua dhe u ruajt në 'secret.key'.")

# Funksioni për të lexuar çelësin nga skedari
def load_key():
    return open("secret.key", "rb").read()

# Funksioni për të enkriptuar të dhënat
def encrypt_data(data):
    key = load_key()
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data.encode())
    return encrypted_data

# Funksioni për të dekriptuar të dhënat
def decrypt_data(encrypted_data):
    key = load_key()
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data).decode()
    return decrypted_data

# Funksioni për të marrë citate nga scraping
def fetch_quotes():
    url = 'http://quotes.toscrape.com/'

    # Dërgo një kërkesë HTTP për faqen
    response = requests.get(url)

    if response.status_code == 200:
        # Përdor BeautifulSoup për të analizuar HTML-në
        soup = BeautifulSoup(response.text, 'html.parser')

        # Gjej citatet dhe autorët
        quotes = []
        quote_elements = soup.find_all('div', class_='quote')

        for element in quote_elements:
            text = element.find('span', class_='text').text
            author = element.find('small', class_='author').text
            quotes.append({
                'quote': text,
                'author': author
            })

        # Ruaj citatet në një skedar JSON
        with open('quotes.json', 'w', encoding='utf-8') as f:
            json.dump(quotes, f, indent=4, ensure_ascii=False)

        print(f"{len(quotes)} citate u ruajtën me sukses në 'quotes.json'.")
        return quotes
    else:
        print(f"Gabim gjatë kërkesës. Statusi: {response.status_code}")
        return None

# Funksioni për të marrë të dhëna nga API
def fetch_api_data():
    # API publike JSONPlaceholder për marrjen e të dhënave
    api_url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        # Ruaj të dhënat e marrë nga API në një skedar JSON
        with open('api_data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"{len(data)} shkrime u ruajtën nga API në 'api_data.json'.")
        return data
    else:
        print(f"Gabim gjatë kërkesës së API. Statusi: {response.status_code}")
        return None

# Funksioni për të kombinuar të dhënat nga scraping dhe API
def combine_data():
    quotes = fetch_quotes()
    api_data = fetch_api_data()

    if quotes and api_data:
        # Kombinoni të dhënat nga scraping dhe API
        combined_data = {
            'quotes': quotes,
            'api_data': api_data
        }

        # Ruaj të dhënat e kombinuara në një skedar JSON
        with open('combined_data.json', 'w', encoding='utf-8') as f:
            json.dump(combined_data, f, indent=4, ensure_ascii=False)

        print(f"Të dhënat u kombinuan dhe u ruajtën në 'combined_data.json'.")

# Funksioni për enkriptimin e të dhënave nga skedari JSON
def encrypt_combined_data():
    # Lexoni të dhënat nga skedari combined_data.json
    with open('combined_data.json', 'r', encoding='utf-8') as f:
        data = f.read()

    # Enkriptuam të dhënat
    encrypted_data = encrypt_data(data)

    # Ruaj të dhënat e enkriptuara në një skedar
    with open('encrypted_combined_data.json', 'wb') as f:
        f.write(encrypted_data)

    print("Të dhënat u enkriptuan dhe u ruajtën në 'encrypted_combined_data.json'.")

# Funksioni për dekriptimin e të dhënave
def decrypt_and_read():
    # Lexoni të dhënat e enkriptuara nga skedari
    with open('encrypted_combined_data.json', 'rb') as f:
        encrypted_data = f.read()

    # Dekriptojmë të dhënat dhe i shfaqim
    decrypted_data = decrypt_data(encrypted_data)
    print("Të dhënat e dekriptuara:")
    print(decrypted_data)

if __name__ == "__main__":
    # Krijoni çelësin nëse nuk është krijuar ende
    generate_key()

    # Kombinoni të dhënat nga scraping dhe API
    combine_data()

    # Enkripto dhe ruaj të dhënat e kombinuara
    encrypt_combined_data()

    # Dekripto dhe shiko të dhënat
    decrypt_and_read()
