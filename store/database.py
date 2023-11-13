from __future__ import annotations
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base


from constants import TABLE_NAME


class Database:
    def __init__(self, friends_list):
        self.friends_list = friends_list
        self.session: None
        self.table = TABLE_NAME

    def _connect(self):
        engine = create_engine('sqlite:///frensdb.db')
        base = declarative_base()
        ses = sessionmaker(bind=engine)

        base.metadata.create_all(engine)

        self.session = ses()
        self.session.begin()

    def _table_exists(self):
        tab = self.session.execute(text(
            "SELECT tbl_name FROM sqlite_master WHERE type='table' \
            AND tbl_name=:table")
               .bindparams(table=self.table)
               .fetchone()
               )
        if tab:
            return 1
        return 0

    def _create_table(self):
        self.session.execute(text(
            "CREATE TABLE frens (id, 'domain', first_name, last_name, sex, bdate, city, university)"
        ))

    def clear_table(self):
        self._connect()
        self.session.execute(text(
            "DELETE FROM frens where id >-1"
        ))

    def store(self):
        stmt = text("INSERT INTO frens (id, 'domain', first_name, last_name, sex, bdate, city, university) \
                    VALUES (:id, :domainn, :first_name, :last_name, :sex, :bdate, :city, :university)")
        for entry in self.friends_list:

            stmt = stmt.bindparams(
                id=entry['id'],
                domainn=entry['domain'],
                first_name=entry['first_name'],
                last_name=entry['last_name'],
                sex='F' if entry['sex'] == 1 else 'M',
                bdate=entry['bdate'] if 'bdate' in entry else '',
                city=entry['city']['title'] if 'city' in entry else '',
                university=entry['universities'][0]['name'] if 'universities' in entry and len(entry['universities']) else ''
            )
            res = self.session.execute(stmt)

        self.session.commit()
        self.session.close()


