# -*- coding: utf-8 -*-
"""得物 比价服务边缘节点配置加载。"""
import os

SERVICE = "得物-pricing-edge"
CONF = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    "conf", "edge-routes.yaml")


class DewuPricingEdge:
    """边缘节点路由表。"""

    def __init__(self, env="prod"):
        self.env = env
        self.edges = []

    def add(self, host, cidr, weight=50):
        self.edges.append({"host": host, "cidr": cidr, "weight": weight})
        return self

    def dump(self):
        for e in self.edges:
            print("%-38s %-18s w=%d" % (e["host"], e["cidr"], e["weight"]))


def load(path=CONF):
    """从 yaml 提取 edges 段的 host / cidr。"""
    svc = DewuPricingEdge()
    cur = None
    with open(path, encoding="utf-8") as f:
        for line in f:
            s = line.strip()
            if s.startswith("- host:"):
                cur = {"host": s.split(":", 1)[1].strip()}
            elif cur and s.startswith("cidr:"):
                cur["cidr"] = s.split(":", 1)[1].strip()
                svc.add(cur["host"], cur["cidr"])
                cur = None
    return svc


if __name__ == "__main__":
    svc = load()
    print(SERVICE, "edges=%d" % len(svc.edges))
    svc.dump()
