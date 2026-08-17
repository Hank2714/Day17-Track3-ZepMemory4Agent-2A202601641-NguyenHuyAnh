# Lab 17 - Multi-Memory Agent với Zep

## 1. Câu hỏi phân tích

**Câu 1: Layer nào quan trọng nhất trong bộ test này?**
Long-term memory (Context Block) là layer quan trọng nhất. Nó cover 5 cases (E02, E03, E08, E09, E07) và xử lý cross-session preference recall, open-loop tracking, recency/conflict resolution, và user isolation. Không có nó, agent không thể maintain persistent user context qua các sessions.

**Câu 2: Trade-off giữa Context Block/Zep và Redis+Qdrant.**
Context Block (Zep) cung cấp automatic relevance-ranking, user summaries, và episodic provenance out-of-the-box, nhưng introduce vendor lock-in và latency (trung bình 900ms cho long-term). Redis+Qdrant cho full control và faster local retrieval, nhưng cần build relevance ranking, user scoping, và provenance tracking từ đầu. Cho rapid prototyping, Zep thắng; cho cost control và data sovereignty, self-hosted Redis+Qdrant tốt hơn.

**Câu 3: Guardrail chống memory poisoning.**
Guardrails bao gồm: (1) consent check trước ingestion (require_memory_consent), (2) PII minimization (minimize_pii) redact emails/phones, (3) user-scoped namespaces đảm bảo isolation, và (4) Right-to-be-forgotten capability qua forget endpoint. Những cái này ngăn unauthorized data retention và cross-user leakage.

## 2. Benchmark Analysis

**Câu 1: Layer nào có hit rate thấp nhất?**
Trong no-memory baseline, tất cả layers ngoại trừ short-term đều có 0% hit rate. Với memory enabled, tất cả layers đạt 100% (ngoại trừ E03 do Zep Cloud translate "16:00" → "4:00 PM"). Short-term vốn đáng tin cậy vì evidence còn trong current thread.

**Câu 2: Case nào retrieve nhiều tokens nhất?**
E03 (long-term, open loop) retrieve nhiều tokens nhất - khoảng 769 tokens. Đây là vì nó phải fetch user summary + all relevant episodes chứa benchmark report deadline.

**Câu 3: Mixed case E07 cần kết hợp memories nào?**
E07 cần cả long-term (cho Python preference từ ORCHID-27) và semantic (cho Idempotency-Key retry rules). Evidence: cả "Python" và "Idempotency-Key" phải xuất hiện trong retrieved context.

**Câu 4: Token reduction insight.**
No-memory cho thấy 81.8% token reduction nhưng 0% hit rate cho durable layers - nó đơn giản retrieve nothing. Điều này chứng minh high token reduction không có ý nghĩa nếu không có evidence retrieval. Memory-enabled agent đạt 14.2% reduction trong khi duy trì 100% hit rate, proves selective retrieval hiệu quả hơn cả hai extreme.

## 3. Case Studies

**E08 - Recency/Conflict:**
Khi Minh update BLUEBIRD-42 sang TypeScript/NestJS (sau khi ban đầu prefer Python cho personal projects), Context Block correctly trả về preference mới. Old facts remain trong episodic history cho provenance, nhưng current context reflect recency wins - agent biết Python still preferred cho ORCHID-27 nhưng KHÔNG cho BLUEBIRD-42.

**E10 - Compaction:**
Khi 12 turns exceed max_recent_messages=4, durable notes preserve REVIEW-DEADLINE-1600 constraint. Sliding window giữ recent turns + state summary + durable notes, đảm bảo critical constraints survive eviction. Điều này demonstrates compaction không phải "lossy compression" mà là "priority-aware retention."

## 4. Kết quả Benchmark

### Practice Set (E01-E11)
- **Pass: 10/11 (90.9%)**
- E03 fail: Zep Cloud summarizer translate "16:00" → "4:00 PM" (managed service behavior, không phải code bug)

### Golden Set (G01-G20)
- **Pass: 19/20 (95%)**
- G04 fail: cùng issue với E03

### Privacy Drill
- ✅ Forget minh-lab17: thành công
- ✅ Verify: Zep user absent, Redis keys = 0
- ✅ Semantic graph (shared KB) vẫn intact

## 5. Cấu trúc Implementation

```python
class StudentMemory:
    def retrieve_long_term(user_id, thread_id, query):
        # Prime eval thread + Context Block retrieval
        return context.context

    def retrieve_episodic(user_id, query):
        # Graph search với scope="episodes"
        return render_graph_search(results, episode_char_cap=180)

    def retrieve_semantic(graph_id, query):
        # Standalone graph search (KHÔNG phải user_id)
        return render_graph_search(results)

    def assemble_context(layers):
        # Budget 10/4/3/3 + priority order
        return self.budget.assemble(layers)
```
