# Парсинг PEP

### Функции
Формирует список PEP с сайта https://peps.python.org/ и размещает в директории results в файле 'pep_ДатаВремя.csv', сохраняя: 
- number (номер PEP),
- name (название PEP),
- status (статус, указанный на странице PEP)

Считает количество PEP с разными статусами и размещает в директории results в файле 'status_summary_ДатаВремя.csv''. 

### Установка проекта    
Клонируйте репозиторий:
```
git clone git@github.com:sldmxm/scrapy_parser_pep.git
```
Разверните виртуальное окружение и установите зависимости
```
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```
Запустите приложение
```
scrapy crawl pep
```

### Технологии в проекте
- Python v.3.7+
- scrapy