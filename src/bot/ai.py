from functools import lru_cache

from llama_index.core import VectorStoreIndex
from llama_index.vector_stores.upstash import UpstashVectorStore 
import httpx
import helpers
import openai
from upstash_vector import Index

OPENAI_API_KEY = helpers.config("OPENAI_API_KEY", default=None)
UPSTASH_VECTOR_URL = helpers.config("UPSTASH_VECTOR_URL", default=None)
UPSTASH_VECTOR_TOKEN= helpers.config("UPSTASH_VECTOR_TOKEN", default=None)


@lru_cache
def get_vector_store_index(): 
    openai.api_key = OPENAI_API_KEY
    timeout = httpx.Timeout(600.0, connect=600.0)
    client = httpx.Client(timeout=timeout)
    url=UPSTASH_VECTOR_URL
    token=UPSTASH_VECTOR_TOKEN
    upstash_index = Index(
        url=url, 
        token=token,
        retries=5,
        retry_interval=0.2
    )
    upstash_index._client = client
    vector_store = UpstashVectorStore(
        url=url, 
        token=token,
    )
    vector_store._index = upstash_index
    return VectorStoreIndex.from_vector_store(vector_store=vector_store)

@lru_cache
def get_query_engine():
    index = get_vector_store_index()
    return index.as_query_engine()


def query(message, raw=False):
    query_engine = get_query_engine()
    r = query_engine.query(message)
    if raw:
        return r
    return r.response



