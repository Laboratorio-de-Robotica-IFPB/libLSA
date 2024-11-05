## Dia Zero - 01/11
_escrito por: ramalho_

Começamos o desenvolvimento usando uma biblioteca da [própria mindsensors](https://github.com/mindsensors/mindsensorsPYB)

É um arquivo de python único, que trás uma api bem rudimentar e crua, mas faz o básico da comunicação entre o driver I2C do ev3dev com os diversos dispositivos que a própria mindsensors produz.

PS: é bom dar uma olhada no código do LineFollower e da NXTCam5 que estão ali no meio, esses são
outros 2 sensores que a gente tem no lab.

De início, o foco de hoje é apenas conseguir os dados brutos do sensor e conseguir estudar um pouco 
a api para saber como puxar informações mais avançadas do sensor (exemplo: calibração da cor preta e da cor branca, além do uso dos comandos).

Puxar os dados brutos foi a parte fácil, mas muitas funções da api simplemente não funcionavam :)

Então, para sanar as dúvidas sobre o funcionamento esperado do sensor, fui atrás do [manual oficial](manual-lsa.pdf). 

Esse é o guia **quase que definitivo desse sensor**, com ele dava pra descobrir cada registrador I2C usado e seu propósito, além de ter toda descrição dos comando aceitos pelo sensor.

Com ele deu até pra identificar a firmware, vendor ID e o device ID do sensor, só usando as funções
cruas do ev3dev e as infos do manual.

Por fim, tonni procurou saber uma forma de atualizar os pacotes do ev3dev, já que ele é baseado em debian, mas não deu certo. Mesmo alterando a fonte dos pacotes, o ev3 não atualiza de jeito nenhum.

Então ficaremos com um debian 9 até uma outra forma aparecer.


## Dia 1 - 05/11

_escrito por: ramalho_

Hoje o foco foi tentar corrigir a api, tentar mandar alguns dos comandos e ver o comportamento do sensor.

Baseado no que o manual indica, os comandos deve ser enviados ao registardor **''0x41''**

Todos os comandos são caracteres de 1 byte, e aparentemente funciona normalmente se optarmos por ele
no 'port view' do sensor. Mas um certo erro voltava a aparecer:

TODO, escrever sobre:
- o erro 'OSError: [Errno 5] EIO' e como evitar ele
- como ler os bytes puros a partir de um registrador I2C
- as diferenças entre o endereço "real" (para o ev3) e o endereço da fabricante - [ref](https://docs.ev3dev.org/projects/lego-linux-drivers/en/ev3dev-stretch/i2c.html#)
- planos sobre a refatoração da api e como devemos organizar ela.