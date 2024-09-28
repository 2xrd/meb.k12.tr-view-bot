import requests
import time

# Kırmızı metin için ANSI kodu
RED = "\033[91m"
RESET = "\033[0m"

def refresh_website(url, interval):
    """Belirtilen URL'yi belirli aralıklarla refresh eder."""
    while True:
        try:
            response = requests.get(url)
            print(f"{RED}Refreshed {url} - Status Code: {response.status_code}{RESET}")
        except Exception as e:
            print(f"{RED}Error accessing {url}: {e}{RESET}")

        # Kullanıcının belirlediği saniye aralığına göre bekle
        time.sleep(interval)

# Kullanıcıdan URL ve refresh aralığı bilgilerini al
try:
    url = input(f"{RED}Please enter the meb.k12.tr URL to refresh (e.g., https://dundarucarmtandl.meb.k12.tr/icerikler/hazirbulunusluk-uygulamasi-takvimi_15414490.html): {RESET}")
    interval = float(input("Enter refresh interval (in seconds): "))
    if interval <= 0:
        print("Refresh interval must be a positive number.")
    else:
        # Fonksiyonu kullanıcıdan alınan URL ve aralık ile çalıştır
        refresh_website(url, interval)
except ValueError:
    print("Please enter valid numbers.")