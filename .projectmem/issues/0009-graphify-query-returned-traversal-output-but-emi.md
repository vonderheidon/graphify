# #0009 graphify query returned traversal output but emitted Failed to create stream fd: Operation not permitted under the restricted environment; query result remained usable.

- 2026-06-30T20:15:52Z `issue`: graphify query returned traversal output but emitted Failed to create stream fd: Operation not permitted under the restricted environment; query result remained usable. [graphify-out/graph.json]
- 2026-06-30T20:17:53Z `attempt`: Running commands through the non-login shell removed the stream-fd warning while preserving command output, isolating the issue to shell startup integration rather than Graphify query behavior. [shell startup] (worked)
- 2026-06-30T20:19:14Z `fix`: Confirmed Graphify query itself is healthy; using the non-login execution path avoids the restricted shell startup stream-fd warning. [shell startup]
