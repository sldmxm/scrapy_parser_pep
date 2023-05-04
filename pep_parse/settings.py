from pathlib import Path

BASE_DIR = Path(__file__).parent / '..'
RESULTS_DIR = 'results'

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True


# Было BASE_DIR / RESULTS_DIR / 'pep_%(time)s.csv', но тесты хотят не так:
# "Убедитесь, что в ключе словаря `FEEDS` перед именем файла
# указан путь к директории `results/`"
FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': [
            'number',
            'name',
            'status',
        ],
        'overwrite': True
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
