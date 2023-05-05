import csv
from datetime import datetime as dt

from pep_parse.settings import BASE_DIR, RESULTS_DIR


class PepParsePipeline:
    def __init__(self):
        self.status_counter = {}

    def open_spider(self, spider):
        (BASE_DIR / RESULTS_DIR).mkdir(exist_ok=True)

    def process_item(self, item, spider):
        self.status_counter[
            item['status']
        ] = self.status_counter.get(item['status'], 0) + 1
        return item

    def close_spider(self, spider):
        now = dt.now().strftime("%d-%m-%Y_%H-%M-%S")
        file_name = (BASE_DIR / RESULTS_DIR / f'status_summary_{now}.csv')
        with open(file_name, 'w', newline='') as csvfile:
            fieldnames = ['Status', 'Amount']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows({'Status': status,
                              'Amount': count}
                             for status, count
                             in self.status_counter.items())
            total = sum(self.status_counter.values())
            writer.writerow({'Status': 'Total', 'Amount': total})
