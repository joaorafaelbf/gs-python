# gs-python

# 🚚 OrbitTrack – Rastreamento Logístico via IoT e Satélite

## 📌 Sobre o Projeto

O **OrbitTrack** é uma solução desenvolvida para a **Global Solution FIAP**, com o objetivo de simular um sistema de rastreamento logístico baseado em dispositivos IoT conectados a satélites de órbita baixa (LEO).

O projeto busca solucionar um problema comum em setores como transporte, agronegócio, mineração e construção civil: a dificuldade de monitorar veículos e cargas em regiões sem cobertura de telefonia móvel.

Por meio do uso de tecnologias inspiradas em comunicação satelital, o sistema permite acompanhar a localização de veículos, atualizar coordenadas, identificar possíveis desvios de rota e gerar relatórios de monitoramento.

---

## 🎯 Problema Abordado

Empresas que operam em áreas remotas frequentemente enfrentam dificuldades para rastrear seus veículos devido à ausência de sinal celular.

Essa limitação pode resultar em:

* Falta de visibilidade da frota;
* Atrasos na entrega de cargas;
* Dificuldade na tomada de decisões;
* Aumento dos riscos operacionais;
* Perdas financeiras.

---

## 💡 Solução Proposta

O OrbitTrack simula uma plataforma de rastreamento que utiliza dispositivos IoT para coletar informações de localização e transmiti-las via satélite.

O sistema permite:

* Monitoramento de veículos;
* Atualização de coordenadas;
* Consulta de localização;
* Geração de alertas;
* Emissão de relatórios;
* Análise estatística da frota.

---

## ⚙️ Tecnologias Utilizadas

* Python 3
* Terminal/Console
* Estruturas de Dados (Listas)
* Funções (`def`)
* Estruturas de Decisão (`if`, `elif`, `else`)
* Estruturas de Repetição (`for`, `while`)
* Tratamento de Exceções (`try/except`)
* `match-case`

---

## 📂 Estrutura de Dados

O sistema utiliza quatro listas principais com 20 registros cada:

* `placas`
* `motoristas`
* `latitudes`
* `longitudes`

Essas listas simulam os dados recebidos pelos dispositivos de rastreamento instalados nos veículos.

---

## 🖥️ Funcionalidades

### 1️⃣ Descrição da Solução

Apresenta um resumo do projeto e seus objetivos.

---

### 2️⃣ Exibir Frota Monitorada

Mostra todos os veículos cadastrados e seus respectivos motoristas.

---

### 3️⃣ Consultar Localização

Permite consultar a posição atual de um veículo por meio da placa.

Informações exibidas:

* Placa
* Motorista
* Latitude
* Longitude

---

### 4️⃣ Atualizar Localização

Simula o envio de dados pelo dispositivo IoT.

O usuário informa:

* Placa do veículo
* Nova latitude
* Nova longitude

---

### 5️⃣ Verificar Alertas

Analisa as coordenadas registradas e identifica possíveis desvios de rota.

Caso uma localização esteja fora da área esperada, um alerta é exibido.

---

### 6️⃣ Relatório Geral

Exibe:

* Quantidade total de veículos monitorados;
* Lista completa da frota;
* Coordenadas atuais.

---

### 7️⃣ Estatísticas

Realiza análises simples da frota, mostrando:

* Quantidade de veículos no Hemisfério Norte;
* Quantidade de veículos no Hemisfério Sul;
* Região com maior concentração de veículos.

---

### 8️⃣ Encerrar Sistema

Finaliza a execução do programa.

---

## ▶️ Como Executar

### Pré-requisitos

* Python 3 instalado

Verifique a instalação:

```bash
python --version
```

ou

```bash
python3 --version
```

### Executando o Projeto

Clone o repositório:

```bash
git clone https://github.com/joaorafaelbf/gs-python
```

Acesse a pasta:

```bash
cd gs-python
```

Execute o programa:

```bash
python orbittrack.py
```

ou

```bash
python3 orbittrack.py
```

---

## 📊 Requisitos Atendidos

✔ Definição do problema

✔ Menu interativo

✔ 4 listas com 20 informações cada

✔ Estruturas de decisão (`if`, `elif`, `else`)

✔ Estruturas de repetição (`for`, `while`)

✔ Estrutura `match-case`

✔ Tratamento de exceções (`try/except`)

✔ Funções (`def`)

✔ Relatórios e análises

✔ Execução via terminal

✔ Aplicação relacionada ao tema da Global Solution

---

## 🌎 Objetivos de Desenvolvimento Sustentável (ODS)

O projeto está alinhado ao:

### ODS 9 – Indústria, Inovação e Infraestrutura

Promovendo soluções tecnológicas para melhorar a infraestrutura logística, aumentar a eficiência operacional e ampliar o acesso a sistemas de rastreamento em regiões remotas.

---

## 👨‍💻 Equipe

Projeto desenvolvido para a **Global Solution – FIAP**.
