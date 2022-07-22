import yaml

es01_host = "172.19.0.11"
es02_host = "172.19.0.12"
es03_host = "172.19.0.13"

"""
/etc/elasticsearch/elasticsearch.yml

OR

/usr/share/elasticsearch/config/elasticsearch.yml
"""


def create_config(bind_host="0.0.0.0", publish_host="0.0.0.0",
                  name="es", cluster_name="es-cluster",
                  initial_master_nodes=[es01_host, es02_host, es03_host],
                  discovery_seed_hosts=[es01_host, es02_host, es03_host]):
    x = {
        "node.name": name,
        "cluster.name": cluster_name,
        "network.bind_host": bind_host,
        "transport.publish_host": publish_host,
        "cluster.initial_master_nodes": initial_master_nodes,
        "discovery.seed_hosts": discovery_seed_hosts,
    }
    return x


print(yaml.dump(create_config()))
