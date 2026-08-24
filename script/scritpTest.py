import requests

URL = 'https://wttr.in/Cachoeiro%20de%20Itapemirim?format=j1&lang=pt'

def desc_lang_pt(entry):
    # Tenta pegar descrição em PT; se não houver, usa a descrição padrão
    if 'lang_pt' in entry and entry['lang_pt']:
        return entry['lang_pt'][0].get('value') or entry['weatherDesc'][0]['value']
    return entry['weatherDesc'][0]['value']
    return entry['weatherDesc'][0]['value']

def main():
    resp = requests.get(URL, timeout=10)
    resp.raise_for_status()
    data = resp.json()

    cc = data['current_condition'][0]
    agora = f"{cc['temp_C']}°C, {desc_lang_pt(cc)}"

    hoje = data['weather'][0]
    max_c = hoje['maxtempC']
    min_c = hoje['mintempC']

    print("Cachoeiro de Itapemirim - ES")
    print(f"Agora: {agora}")
    print(f"Máx/Mín de hoje: {agora}")
    print(f"Máx/Mín de hoje: {max_c}°C/{min_c}°C")

if __name__ == "__main__":
    main()