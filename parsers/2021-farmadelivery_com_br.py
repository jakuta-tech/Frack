import collections

from parsers import base


class Parse(base.Parser):
    """
        farmadelivery.com.br breach data parser
        Source File SHA-1: 
        Good Lines: 
    """

    name = "None"
    web = "farmadelivery.com.br"
    year = "2021"

    def row_format(self, r: str) -> tuple:
        """
            sample:
                barbararicardo@uol.com.br:lizie123
                'ja-fleury@bol.com.br:as102030

           name,website,year,domain,email,password,hash,salt

            :param r:
            :return:
        """
        row = r.split(':')

        if len(row) == 2:
            email = row[0]
            try:
                domain = row[0].split('@')[1]
            except:
                domain = ''
            password = row[1].strip()
        else:
            email = domain = password = ''
        
        #print(f'{email}:{password}')

        return self.name, self.web, int(self.year), domain, email, password, '', ''

    def process_rows(self) -> collections.abc.Iterable[tuple]:
        """
            Returns rows for the caller to process
        """

        with open(self.source, 'r', encoding='utf-8', errors='ignore') as source:
            for row in source:
                if row is None:
                    continue

                yield self.row_format(row)
