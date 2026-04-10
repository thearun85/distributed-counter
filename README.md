# distributed-counter

A production-grade distributed counter service using Raft consensus - the simplest possible replicated state machine, done properly.

---

## Why This Exists

A counter is deceptively simple. On a single machine, `counter +=1` is trivial.
Across three machines, with any of them able to fail at any moment, it becomes a distributed systems problem that real infrastructure has to solve.

The same pattern powers:

- **etcd** - the key-value store Kubernetes uses for all cluster state
- **Apache ZooKeeper** - the coordination layer underneath Kafka
- **Google Chubby** - the distributed lock service

All of them are replicated state machines under the hood. This project builds the simplest possible version of that - a counter - to demonstrate that the fundamentals are understood, not just the abstractions.

---

