# Lab 17 Submission - Multi-Memory Agent with Zep

## 1. Analysis Questions

**Q1: Which memory layer is most important in this test suite?**
Long-term memory (Context Block) is the most critical layer in this benchmark. It covers 5 cases (E02, E03, E08, E09, E07) and handles cross-session preference recall, open-loop tracking, recency/conflict resolution, and user isolation. Without it, agents cannot maintain persistent user context across sessions.

**Q2: Trade-off Context Block/Zep vs Redis+Qdrant.**
Context Block (Zep) provides automatic relevance-ranking, user summaries, and episodic provenance out-of-the-box, but introduces vendor lock-in and latency (avg 900ms for long-term). Redis+Qdrant offers full control and faster local retrieval, but requires building relevance ranking, user scoping, and provenance tracking from scratch. For rapid prototyping, Zep wins; for cost control and data sovereignty, self-hosted Redis+Qdrant is better.

**Q3: Guardrail against memory poisoning.**
Guardrails include: (1) consent check before ingestion (require_memory_consent), (2) PII minimization (minimize_pii) that redacts emails/phones, (3) user-scoped namespaces ensuring isolation, and (4) Right-to-be-forgotten capability via forget endpoint. These prevent unauthorized data retention and cross-user leakage.

## 2. Benchmark Analysis

**Q1: Which layer has the lowest hit rate?**
In the no-memory baseline, all layers except short-term show 0% hit rate. With memory enabled, all layers achieve 100%. Short-term is inherently reliable because evidence stays in the current thread.

**Q2: Which case retrieves the most tokens?**
E03 (long-term, open loop) retrieves 769 tokens - the highest in the test suite. This is because it must fetch user summary + all relevant episodes containing the benchmark report deadline.

**Q3: Mixed case E07 requires which memories?**
E07 needs both long-term (for Python preference from ORCHID-27) and semantic (for Idempotency-Key retry rules). Evidence: both "Python" and "Idempotency-Key" must appear in retrieved context.

**Q4: Token reduction insight.**
No-memory shows 81.8% token reduction but 0% hit rate for durable layers - it simply retrieves nothing. This demonstrates that high token reduction is meaningless without evidence retrieval. Memory-enabled agent achieves 14.2% reduction while maintaining 100% hit rate, proving selective retrieval is more effective than either extreme.

## 3. Case Studies

**E08 Recency/Conflict:**
When Minh updated BLUEBIRD-42 to require TypeScript/NestJS (after initially preferring Python for personal projects), the Context Block correctly returns the new preference. Old facts remain in episodic history for provenance, but current context reflects recency wins - the agent knows Python is still preferred for ORCHID-27 but NOT for BLUEBIRD-42.

**E10 Compaction:**
When 12 turns exceed max_recent_messages=4, durable notes preserve the REVIEW-DEADLINE-1600 constraint. The sliding window keeps recent turns + state summary + durable notes, ensuring critical constraints survive eviction. This demonstrates that compaction isn't "lossy compression" but "priority-aware retention."
