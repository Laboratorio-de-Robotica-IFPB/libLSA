# libLSA - Biblioteca para utilizar o LightSensorArray no ev3dev

O objetivo desse projeto é conseguir controlar todas as funcionalidades presentes no sensor da mindsensors, de forma programática, utilizando o micropython e a plataforma do ev3dev

O suporte do sensor é bem completo quando utilizamos a plataforma base da lego, o LEGO EV3 Mindstorms, porém o software se tornou legado e não queremos mais depender da programação por blocos para utilizar o sensor em sua totalidade :) 

## Features:
- [x] Leitura dos valores calibrados (0 a 100, do preto até o branco)
- [x] Leitura dos valores de tensão puros
- [x] Escrita de comandos I2C arbitrários no sensor
- [x] Calibração do valor de referência do branco
- [x] Calibração do valor de referência do preto


## Como utilizar

1. Copie o arquivo _**mindstormsPYB.py**_ para a raiz do seu projeto.
2. Importe a biblioteca e instancie o sensor com a porta escolhida:
   ```python3
   from mindstormsPYB import LightArraySensor
   lsa = LightSensorArray(Port.S4)
   ```
3. Leia o exemplo disponível na pasta _samples_ para saber como utilizar os métodos de calibração


## Referências:
### Geral
- https://github.com/ev3dev/ev3dev
- https://pybricks.com/ev3-micropython/
- https://github.com/mindsensors/mindsensorsPYB/tree/main
- https://www.mindsensors.com/home/index.php?controller=attachment&id_attachment=101
### Hardware
- https://www.ev3dev.org/docs/kernel-hackers-notebook/
- https://www.ev3dev.org/docs/platform-comparison/
- https://docs.ev3dev.org/projects/lego-linux-drivers/en/ev3dev-jessie/i2c.html
- https://docs.ev3dev.org/projects/lego-linux-drivers/en/ev3dev-jessie/sensor_data.html#id167

### Software
- https://www.ev3dev.org/docs/programming-languages/
- https://github.com/ev3dev/brickman
- https://github.com/ev3dev/brickstrap
- https://github.com/ev3dev/ev3-kernel
- https://github.com/theZiz/ev3c/tree/master
- https://github.com/ldmberman/GoEV3
- https://github.com/ddemidov/ev3dev-lang-cpp
 - https://github.com/in4lio/ev3dev-c
### kernel e etc
- https://docs.ev3dev.org/projects/lego-linux-drivers/en/ev3dev-jessie/
- https://www.ev3dev.org/docs/devtools/
- https://github.com/ev3dev/lego-linux-drivers