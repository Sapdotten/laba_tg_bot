import json
import urllib.parse
from typing import Any

from pydantic_settings import BaseSettings, SettingsConfigDict


class ConnectionSettings(BaseSettings):
    connection_link: str
    port: int = 10808
    config_path: str = "xray_config.json"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding='utf-8',
        env_prefix="PROXY_",
        extra="ignore"
    )


def vless_to_xray_config(vless_url: str, socks_port: int = 10808) -> dict:
    parsed = urllib.parse.urlparse(vless_url)
    uuid = parsed.username
    address = parsed.hostname
    port = parsed.port
    q = urllib.parse.parse_qs(parsed.query)

    security = q.get("security", ["none"])[0]
    network = q.get("type", ["tcp"])[0]  # tcp, ws, grpc, xhttp...
    sni = q.get("sni", [address])[0]
    fp = q.get("fp", ["chrome"])[0]

    stream_settings: dict[str, Any] = {"network": network, "security": security}

    if security in ("tls", "reality"):
        tls_settings = {"serverName": sni, "fingerprint": fp}
        if security == "reality":
            tls_settings.update({
                "publicKey": q.get("pbk", [""])[0],
                "shortId": q.get("sid", [""])[0],
                "spiderX": q.get("spx", [""])[0],
            })
            stream_settings["realitySettings"] = tls_settings
        else:
            stream_settings["tlsSettings"] = tls_settings

    if network == "ws":
        stream_settings["wsSettings"] = {
            "path": q.get("path", ["/"])[0],
            "headers": {"Host": q.get("host", [sni])[0]},
        }
    elif network == "grpc":
        stream_settings["grpcSettings"] = {
            "serviceName": q.get("serviceName", [""])[0],
        }
    elif network == "xhttp":
        stream_settings["xhttpSettings"] = {
            "path": q.get("path", ["/"])[0],
            "host": q.get("host", [sni])[0],
            "mode": q.get("mode", ["auto"])[0],
        }

    return {
        "log": {"loglevel": "warning"},
        "inbounds": [{
            "listen": "0.0.0.0",
            "port": socks_port,
            "protocol": "socks",
            "settings": {"udp": True},
        }],
        "outbounds": [{
            "protocol": "vless",
            "settings": {
                "vnext": [{
                    "address": address,
                    "port": port,
                    "users": [{
                        "id": uuid,
                        "encryption": q.get("encryption", ["none"])[0],
                    }],
                }]
            },
            "streamSettings": stream_settings,
        }],
    }


proxy_settings = ConnectionSettings()
config = vless_to_xray_config(
    vless_url=proxy_settings.connection_link,
    socks_port=proxy_settings.port
)

with open(proxy_settings.config_path, "w") as f:
    json.dump(config, f, indent=2)