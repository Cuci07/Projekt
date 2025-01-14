# Projekt
# # Detyra Kursi - Web Scraping, Enkriptimi dhe Integrimi API

# Projekt Enkriptimi dhe Scraping

Ky projekt ka për qëllim të demonstrojë përdorimin e enkriptimit për të ruajtur të dhënat dhe gjithashtu përdor scraping për të marrë citate dhe të dhëna nga një API publike. Mjetet kryesore të përdorura në këtë projekt përfshijnë:

- **BeautifulSoup** për scraping-n e të dhënave nga një faqe web.
- **Cryptography** për enkriptimin dhe dekriptimin e të dhënave.
- **JSON** për ruajtjen dhe manipulimin e të dhënave në formatin JSON.

## Përshkrimi i Funksioneve

### 1. **`generate_key()`**
Ky funksion krijon një çelës të enkriptimit dhe e ruan atë në një skedar të quajtur `secret.key`. Ky çelës përdoret për enkriptimin dhe dekriptimin e të dhënave.

### 2. **`load_key()`**
Ky funksion lexon çelësin e enkriptimit nga skedari `secret.key`, që është krijuar më parë.

### 3. **`encrypt_data(data)`**
Ky funksion merr të dhëna në formë teksti dhe i enkripton ato duke përdorur çelësin e ruajtur. Kjo i mundëson ruajtjen e të dhënave në një format të sigurt.

### 4. **`decrypt_data(encrypted_data)`**
Ky funksion merr të dhëna të enkriptuara dhe i dekripton ato për t’i bërë të lexueshme. Përdoret për të kthyer të dhënat në formatin origjinal pas enkriptimit.

### 5. **`fetch_quotes()`**
Ky funksion përdor **requests** dhe **BeautifulSoup** për të marrë citate nga një faqe e njohur scraping (http://quotes.toscrape.com/). Citatet dhe autorët ruhen në një skedar `quotes.json`.

### 6. **`fetch_api_data()`**
Ky funksion merr të dhëna nga një API publike (JSONPlaceholder) që ofron shkrime dhe informacion tjetër. Të dhënat ruhen në një skedar `api_data.json`.

### 7. **`combine_data()`**
Ky funksion kombinon të dhënat e marrë nga scraping dhe nga API. Të dyja grupet e të dhënave ruhen në një skedar të quajtur `combined_data.json`.

### 8. **`encrypt_combined_data()`**
Ky funksion enkripton të dhënat e kombinuara dhe i ruan ato në një skedar të enkriptuar të quajtur `encrypted_combined_data.json`.

### 9. **`decrypt_and_read()`**
Ky funksion lexon të dhënat e enkriptuara nga `encrypted_combined_data.json`, i dekripton ato dhe i shfaq në konsolë.

## Udhëzime për Përdorim

1. **Krijo Çelësin:**
   Përdorni funksionin `generate_key()` për të krijuar çelësin dhe për ta ruajtur atë në skedarin `secret.key`.

2. **Merrni të Dhënat nga Scraping dhe API:**
   Përdorni funksionet `fetch_quotes()` dhe `fetch_api_data()` për të marrë të dhëna nga faqet e internetit dhe API-ja.

3. **Kombinoni dhe Enkripto Të Dhënat:**
   Përdorni `combine_data()` për të kombinuar të dhënat dhe `encrypt_combined_data()` për t’i enkriptuar ato.

4. **Dekripto dhe Lexo Të Dhënat:**
   Funksioni `decrypt_and_read()` do të lexojë të dhënat e enkriptuara dhe do t’i dekriptojë ato për t’i shfaqur në konsolë.

## Teknologjitë dhe Libraritë e Përdorura

- **Python 3.x** - Gjuhë programimi e përdorur.
- **Requests** - Përdoret për të dërguar kërkesa HTTP për të marrë të dhëna nga interneti.
- **BeautifulSoup** - Përdoret për scraping HTML për të nxjerrë informacione nga faqet e internetit.
- **Cryptography** - Përdoret për enkriptimin dhe dekriptimin e të dhënave për mbrojtje të informacionit.

## Instalimi i Varësive

Për të përdorur këtë projekt, duhet të instaloni varësitë e nevojshme. Mund t’i instaloni ato duke përdorur **pip**:

```bash
pip install cryptography requests beautifulsoup4


   
