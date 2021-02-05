from pymongo import MongoClient

mongo = MongoClient(
    '127.0.0.1',
    27017,
    username='admin',
    password='senha@123'
)
db = mongo['test_database']
db['testcol'].insert_one({'1': '2'})


# db.partner.find( 
# { $and: [ 
#             {    coverageArea: {
#                     "$geoIntersects":{
#                         "$geometry":{
#                             "type":"Point", "coordinates":[34.5609, 27.2900]
#                         }
#                     }
#                 }
#             },
            
#             {     address: {
#                     "$near": {
#                         "$geometry": { 
#                             "type": "Point", "coordinates": [-46.57421, -21.785741] 
#                             }
#                          }
#                      }
#             }
#         ] 
#     } 
# )
