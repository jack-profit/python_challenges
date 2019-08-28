from sqlalchemy.orm import sessionmaker
from syl.models import Repository, engine


class SylPipeline(object):
    def process_item(self, item, spider):
        item['commits'] = int(''.join(item['commits'].split(',')))
        item['branches'] = int(item['branches'])
        item['releases'] = int(item['releases'])
        self.session.add(Repository(**item))
        return item

    def open_spider(self, spider):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def close_spider(self, spider):
        self.session.commit()
        self.session.close()
