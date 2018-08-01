#Get topologies
curl -X GET -H "Content-Type: application/json" http://127.0.0.1:8182/restconf/config/context/topology/

#Get topology Top0
curl -X GET -H "Content-Type: application/json" http://127.0.0.1:8182/restconf/config/context/topology/0/


#Create Connectivity Service
curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8182/restconf/config/context/connectivity-service/cs1/ -d @cs1.json

#Get Connectivity Services
#curl -X GET -H "Content-Type: application/json" http://127.0.0.1:8182/restconf/config/context/connectivity-service/
#curl -X GET -H "Content-Type: application/json" http://127.0.0.1:8182/restconf/config/context/connectivity-service/cs1/

#Delete Connectivity Services
#curl -X DELETE -H "Content-Type: application/json" http://127.0.0.1:8182/restconf/config/context/connectivity-service/cs1/

#Get connection
#curl -X GET -H "Content-Type: application/json" http://127.0.0.1:8182/restconf/config/context/connection/

