from sqlalchemy.orm import sessionmaker
from syl.models import Repository, engine


class SylPipeline(object):
    def process_item(self, item, spider):
        if item.get('commits'):
            # repository isn't empty
            item['commits'] = int(''.join(item['commits'].split(',')))
            item['branches'] = int(''.join(item['branches'].split(',')))
            item['releases'] = int(''.join(item['releases'].split(',')))
        self.session.add(Repository(**item))
        return item

    def open_spider(self, spider):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def close_spider(self, spider):
        self.session.commit()
        self.session.close()
