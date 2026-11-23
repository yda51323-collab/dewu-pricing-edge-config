# 得物 · 比价边缘节点运行时配置

比价服务的边缘节点（edge）运行时配置：上游探测路由、限速、对象存储与缓存凭据。

## 目录

```
conf/edge-routes.yaml           边缘节点路由与限速
src/dewu_pricing_edge.py        配置加载与路由解析
```

## 服务标识

- 业务标识：`得物`（比价服务边缘节点）
- 出现位置：`conf/edge-routes.yaml` 的 `service` 与域名 `*.dewu.internal`、`dewu_pricing_edge.py` 的 `SERVICE` 常量与类名、`README` 标题

## 使用

```bash
python src/dewu_pricing_edge.py --env prod --dump-routes
```

## 字段说明

| 键 | 说明 |
|---|---|
| `edges[].host` | 边缘节点内部域名 |
| `edges[].cidr` | 节点所在网段 |
| `upstream.weight` | 上游探测权重 |
| `storage.bucket` | 归档桶名 |
| `storage.ak/sk` | 归档桶访问凭据 |

## 已知问题

1. `qps_limit` 按节点配置，扩缩容后需同步，否则新节点按默认 200 限速。
2. 归档桶生命周期由对象存储侧控制，配置里不再重复声明。

## 维护

比价平台组 · 变更单 `CHG-2026-1112`
