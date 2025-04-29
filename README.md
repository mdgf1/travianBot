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
10. Correr o bot de novo se n der é chorar e ver o erro que deu idk

# Como Usar

Se abrirem a pasta que é descarregada ao fazer ``` git clone https://github.com/mdgf1/travianBot.git ``` vai haver um ficheiro de texto chamado config.ini, nesse ficheiro têm que mudar os valores das coisas todas para as vossas, os oasis sao os meus num raio de 11 por 11 e as credenciais tambem (acabei de perceber que fiz upload da minha passe para o git vou ter de mudar isso ops).

Dps podem fazer essencialmente 4 comandos:

1. ``` crops 5 ``` vai procurar o primeiro campo de recurso de nivel mais baixo e evolui-lo, a ideia é dps meter crops de 1 a 4 que é pedra, madeira etc mas n me apetece meter agora.
2. ``` oasis ``` ataca todos os oasis da vossa lista, os que sao atacados com sucesso e n falham por falta de tropas vao para o fim da fila.
3. ``` natares ``` ataca todas as aldeias natares da vossa lista, same thing que os oasis, se tiverem oasis e natares ativos ao mesmo tempo a ordem é random a cada ciclo (ele tenta fazer o ciclo todo de accoes a cada 2-3 min)
4. ``` main ``` evolui o edificio principal quando ha recursos

----

