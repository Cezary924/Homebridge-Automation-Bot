<div align="center">
   <h1>Homebridge Automation Bot</h1>
   <h3>🏠</h3>
   <h3>Create Homebridge accessory automation without HomeKit home hub</h3>
   <a href="https://github.com/Cezary924/Homebridge-Automation-Bot/blob/master/README.md" target="__blank"><img alt="A badge with a label 'Lang 🇬🇧' - a link takes to README file in English" src="https://img.shields.io/badge/Lang-🇬🇧-012169?style=for-the-badge"></a>
   <a href="https://github.com/Cezary924/Homebridge-Automation-Bot/blob/master/README.pl-pl.md" target="__blank"><img alt="A badge with a label 'Lang 🇵🇱' - a link takes to README file in Polish" src="https://img.shields.io/badge/Lang-🇵🇱-dc143c?style=for-the-badge"></a>
</div><br/>

## ✨ Automations
- Timer (to turn off the Homebridge accessory after a specified period of time)
- Scheduler (to turn on/off the Homebridge accessory depending on the time of the day)

## ⚙️ Installation
1. Clone this repo.
2. Install required libraries with this code:
```
pip install -r requirements.txt
```

## 🚀 Configuration & The First Start
1. To start, execute this command in the main directory:
```
python src/bot.py
```
2. During the first launch, the script created a *config.ini* file in a *config* directory. Please, edit the file with your data *(Homebridge IP, port, username & password)*.
3. If the information provided was correct, the script updated the file with Homebridge accessories data. Please, add to the file your automations.
4. Enjoy!