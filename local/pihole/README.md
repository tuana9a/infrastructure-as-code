# How to setup pihole as local dns

`systemd-resolved.service`

# `/etc/resolve.conf`

content

```conf
nameserver 172.20.0.53
nameserver 127.0.0.53
options edns0 trust-ad
search Home
```

# Other command

```bash
sudo systemctl start systemd-resolved.service
sudo systemctl stop systemd-resolved.service

sudo systemctl enable systemd-resolved.service
sudo systemctl disable systemd-resolved.service
```