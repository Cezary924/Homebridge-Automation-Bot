<div align="center">
   <h1>Homebridge Automation Bot</h1>
   <h3>🏠</h3>
   <h3>Twórz automatyzacje akcesoriów Homebridge bez centrum akcesoriów HomeKit</h3>
   <a href="https://github.com/Cezary924/Homebridge-Automation-Bot/blob/master/README.md" target="__blank"><img alt="A Etykieta z napisem 'Jęz 🇬🇧' - link prowadzi do pliku README w języku angielskim" src="https://img.shields.io/badge/Jęz-🇬🇧-012169?style=for-the-badge"></a>
   <a href="https://github.com/Cezary924/Homebridge-Automation-Bot/blob/master/README.pl-pl.md" target="__blank"><img alt="A Etykieta z napisem 'Jęz 🇵🇱' - link prowadzi do pliku README w języku polskim" src="https://img.shields.io/badge/Jęz-🇵🇱-dc143c?style=for-the-badge"></a>
</div><br/>

## ✨ Automatyzacje
- Timer (wyłącz akcesorium Homebridge po danym okresie czasu (+ tylko w określonych godzinach)).
- Scheduler (włącz/wyłącz akcesorium Homebridge w zależności od pory dnia (+ wschód/zachód Słońca)).
- Auto-restart (restart instancji Homebridge w zależności od pory dnia czy dnia tygodnia).

## ⚙️ Instalacja
1. Sklonuj to repozytorium.
2. Zainstaluj wymagane biblioteki przy pomocy tego polecenia:
```
pip install -r requirements.txt
```

## 🚀 Konfiguracja & Pierwsze Uruchomienie
1. Aby uruchomić skrypt, wykonaj to polecenie będąc w głównym folderze:
```
python src/bot.py
```
2. Podczas pierwszego uruchomienia, skrypt stworzy plik *config.ini* w folderze *config*. Dokonaj edycji tego pliku umieszczając w nim swoje dane *(Homebridge IP, port, nazwa użytkownika i hasło)*.
3. Jeśli podane informacje były prawidłowe, skrypt zaktualizował plik o dane akcesoriów Homebridge. Dodaj teraz do pliku swoje automatyzacje.
4. Gotowe!