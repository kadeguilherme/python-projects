from flask.json import JSONEncoder

class ONGS(object):
    new_id = 1
    def __init__(self,name,founder,sector):
        self.name = name
        self.founder = founder
        self.sector = sector
        self.new_id = ONGS.new_id
        ONGS.new_id += 1

class ONGSEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ONGS):
            return obj.__dict__
        return super(ONGSEncoder, self).default(obj)