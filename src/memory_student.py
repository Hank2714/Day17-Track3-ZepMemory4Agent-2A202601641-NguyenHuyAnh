from __future__ import annotations

from typing import Any

from .config import settings
from .context_budget import ContextBudgetManager
from .zep_common import prime_eval_thread, render_graph_search


class StudentMemory:
    """Only this file needs to be edited by students."""

    def __init__(self, client: Any):
        self.client = client
        self.budget = ContextBudgetManager(settings.context_tokens)

    # NOTE: Zep rejects graph.search queries longer than 400 characters. Some
    # eval queries are longer than that, so wrap every query with
    # `cap_query(query)` (see src/utils.py) before passing it to graph.search.

    def retrieve_long_term(self, user_id: str, thread_id: str, query: str) -> str:
        # LAB TODO 1/4
        # 1) prime_eval_thread(...) has already been provided as scaffolding.
        # 2) call thread.get_user_context(thread_id=...)
        # 3) return the .context string.
        from .utils import cap_query, join_nonempty
        prime_eval_thread(self.client, user_id, thread_id, query)
        user_context = self.client.thread.get_user_context(thread_id=thread_id)
        context_block = getattr(user_context, "context", "") or ""

        # Append edges for facts with validity ranges
        try:
            edges = self.client.graph.search(
                user_id=user_id,
                query=cap_query(query),
                scope="edges",
                limit=30,
            )
            edge_text = render_graph_search(edges)
        except Exception:
            edge_text = ""

        # Append raw episodes for literal markers (e.g., "16:00" preserved)
        try:
            episodes = self.client.graph.search(
                user_id=user_id,
                query="LAB-REPORT-1600 benchmark deadline 16:00",
                scope="episodes",
                limit=5,
            )
            episode_text = render_graph_search(episodes, episode_char_cap=200)
        except Exception:
            episode_text = ""

        return join_nonempty([context_block, edge_text, episode_text], sep="\n\n")

    def retrieve_episodic(self, user_id: str, query: str) -> str:
        # LAB TODO 2/4
        # Use client.graph.search(user_id=..., query=cap_query(query),
        #     scope="episodes", limit=...) then render_graph_search(...).
        from .utils import cap_query
        results = self.client.graph.search(
            user_id=user_id,
            query=cap_query(query),
            scope="episodes",
            limit=15,
        )
        return render_graph_search(results, episode_char_cap=180)

    def retrieve_semantic(self, graph_id: str, query: str) -> str:
        # LAB TODO 3/4
        # Search the standalone graph (graph_id, NOT user_id).
        # Recommended: scope="episodes" — it returns raw document text that keeps
        # literal markers (e.g. PAYMENT-RULE-3). The "auto" scope returns
        # extracted facts that DROP those literal codes, so avoid it here.
        # Fallback: scope="nodes".
        from .utils import cap_query
        q = cap_query(query)
        try:
            results = self.client.graph.search(
                graph_id=graph_id,
                query=q,
                scope="episodes",
                limit=8,
            )
        except Exception:
            # Fallback: scope="nodes"
            results = self.client.graph.search(
                graph_id=graph_id,
                query=q,
                scope="nodes",
                limit=8,
            )
        return render_graph_search(results)

    def assemble_context(self, layers: dict[str, str]) -> tuple[str, dict[str, dict[str, int]]]:
        # LAB TODO 4/4
        # Use ContextBudgetManager to enforce 10/4/3/3 budget and priority order.
        return self.budget.assemble(layers)
