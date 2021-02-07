from . import mongodb
from conf import settings

STRATEGY_DB_HIGH_ORDER = {
    'mongodb': mongodb
}

db_implementation = STRATEGY_DB_HIGH_ORDER[settings['database']['type']]
db = db_implementation.make_database(settings['database']['properties'])
db_implementation.setup_database(db)