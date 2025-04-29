# Travian Bot Thingy

isto é util para auto evoluir recursos e auto atacar oasis e natares que quisermos

# Instalação

1. Ir ao cmd no windows
2. Ter python no windows. Se n tiverem façam download online para windows. Testar se esta instalado com  ``` python3 --version ``` ou sem o 3 idk.
3. Ter pip (normalmente vem com o python) no windows, checkar com ``` python3 -m pip --version``` ou ``` pip3 --version ``` ou uma variante qualquer que resulte para vcs com ou sem o 3 dps do pip ou do python n percebo nada destas instalações de python.
4. Instalar Selenium com ``` python3 -m pip install selenium ``` ou ``` pip install selenium ``` ou novamente a variante que resultou no ponto anterior
5. Instalar firefox 
6. No cmd correr ``` git clone https://github.com/mdgf1/travianBot.git ``` dps ``` python3 bot.py ```
7. Deve ser isso, se n correr pode ser porque há um problema qualquer com o selenium e o firefox os proximos passos é só se tiverem esse problema
8. Têm que fazer download de uma cena chamada geckodriver, extrair o ficheiro para o windows do git que aparece primeiro no google e meter num sitio que saibam o caminho para tipo ``` C:\Users\username\Documents ``` coisa simples assim
9. Vão a edit system environment variables no windows (pesquisar isto na lupa do windows), environment variables, em system variables clicar no path, clicar em edit, new, adicionar ``` C:\Users\username\Documents\pastaDoGeckodriver ```
10. Correr o bot de novo se n der é chorar e ver o erro que deu idk maybe meter o geckodriver em vez do que esta na pasta travianBot mesmo

# Como Usar

Se abrirem a pasta que é descarregada ao fazer ``` git clone https://github.com/mdgf1/travianBot.git ``` vai haver um ficheiro de texto chamado config.ini, nesse ficheiro têm que mudar os valores das coisas todas para as vossas, os oasis sao os meus num raio de 11 por 11 e as credenciais tambem (acabei de perceber que fiz upload da minha passe para o git vou ter de mudar isso ops). O valor de windowless é 0 ou 1, se for 1 o bot corre no background e n abre nada, mas recomendo correr pelo menos umas vezes com window para ver se esta tudo a correr fixe.

Dps podem fazer essencialmente 4 comandos:

1. ``` crops 5 ``` vai procurar o primeiro campo de recurso de nivel mais baixo e evolui-lo, a ideia é dps meter crops de 1 a 4 que é pedra, madeira etc mas n me apetece meter agora.
2. ``` oasis ``` ataca todos os oasis da vossa lista, os que sao atacados com sucesso e n falham por falta de tropas vao para o fim da fila.
3. ``` natares ``` ataca todas as aldeias natares da vossa lista, same thing que os oasis, se tiverem oasis e natares ativos ao mesmo tempo a ordem é random a cada ciclo (ele tenta fazer o ciclo todo de accoes a cada 2-3 min)
4. ``` main ``` evolui o edificio principal quando ha recursos

---
---

English translated by ai:

# Installation

1. Open Command Prompt (CMD) on Windows
2. Install Python on Windows. If you don't have it, download it from [python.org](https://www.python.org/downloads/windows/). Test installation with ```python3 --version``` or ```python --version``` (try with/without the "3" if unsure)
3. Ensure pip is installed (usually comes with Python). Check with:
   ```python3 -m pip --version``` 
   or 
   ```pip3 --version```
   (try different variations with/without "3" if needed)
4. Install Selenium using:
   ```python3 -m pip install selenium```
   or
   ```pip install selenium```
5. Install [Mozilla Firefox](https://www.mozilla.org/firefox/)
6. In CMD run:
   ```git clone https://github.com/mdgf1/travianBot.git```
   Then:
   ```python3 bot.py```
7. That should be it. If it doesn't run, you might need these additional steps for Firefox/Selenium issues

**Troubleshooting Firefox Driver (if needed):**
8. Download [geckodriver](https://github.com/mozilla/geckodriver/releases), extract the file to a simple location like:
   ```C:\Users\YourUsername\Documents\geckodriver```
9. Add to System Path:
   - Search for "Edit system environment variables" in Windows
   - Click "Environment Variables"
   - Under "System variables", select "Path" > "Edit"
   - Click "New" and add your geckodriver path:
     ```C:\Users\YourUsername\Documents\geckodriver```
10. Try running the bot again. If it still fails, check the error message and troubleshoot accordingly

# How to Use

After cloning the repository, edit the ```config.ini``` file:
- Replace all values with your account credentials 
- **Important:** The Oasis coordinates are currently set for an 11x11 radius around my base (I just realized I committed my password - need to fix that!)

Available commands:
1. ```crops 5```  
   Upgrades the first low-level crop field found. (Planned: levels 1-4 for stone/wood/etc, but not implemented yet)

2. ```oasis```  
   Attacks all Oases in your list. Successfully raided Oases get moved to the end of the queue.

3. ```natares```  
   Attacks all Natar villages in your list. Same queue management as Oases. If both Oasis and Natar commands are active, execution order is random per cycle.

4. ```main```  
   Upgrades your main building when resources are available.

**Note:** The bot attempts to complete all actions in a cycle every 2-3 minutes.
