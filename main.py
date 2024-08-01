import os
import nest_asyncio
nest_asyncio.apply()
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the Google API Key from environment variable
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
URL = os.getenv("URL")

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY environment variable is not set")

from scrapegraphai.helpers import nodes_metadata
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from scrapegraphai.models import Gemini
from scrapegraphai.graphs import BaseGraph
from scrapegraphai.nodes import FetchNode, ParseNode, RAGNode, GenerateAnswerNode

# Define the configuration for the graph
graph_config = {
    "llm": {
        "api_key": GOOGLE_API_KEY,
        "model": "gemini-pro",
        "temperature": 0,
        "streaming": True
    },
}

llm_model = Gemini(graph_config["llm"])
embedder = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# Define the nodes for the graph
fetch_node = FetchNode(
    input="url | local_dir",
    output=["doc", "link_urls", "img_urls"],
    node_config={
        "verbose": True,
        "headless": True,
    }
)

parse_node = ParseNode(
    input="doc",
    output=["parsed_doc"],
    node_config={
        "chunk_size": 4096,
        "verbose": True,
    }
)

rag_node = RAGNode(
    input="user_prompt & (parsed_doc | doc)",
    output=["relevant_chunks"],
    node_config={
        "llm_model": llm_model,
        "embedder_model": embedder,
        "verbose": True,
    }
)

generate_answer_node = GenerateAnswerNode(
    input="user_prompt & (relevant_chunks | parsed_doc | doc)",
    output=["answer"],
    node_config={
        "llm_model": llm_model,
        "verbose": True,
    }
)

# Create the graph by defining the nodes and their connections
graph = BaseGraph(
    nodes=[
        fetch_node,
        parse_node,
        rag_node,
        generate_answer_node,
    ],
    edges=[
        (fetch_node, parse_node),
        (parse_node, rag_node),
        (rag_node, generate_answer_node)
    ],
    entry_point=fetch_node
)

# Execute the graph
result, execution_info = graph.execute({
    "user_prompt": "Extract all phone numbers and email addresses from this page. Provide the results in a structured format with separate fields for phone numbers and email addresses.",
    "url": URL
})

# Get the answer from the result
result = result.get("answer", "No answer found.")

import json

output = json.dumps(result, indent=2)
line_list = output.split("\n")

# Print each line of the output
for line in line_list:
    print(line)