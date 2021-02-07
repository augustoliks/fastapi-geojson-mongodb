from . import mongodb
from conf import settings

STRATEGY_DB_HIGH_ORDER = {
    'mongodb': mongodb
}

db = STRATEGY_DB_HIGH_ORDER[settings['database']['type']]
db.make_database(settings['database']['properties'])
