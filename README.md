# Gantt Chart Project Management

Este é um sistema simples de gerenciamento de projetos usando **Syncfusion Gantt Chart**, **JavaScript puro**, **Python (Flask)** e **XML** como armazenamento.

## 📋 Funcionalidades
- Visualização de tarefas em um gráfico de Gantt.
- Adição, edição e exclusão de tarefas diretamente no gráfico.
- Armazenamento de tarefas em um arquivo XML no backend.
- Sincronização automática entre o frontend e o backend.

---

## 🛠️ Tecnologias Usadas
- **Frontend:** HTML, CSS, JavaScript (Syncfusion Gantt Chart).
- **Backend:** Python com Flask.
- **Armazenamento:** Arquivo XML para persistência de dados.

---

## 🚀 Como Rodar o Projeto

### 1. Clone o Repositório
```bash
git clone https://github.com/gabsouza-dev/Syncfusion-Gantt-Chart.git
cd gantt-chart-project
```

### 2. Configure o Ambiente Backend
- Certifique-se de ter o **Python 3** instalado.
- Instale o Flask:
  ```bash
  pip install flask
  ```

### 3. Estrutura do Projeto
```plaintext
.
├── app.py          # Backend em Python usando Flask
├── tasks.xml       # Arquivo XML para armazenamento de tarefas
├── index.html      # Frontend com Syncfusion Gantt Chart
└── README.md       # Este arquivo
```

### 4. Execute o Servidor
Inicie o servidor Flask:
```bash
python app.py
```

O servidor será iniciado em [http://localhost:5000](http://localhost:5000).

### 5. Abra o Frontend
- Acesse [http://localhost:5000](http://localhost:5000) no navegador.
- O Gantt Chart será exibido com as tarefas carregadas do arquivo `tasks.xml`.

---

## 🧩 Estrutura do Arquivo XML

O arquivo `tasks.xml` armazena as informações das tarefas:

```xml
<tasks>
    <task>
        <id>1</id>
        <name>Task 1</name>
        <start_date>2024-12-01</start_date>
        <end_date>2024-12-05</end_date>
        <progress>50</progress>
    </task>
    <task>
        <id>2</id>
        <name>Task 2</name>
        <start_date>2024-12-03</start_date>
        <end_date>2024-12-10</end_date>
        <progress>20</progress>
    </task>
</tasks>
```

- **id:** ID único da tarefa.
- **name:** Nome da tarefa.
- **start_date:** Data de início da tarefa (formato YYYY-MM-DD).
- **end_date:** Data de término da tarefa (formato YYYY-MM-DD).
- **progress:** Progresso da tarefa em porcentagem.

---

## 📜 Funcionalidades do Syncfusion Gantt Chart
- **Edição no Gráfico:** Clique em qualquer tarefa para editá-la.
- **Adição de Tarefas:** Use a barra de ferramentas para adicionar novas tarefas.
- **Exclusão de Tarefas:** Exclua tarefas diretamente no gráfico.
- **Sincronização:** As alterações no frontend são salvas automaticamente no backend e no arquivo XML.

---

## 🔧 Próximos Passos
- **Validação de Entrada:** Adicionar validações para garantir que os dados inseridos sejam válidos.
- **Exportação:** Permitir exportar o Gantt Chart como PDF ou imagem.
- **Interface Responsiva:** Melhorar a aparência para dispositivos móveis.

---

## 📝 Licença
Este projeto é de uso livre para aprendizado e desenvolvimento pessoal.

---

## 🙌 Contribuições
Sinta-se à vontade para enviar sugestões ou melhorias. Vamos construir juntos! 😊
