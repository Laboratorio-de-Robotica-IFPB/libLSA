# ev3dev-lightarraysensor

O Objetivo desse projeto é conseguir controlar todas as funcionalidades presentes no sensor da mindsensors, de forma programática, utilizando o micropython e a plataforma do ev3dev

O suporte do sensor é bem completo quando utilizamos a plataforma base da lego, o Mindstorms, porém o software se tornou legado e não queremos mais depender da programação por blocos para utilizar o sensor com poder total :) 

## Etapas:
- [x] Identificação do sensor pelo sistema do ev3dev
- [x] Comunicação com o sensor de forma programada, utilizando o micropython
- [x] Leitura dos valores não calibrados (raw)
- [x] Leitura das informações do sensor
- [ ] Escrita de comandos I2C arbitrários no sensor
- [ ] Calibração do valor Branco
- [ ] Calibração do valor Preto
- [ ] Leitura de valores calibrados
- [ ] Estudar os registros I2C disponíveis e suas funcionalidades
- [ ] (Opcional) customizar/refatorar a biblioteca do mindsensors

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