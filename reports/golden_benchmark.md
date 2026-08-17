# Lab 17 Golden Set Report

- Implementation: `student`
- Kind: `golden`
- Cases: **20**
- Passed: **20/20**
- Evidence hit rate: **100.0%**
- Average retrieval latency: **980.2 ms**
- Average token reduction vs full source context: **6.3%**
- Golden bonus: **10/10** (100% required)

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| G01 | short_term | PASS | 0.2 | 227 | 0.0% |  |
| G02 | short_term | PASS | 0.0 | 133 | 0.0% |  |
| G08 | long_term | PASS | 1646.6 | 760 | 0.0% |  |
| G09 | long_term | PASS | 1439.8 | 1731 | 0.0% |  |
| G12 | semantic | PASS | 282.0 | 418 | 8.9% |  |
| G14 | semantic | PASS | 316.5 | 270 | 30.2% |  |
| G15 | semantic | PASS | 227.4 | 270 | 41.2% |  |
| G19 | mixed | PASS | 1703.6 | 581 | 0.0% |  |
| G03 | long_term | PASS | 1460.0 | 1732 | 0.0% |  |
| G04 | long_term | PASS | 1431.4 | 1674 | 0.0% |  |
| G05 | long_term | PASS | 1486.6 | 1679 | 0.0% |  |
| G10 | episodic | PASS | 228.3 | 582 | 0.0% |  |
| G11 | episodic | PASS | 234.7 | 614 | 0.0% |  |
| G13 | semantic | PASS | 257.4 | 416 | 26.4% |  |
| G16 | mixed | PASS | 1713.0 | 581 | 0.0% |  |
| G18 | mixed | PASS | 458.7 | 500 | 11.5% |  |
| G20 | mixed | PASS | 1893.4 | 831 | 0.0% |  |
| G06 | long_term | PASS | 1541.0 | 1729 | 0.0% |  |
| G07 | long_term | PASS | 1607.0 | 1722 | 0.0% |  |
| G17 | mixed | PASS | 1677.0 | 581 | 8.1% |  |

## Evidence excerpts

### G01 - short_term

`<SESSION_SUMMARY> user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. | assistant: Noted standup constraint. | user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. | assistant: Noted staging constraint. | user: Filler A about button padding. | assistant: Filler A. | user: Filler B about color tokens. | assistant: Filler B. | user: Filler C about copy tone. | assistant: Filler C. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. - assistant: Noted standup constraint. - user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. - assistant: Noted staging constraint. </DURA`

### G02 - short_term

`<RECENT_TURNS> user: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. assistant: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. user: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. assistant: Toi se uu tien timeline khi giai thich coroutine va Task. user: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. </RECENT_TURNS>`

### G08 - long_term

`<USER_SUMMARY> Lan's project is LOTUS-88. They prioritize Java and Spring Boot for backend examples and do not use Python for the backend. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-17 08:06:47     Source: message     Content: [user] {   "user_id": "lan-lab17",   "first_name": "Lan",   "last_name": "Tran",   "user_alias": "Evaluation User" }: Minh la Lan, minh dang muon them retry cho phan goi payment trong san pham cua minh va minh muon vi du code hop voi dung stack ma minh dang dung chu dung dua cho minh vi du cua ngon ngu khac. Ban gy y gium minh: dua theo backend ma minh da chon cho san pham cua minh, min`

### G09 - long_term

`<USER_SUMMARY> The user's personal project is named ORCHID-27, for which they prefer Python. For company projects such as BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project.  Minh prefers Python and dislikes Java. When explaining code, Minh wants short examples. The user is learning async/await and sometimes confuses coroutines with Tasks. When discussing this topic in the future, the user wants explanations presented as a timeline.  The AI will prioritize timelines when explaining coroutines and Tasks. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-05 08:00:00`

### G12 - semantic

`EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. metadata= EPISODE: Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodic 3 percent, semantic 3 percent; trim lower-priority memory first. Marker: BUDGET-10-4-3-3. metadata= EPISODE: {"id":"kb-payment-retry","entity":"Payment API Retry Policy","summary":"For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3.","source":"intern`

### G14 - semantic

`EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. metadata= EPISODE: Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodic 3 percent, semantic 3 percent; trim lower-priority memory first. Marker: BUDGET-10-4-3-3. metadata= EPISODE: {"id":"kb-memory-privacy","entity":"Agent Memory Privacy Rule","summary":"Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL.","source":"memory-governance-policy","updated_at":"2`

### G15 - semantic

`EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. metadata= EPISODE: Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodic 3 percent, semantic 3 percent; trim lower-priority memory first. Marker: BUDGET-10-4-3-3. metadata= EPISODE: {"id":"kb-memory-privacy","entity":"Agent Memory Privacy Rule","summary":"Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL.","source":"memory-governance-policy","updated_at":"2`

### G19 - mixed

`<LONG_TERM> <USER_SUMMARY> Lan's project is LOTUS-88. They prioritize Java and Spring Boot for backend examples and do not use Python for the backend. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-17 08:22:44     Source: message     Content: [user] {   "user_id": "lan-lab17",   "first_name": "Lan",   "last_name": "Tran",   "user_alias": "Evaluation User" }: Lan uu tien stack backend nao cho LOTUS-88?   - Created At: 2026-08-01 11:00:00     Source: message     Content: [user] {   "user_id": "lan-lab17",   "first_name": "Lan",   "last_name": "Tran",   "user_alias": "Lan Tran" }: Toi la Lan. Du an cua toi la LOTUS-`

### G03 - long_term

`<USER_SUMMARY> The user's personal project is named ORCHID-27, for which they prefer Python. For company projects such as BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project.  Minh prefers Python and dislikes Java. When explaining code, Minh wants short examples. The user is learning async/await and sometimes confuses coroutines with Tasks. When discussing this topic in the future, the user wants explanations presented as a timeline.  The AI will prioritize timelines when explaining coroutines and Tasks. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-17 08:22:45`

### G04 - long_term

`<USER_SUMMARY> The user's personal project is named ORCHID-27, for which they prefer Python. For company projects such as BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project.  Minh prefers Python and dislikes Java. When explaining code, Minh wants short examples. The user is learning async/await and sometimes confuses coroutines with Tasks. When discussing this topic in the future, the user wants explanations presented as a timeline.  The AI will prioritize timelines when explaining coroutines and Tasks. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-17 08:22:46`

### G05 - long_term

`<USER_SUMMARY> The user's personal project is named ORCHID-27, for which they prefer Python. For company projects such as BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project.  Minh prefers Python and dislikes Java. When explaining code, Minh wants short examples. The user is learning async/await and sometimes confuses coroutines with Tasks. When discussing this topic in the future, the user wants explanations presented as a timeline.  The AI will prioritize timelines when explaining coroutines and Tasks. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-01 09:02:00`

### G10 - episodic

`EPISODE: Minh dang lam kiem ke lai mo hinh cac du an backend de bao cao, ma minh rat so cai vu bi gan nham du an cua nguoi khac vao ho so cua minh, chuyen do tung xay ra roi nen lan nay min EPISODE: Minh dang ngoi mot minh viet cho xong cai ham retry cho POST payment de toi nay demo, va minh muon no vua dung dung ngon ngu ma minh thich khi lam viec ca nhan, vua bam sat dung po EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: Toi se uu tien timeline khi giai thich coroutine va Task. `

### G11 - episodic

`EPISODE: Minh dang lam kiem ke lai mo hinh cac du an backend de bao cao, ma minh rat so cai vu bi gan nham du an cua nguoi khac vao ho so cua minh, chuyen do tung xay ra roi nen lan nay min EPISODE: Minh dang ngoi mot minh viet cho xong cai ham retry cho POST payment de toi nay demo, va minh muon no vua dung dung ngon ngu ma minh thich khi lam viec ca nhan, vua bam sat dung po EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00.`

### G13 - semantic

`EPISODE: When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST. metadata= EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. metadata= EPISODE: Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodic 3 percent, semantic 3 percent; trim lower-priority memory first. Marker: BUDGET-10-4-3-3. metadata= EPISODE: {"id":"kb-memory-privacy","entity":"Agent Memory Privacy Rule","summary":"`

### G16 - mixed

`<LONG_TERM> <USER_SUMMARY> The user's personal project is named ORCHID-27, for which they prefer Python. For company projects such as BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project.  Minh prefers Python and dislikes Java. When explaining code, Minh wants short examples. The user is learning async/await and sometimes confuses coroutines with Tasks. When discussing this topic in the future, the user wants explanations presented as a timeline.  The AI will prioritize timelines when explaining coroutines and Tasks. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08`

### G18 - mixed

`<EPISODIC> EPISODE: Voi demo ca nhan cua Minh, ngon ngu uu tien la gi? EPISODE: Minh dang lam kiem ke lai mo hinh cac du an backend de bao cao, ma minh rat so cai vu bi gan nham du an cua nguoi khac vao ho so cua minh, chuyen do tung xay ra roi nen lan nay min EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh `

### G20 - mixed

`<LONG_TERM> <USER_SUMMARY> The user's personal project is named ORCHID-27, for which they prefer Python. For company projects such as BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project.  Minh prefers Python and dislikes Java. When explaining code, Minh wants short examples. The user is learning async/await and sometimes confuses coroutines with Tasks. When discussing this topic in the future, the user wants explanations presented as a timeline.  The AI will prioritize timelines when explaining coroutines and Tasks. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08`

### G06 - long_term

`<USER_SUMMARY> The user's personal project is named ORCHID-27, for which they prefer Python. For company projects such as BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project.  Minh prefers Python and dislikes Java. When explaining code, Minh wants short examples. The user is learning async/await and sometimes confuses coroutines with Tasks. When discussing this topic in the future, the user wants explanations presented as a timeline.  The AI will prioritize timelines when explaining coroutines and Tasks. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-05 08:00:00`

### G07 - long_term

`<USER_SUMMARY> The user's personal project is named ORCHID-27, for which they prefer Python. For company projects such as BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project.  Minh prefers Python and dislikes Java. When explaining code, Minh wants short examples. The user is learning async/await and sometimes confuses coroutines with Tasks. When discussing this topic in the future, the user wants explanations presented as a timeline.  The AI will prioritize timelines when explaining coroutines and Tasks. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-17 08:22:45`

### G17 - mixed

`<LONG_TERM> <USER_SUMMARY> The user's personal project is named ORCHID-27, for which they prefer Python. For company projects such as BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project.  Minh prefers Python and dislikes Java. When explaining code, Minh wants short examples. The user is learning async/await and sometimes confuses coroutines with Tasks. When discussing this topic in the future, the user wants explanations presented as a timeline.  The AI will prioritize timelines when explaining coroutines and Tasks. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08`
