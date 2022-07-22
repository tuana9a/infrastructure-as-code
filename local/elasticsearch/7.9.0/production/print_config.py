import yaml

es01_host = "172.19.0.11"
es02_host = "172.19.0.12"
es03_host = "172.19.0.13"

"""
/etc/elasticsearch/elasticsearch.yml

OR

/usr/share/elasticsearch/config/elasticsearch.yml
"""

cert_dir = "/usr/share/elasticsearch/config/certificates"


def create_config(bind_host="0.0.0.0", publish_host="0.0.0.0",
                  name="es", cluster_name="es-cluster",
                  initial_master_nodes=[es01_host, es02_host, es03_host],
                  discovery_seed_hosts=[es01_host, es02_host, es03_host],
                  server_key_file="server.key",
                  server_cert_file="server.crt",
                  ca_cert_file="rootCA.crt",
                  ):
    x = {
        "node.name": name,
        "cluster.name": cluster_name,
        "network.bind_host": bind_host,
        "transport.publish_host": publish_host,
        "cluster.initial_master_nodes": initial_master_nodes,
        "discovery.seed_hosts": discovery_seed_hosts,
        "xpack.security.enabled": True,
        "xpack.security.http.ssl.enabled": True,
        "xpack.license.self_generated.type": "basic",
        "xpack.security.enabled": True,
        "xpack.security.http.ssl.enabled": True,
        "xpack.security.http.ssl.key": cert_dir + "/" + server_key_file,
        "xpack.security.http.ssl.certificate_authorities": cert_dir + "/" + ca_cert_file,
        "xpack.security.http.ssl.certificate": cert_dir + "/" + server_cert_file,
        "xpack.security.transport.ssl.enabled": True,
        "xpack.security.transport.ssl.verification_mode": "certificate",
        "xpack.security.transport.ssl.certificate_authorities": cert_dir + "/" + ca_cert_file,
        "xpack.security.transport.ssl.certificate": cert_dir + "/" + server_cert_file,
        "xpack.security.transport.ssl.key": cert_dir + "/" + server_key_file,
    }
    return x


print(yaml.dump(create_config()))
