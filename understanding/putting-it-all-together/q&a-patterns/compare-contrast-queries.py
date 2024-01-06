# Compare/Contrast Queries w/ Query Transformation Module w/ a ComposableGraph
from llama_index.indices.query.query_transform.base import (
    DecomposeQueryTransform,
)

decompose_transform = DecomposeQueryTransform(
    service_context.llm, verbose = True
)

# Rely on LLM to 'infer' whether to perform Compare/Contrast Queries