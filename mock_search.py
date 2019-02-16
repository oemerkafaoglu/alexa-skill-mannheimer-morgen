import json
import pdb
import database

class MockSearch:
    mock_data = [{'title': 'Merkel rechnet in München mit Trump ab', 'summary': 'Frontalangriff der Kanzlerin auf US-Präsident Donald Trump: Angela Merkel hat auf der Münchner Sicherheitskonferenz die US-Politik scharf kritisiert.', 'tags': 'trump'}, {'title': 'Großer Widerstand gegen Trumps Notstandserklärung', 'summary': 'US-Präsident Donald Trump stößt mit seiner Erklärung eines Nationalen Notstandes an der Grenze zu Mexiko auf großen Widerstand. Mehrere prominente Demokraten warfen Trump einen Angriff auf die Verfassung vor.', 'tags': 'trump'},]

    def __init__(self, search_term, user_id):
        self.term = search_term
        self.user_id = user_id
        self.search_url = f'https://www.morgenweb.de/suche_cosearch,{self.term}.html'
        self.save_search()

    def mock_result(self):
        result = self.mock_data
        return result

    def save_search(self):
        connection = database.TestDB().connection

        sql = ''' INSERT INTO user_tags(USER_UUID, TAG)
              VALUES(?,?) '''
        connection.execute(sql, (self.user_id, self.term))

        connection.commit()
        connection.close()
