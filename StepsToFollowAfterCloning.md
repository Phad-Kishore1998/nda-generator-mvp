
## First create a .env file 

```.env
# HuggingFace API Token
# Get yours at: https://huggingface.co/settings/tokens
HUGGINGFACEHUB_API_TOKEN="PLEASE_ADD_YOUR TOKEN"

# Optional: Model to use (default is set in config)
# HF_MODEL_ID=mistralai/Mistral-7B-Instruct-v0.3
```

## In Case Not working register for
### DEFAULT_MODEL = "meta-llama/Llama-3.1-8B-Instruct" on hugging face 

## udpate the Model ID in section_generator.py



```bash
PS E:\Github\nda-generator-mvp\nda-generator-mvp> python -m venv myenv
PS E:\Github\nda-generator-mvp\nda-generator-mvp> venv\Scripts\activate
venv\Scripts\activate : The module 'venv' could not be loaded. For more information, run 'Import-Module venv'.
At line:1 char:1
+ venv\Scripts\activate
+ ~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (venv\Scripts\activate:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CouldNotAutoLoadModule
 
PS E:\Github\nda-generator-mvp\nda-generator-mvp> myenv\Scripts\activate
(myenv) PS E:\Github\nda-generator-mvp\nda-generator-mvp> pip install -r requirements.txt
Collecting langgraph>=0.2.0 (from -r requirements.txt (line 1))
  Using cached langgraph-1.1.6-py3-none-any.whl.metadata (8.0 kB)
Collecting langchain>=0.2.0 (from -r requirements.txt (line 2))
  Using cached langchain-1.2.15-py3-none-any.whl.metadata (5.8 kB)
Collecting langchain-community>=0.2.0 (from -r requirements.txt (line 3))
  Using cached langchain_community-0.4.1-py3-none-any.whl.metadata (3.0 kB)
Collecting huggingface-hub>=0.23.0 (from -r requirements.txt (line 4))
  Using cached huggingface_hub-1.9.2-py3-none-any.whl.metadata (14 kB)
Collecting python-dotenv>=1.0.0 (from -r requirements.txt (line 5))
  Using cached python_dotenv-1.2.2-py3-none-any.whl.metadata (27 kB)
Collecting python-docx>=1.1.0 (from -r requirements.txt (line 6))
  Using cached python_docx-1.2.0-py3-none-any.whl.metadata (2.0 kB)
Collecting langchain-huggingface>=0.1.0 (from -r requirements.txt (line 7))
  Using cached langchain_huggingface-1.2.1-py3-none-any.whl.metadata (3.3 kB)
Collecting streamlit>=1.35.0 (from -r requirements.txt (line 8))
  Using cached streamlit-1.56.0-py3-none-any.whl.metadata (9.8 kB)
Collecting langchain-core>=0.1 (from langgraph>=0.2.0->-r requirements.txt (line 1))
  Using cached langchain_core-1.2.28-py3-none-any.whl.metadata (4.4 kB)
Collecting langgraph-checkpoint<5.0.0,>=2.1.0 (from langgraph>=0.2.0->-r requirements.txt (line 1))
  Using cached langgraph_checkpoint-4.0.1-py3-none-any.whl.metadata (4.9 kB)
Collecting langgraph-prebuilt<1.1.0,>=1.0.9 (from langgraph>=0.2.0->-r requirements.txt (line 1))
  Using cached langgraph_prebuilt-1.0.9-py3-none-any.whl.metadata (5.2 kB)
Collecting langgraph-sdk<0.4.0,>=0.3.0 (from langgraph>=0.2.0->-r requirements.txt (line 1))
  Using cached langgraph_sdk-0.3.13-py3-none-any.whl.metadata (1.6 kB)
Collecting pydantic>=2.7.4 (from langgraph>=0.2.0->-r requirements.txt (line 1))
  Using cached pydantic-2.12.5-py3-none-any.whl.metadata (90 kB)
Collecting xxhash>=3.5.0 (from langgraph>=0.2.0->-r requirements.txt (line 1))
  Using cached xxhash-3.6.0-cp311-cp311-win_amd64.whl.metadata (13 kB)
Collecting langchain-classic<2.0.0,>=1.0.0 (from langchain-community>=0.2.0->-r requirements.txt (line 3))
  Using cached langchain_classic-1.0.3-py3-none-any.whl.metadata (4.8 kB)
Collecting SQLAlchemy<3.0.0,>=1.4.0 (from langchain-community>=0.2.0->-r requirements.txt (line 3))
  Using cached sqlalchemy-2.0.49-cp311-cp311-win_amd64.whl.metadata (9.8 kB)
Collecting requests<3.0.0,>=2.32.5 (from langchain-community>=0.2.0->-r requirements.txt (line 3))
  Using cached requests-2.33.1-py3-none-any.whl.metadata (4.8 kB)
Collecting PyYAML<7.0.0,>=5.3.0 (from langchain-community>=0.2.0->-r requirements.txt (line 3))
  Using cached pyyaml-6.0.3-cp311-cp311-win_amd64.whl.metadata (2.4 kB)
Collecting aiohttp<4.0.0,>=3.8.3 (from langchain-community>=0.2.0->-r requirements.txt (line 3))
  Using cached aiohttp-3.13.5-cp311-cp311-win_amd64.whl.metadata (8.4 kB)
Collecting tenacity!=8.4.0,<10.0.0,>=8.1.0 (from langchain-community>=0.2.0->-r requirements.txt (line 3))
  Using cached tenacity-9.1.4-py3-none-any.whl.metadata (1.2 kB)
Collecting dataclasses-json<0.7.0,>=0.6.7 (from langchain-community>=0.2.0->-r requirements.txt (line 3))
  Using cached dataclasses_json-0.6.7-py3-none-any.whl.metadata (25 kB)
Collecting pydantic-settings<3.0.0,>=2.10.1 (from langchain-community>=0.2.0->-r requirements.txt (line 3))
  Using cached pydantic_settings-2.13.1-py3-none-any.whl.metadata (3.4 kB)
Collecting langsmith<1.0.0,>=0.1.125 (from langchain-community>=0.2.0->-r requirements.txt (line 3))
  Using cached langsmith-0.7.27-py3-none-any.whl.metadata (15 kB)
Collecting httpx-sse<1.0.0,>=0.4.0 (from langchain-community>=0.2.0->-r requirements.txt (line 3))
  Using cached httpx_sse-0.4.3-py3-none-any.whl.metadata (9.7 kB)
Collecting numpy>=1.26.2 (from langchain-community>=0.2.0->-r requirements.txt (line 3))
  Using cached numpy-2.4.4-cp311-cp311-win_amd64.whl.metadata (6.6 kB)
Collecting filelock>=3.10.0 (from huggingface-hub>=0.23.0->-r requirements.txt (line 4))
  Using cached filelock-3.25.2-py3-none-any.whl.metadata (2.0 kB)
Collecting fsspec>=2023.5.0 (from huggingface-hub>=0.23.0->-r requirements.txt (line 4))
  Using cached fsspec-2026.3.0-py3-none-any.whl.metadata (10 kB)
Collecting hf-xet<2.0.0,>=1.4.3 (from huggingface-hub>=0.23.0->-r requirements.txt (line 4))
  Using cached hf_xet-1.4.3-cp37-abi3-win_amd64.whl.metadata (4.9 kB)
Collecting httpx<1,>=0.23.0 (from huggingface-hub>=0.23.0->-r requirements.txt (line 4))
  Using cached httpx-0.28.1-py3-none-any.whl.metadata (7.1 kB)
Collecting packaging>=20.9 (from huggingface-hub>=0.23.0->-r requirements.txt (line 4))
  Using cached packaging-26.0-py3-none-any.whl.metadata (3.3 kB)
Collecting tqdm>=4.42.1 (from huggingface-hub>=0.23.0->-r requirements.txt (line 4))
  Using cached tqdm-4.67.3-py3-none-any.whl.metadata (57 kB)
Collecting typer (from huggingface-hub>=0.23.0->-r requirements.txt (line 4))
  Using cached typer-0.24.1-py3-none-any.whl.metadata (16 kB)
Collecting typing-extensions>=4.1.0 (from huggingface-hub>=0.23.0->-r requirements.txt (line 4))
  Using cached typing_extensions-4.15.0-py3-none-any.whl.metadata (3.3 kB)
Collecting lxml>=3.1.0 (from python-docx>=1.1.0->-r requirements.txt (line 6))
  Using cached lxml-6.0.2-cp311-cp311-win_amd64.whl.metadata (3.7 kB)
Collecting tokenizers<1.0.0,>=0.19.1 (from langchain-huggingface>=0.1.0->-r requirements.txt (line 7))
  Using cached tokenizers-0.22.2-cp39-abi3-win_amd64.whl.metadata (7.4 kB)
Collecting altair!=5.4.0,!=5.4.1,<7,>=4.0 (from streamlit>=1.35.0->-r requirements.txt (line 8))
  Using cached altair-6.0.0-py3-none-any.whl.metadata (11 kB)
Collecting blinker<2,>=1.5.0 (from streamlit>=1.35.0->-r requirements.txt (line 8))
  Using cached blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)
Collecting cachetools<8,>=5.5 (from streamlit>=1.35.0->-r requirements.txt (line 8))
  Using cached cachetools-7.0.5-py3-none-any.whl.metadata (5.6 kB)
Collecting click<9,>=7.0 (from streamlit>=1.35.0->-r requirements.txt (line 8))
  Using cached click-8.3.2-py3-none-any.whl.metadata (2.6 kB)
Collecting gitpython!=3.1.19,<4,>=3.0.7 (from streamlit>=1.35.0->-r requirements.txt (line 8))
  Using cached gitpython-3.1.46-py3-none-any.whl.metadata (13 kB)
Collecting pandas<4,>=1.4.0 (from streamlit>=1.35.0->-r requirements.txt (line 8))
  Using cached pandas-3.0.2-cp311-cp311-win_amd64.whl.metadata (19 kB)
Collecting pillow<13,>=7.1.0 (from streamlit>=1.35.0->-r requirements.txt (line 8))
  Using cached pillow-12.2.0-cp311-cp311-win_amd64.whl.metadata (9.0 kB)
Collecting pydeck<1,>=0.8.0b4 (from streamlit>=1.35.0->-r requirements.txt (line 8))
  Using cached pydeck-0.9.1-py2.py3-none-any.whl.metadata (4.1 kB)
Collecting protobuf<8,>=3.20 (from streamlit>=1.35.0->-r requirements.txt (line 8))
  Using cached protobuf-7.34.1-cp310-abi3-win_amd64.whl.metadata (595 bytes)
Collecting pyarrow>=7.0 (from streamlit>=1.35.0->-r requirements.txt (line 8))
  Using cached pyarrow-23.0.1-cp311-cp311-win_amd64.whl.metadata (3.1 kB)
Collecting toml<2,>=0.10.1 (from streamlit>=1.35.0->-r requirements.txt (line 8))
  Using cached toml-0.10.2-py2.py3-none-any.whl.metadata (7.1 kB)
Collecting tornado!=6.5.0,<7,>=6.0.3 (from streamlit>=1.35.0->-r requirements.txt (line 8))
  Using cached tornado-6.5.5-cp39-abi3-win_amd64.whl.metadata (2.9 kB)
Collecting watchdog<7,>=2.1.5 (from streamlit>=1.35.0->-r requirements.txt (line 8))
  Using cached watchdog-6.0.0-py3-none-win_amd64.whl.metadata (44 kB)
Collecting aiohappyeyeballs>=2.5.0 (from aiohttp<4.0.0,>=3.8.3->langchain-community>=0.2.0->-r requirements.txt (line 3))
  Using cached aiohappyeyeballs-2.6.1-py3-none-any.whl.metadata (5.9 kB)
Collecting aiosignal>=1.4.0 (from aiohttp<4.0.0,>=3.8.3->langchain-community>=0.2.0->-r requirements.txt (line 3))
  Using cached aiosignal-1.4.0-py3-none-any.whl.metadata (3.7 kB)
Collecting attrs>=17.3.0 (from aiohttp<4.0.0,>=3.8.3->langchain-community>=0.2.0->-r requirements.txt (line 3))
  Using cached attrs-26.1.0-py3-none-any.whl.metadata (8.8 kB)
Collecting frozenlist>=1.1.1 (from aiohttp<4.0.0,>=3.8.3->langchain-community>=0.2.0->-r requirements.txt (line 3))
  Using cached frozenlist-1.8.0-cp311-cp311-win_amd64.whl.metadata (21 kB)
Collecting multidict<7.0,>=4.5 (from aiohttp<4.0.0,>=3.8.3->langchain-community>=0.2.0->-r requirements.txt (line 3))
  Using cached multidict-6.7.1-cp311-cp311-win_amd64.whl.metadata (5.5 kB)
Collecting propcache>=0.2.0 (from aiohttp<4.0.0,>=3.8.3->langchain-community>=0.2.0->-r requirements.txt (line 3))
  Using cached propcache-0.4.1-cp311-cp311-win_amd64.whl.metadata (14 kB)
Collecting yarl<2.0,>=1.17.0 (from aiohttp<4.0.0,>=3.8.3->langchain-community>=0.2.0->-r requirements.txt (line 3))
  Using cached yarl-1.23.0-cp311-cp311-win_amd64.whl.metadata (82 kB)
Collecting jinja2 (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit>=1.35.0->-r requirements.txt (line 8))
  Using cached jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
Collecting jsonschema>=3.0 (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit>=1.35.0->-r requirements.txt (line 8))
  Using cached jsonschema-4.26.0-py3-none-any.whl.metadata (7.6 kB)
Collecting narwhals>=1.27.1 (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit>=1.35.0->-r requirements.txt (line 8))
  Using cached narwhals-2.19.0-py3-none-any.whl.metadata (14 kB)
Collecting colorama (from click<9,>=7.0->streamlit>=1.35.0->-r requirements.txt (line 8))
  Using cached colorama-0.4.6-py2.py3-none-any.whl.metadata (17 kB)
Collecting marshmallow<4.0.0,>=3.18.0 (from dataclasses-json<0.7.0,>=0.6.7->langchain-community>=0.2.0->-r requirements.txt (line 3))
  Using cached marshmallow-3.26.2-py3-none-any.whl.metadata (7.3 kB)
Collecting typing-inspect<1,>=0.4.0 (from dataclasses-json<0.7.0,>=0.6.7->langchain-community>=0.2.0->-r requirements.txt (line 3))
  Using cached typing_inspect-0.9.0-py3-none-any.whl.metadata (1.5 kB)
Collecting gitdb<5,>=4.0.1 (from gitpython!=3.1.19,<4,>=3.0.7->streamlit>=1.35.0->-r requirements.txt (line 8))
  Using cached gitdb-4.0.12-py3-none-any.whl.metadata (1.2 kB)
Collecting anyio (from httpx<1,>=0.23.0->huggingface-hub>=0.23.0->-r requirements.txt (line 4))
  Using cached anyio-4.13.0-py3-none-any.whl.metadata (4.5 kB)
Collecting certifi (from httpx<1,>=0.23.0->huggingface-hub>=0.23.0->-r requirements.txt (line 4))
  Using cached certifi-2026.2.25-py3-none-any.whl.metadata (2.5 kB)
Collecting httpcore==1.* (from httpx<1,>=0.23.0->huggingface-hub>=0.23.0->-r requirements.txt (line 4))
  Using cached httpcore-1.0.9-py3-none-any.whl.metadata (21 kB)
Collecting idna (from httpx<1,>=0.23.0->huggingface-hub>=0.23.0->-r requirements.txt (line 4))
  Using cached idna-3.11-py3-none-any.whl.metadata (8.4 kB)
Collecting h11>=0.16 (from httpcore==1.*->httpx<1,>=0.23.0->huggingface-hub>=0.23.0->-r requirements.txt (line 4))
  Using cached h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)
Collecting langchain-text-splitters<2.0.0,>=1.1.1 (from langchain-classic<2.0.0,>=1.0.0->langchain-community>=0.2.0->-r requirements.txt (line 3))
  Using cached langchain_text_splitters-1.1.1-py3-none-any.whl.metadata (3.3 kB)
Collecting jsonpatch<2.0.0,>=1.33.0 (from langchain-core>=0.1->langgraph>=0.2.0->-r requirements.txt (line 1))
  Using cached jsonpatch-1.33-py2.py3-none-any.whl.metadata (3.0 kB)
Collecting uuid-utils<1.0,>=0.12.0 (from langchain-core>=0.1->langgraph>=0.2.0->-r requirements.txt (line 1))
  Using cached uuid_utils-0.14.1-cp39-abi3-win_amd64.whl.metadata (4.9 kB)
Collecting ormsgpack>=1.12.0 (from langgraph-checkpoint<5.0.0,>=2.1.0->langgraph>=0.2.0->-r requirements.txt (line 1))
  Using cached ormsgpack-1.12.2-cp311-cp311-win_amd64.whl.metadata (3.3 kB)
Collecting orjson>=3.11.5 (from langgraph-sdk<0.4.0,>=0.3.0->langgraph>=0.2.0->-r requirements.txt (line 1))
  Using cached orjson-3.11.8-cp311-cp311-win_amd64.whl.metadata (43 kB)
Collecting requests-toolbelt>=1.0.0 (from langsmith<1.0.0,>=0.1.125->langchain-community>=0.2.0->-r requirements.txt (line 3))
  Using cached requests_toolbelt-1.0.0-py2.py3-none-any.whl.metadata (14 kB)
Collecting zstandard>=0.23.0 (from langsmith<1.0.0,>=0.1.125->langchain-community>=0.2.0->-r requirements.txt (line 3))
  Using cached zstandard-0.25.0-cp311-cp311-win_amd64.whl.metadata (3.3 kB)
Collecting python-dateutil>=2.8.2 (from pandas<4,>=1.4.0->streamlit>=1.35.0->-r requirements.txt (line 8))
  Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Collecting tzdata (from pandas<4,>=1.4.0->streamlit>=1.35.0->-r requirements.txt (line 8))
  Using cached tzdata-2026.1-py2.py3-none-any.whl.metadata (1.4 kB)
Collecting annotated-types>=0.6.0 (from pydantic>=2.7.4->langgraph>=0.2.0->-r requirements.txt (line 1))
  Using cached annotated_types-0.7.0-py3-none-any.whl.metadata (15 kB)
Collecting pydantic-core==2.41.5 (from pydantic>=2.7.4->langgraph>=0.2.0->-r requirements.txt (line 1))
  Using cached pydantic_core-2.41.5-cp311-cp311-win_amd64.whl.metadata (7.4 kB)
Collecting typing-inspection>=0.4.2 (from pydantic>=2.7.4->langgraph>=0.2.0->-r requirements.txt (line 1))
  Using cached typing_inspection-0.4.2-py3-none-any.whl.metadata (2.6 kB)
Collecting charset_normalizer<4,>=2 (from requests<3.0.0,>=2.32.5->langchain-community>=0.2.0->-r requirements.txt (line 3))
  Using cached charset_normalizer-3.4.7-cp311-cp311-win_amd64.whl.metadata (41 kB)
Collecting urllib3<3,>=1.26 (from requests<3.0.0,>=2.32.5->langchain-community>=0.2.0->-r requirements.txt (line 3))
  Using cached urllib3-2.6.3-py3-none-any.whl.metadata (6.9 kB)
Collecting greenlet>=1 (from SQLAlchemy<3.0.0,>=1.4.0->langchain-community>=0.2.0->-r requirements.txt (line 3))
  Using cached greenlet-3.4.0-cp311-cp311-win_amd64.whl.metadata (3.8 kB)
Collecting shellingham>=1.3.0 (from typer->huggingface-hub>=0.23.0->-r requirements.txt (line 4))
  Using cached shellingham-1.5.4-py2.py3-none-any.whl.metadata (3.5 kB)
Collecting rich>=12.3.0 (from typer->huggingface-hub>=0.23.0->-r requirements.txt (line 4))
  Using cached rich-14.3.3-py3-none-any.whl.metadata (18 kB)
Collecting annotated-doc>=0.0.2 (from typer->huggingface-hub>=0.23.0->-r requirements.txt (line 4))
  Using cached annotated_doc-0.0.4-py3-none-any.whl.metadata (6.6 kB)
Collecting smmap<6,>=3.0.1 (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit>=1.35.0->-r requirements.txt (line 8))
  Using cached smmap-5.0.3-py3-none-any.whl.metadata (4.6 kB)
Collecting MarkupSafe>=2.0 (from jinja2->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit>=1.35.0->-r requirements.txt (line 8))
  Using cached markupsafe-3.0.3-cp311-cp311-win_amd64.whl.metadata (2.8 kB)
Collecting jsonpointer>=1.9 (from jsonpatch<2.0.0,>=1.33.0->langchain-core>=0.1->langgraph>=0.2.0->-r requirements.txt (line 1))
  Using cached jsonpointer-3.1.1-py3-none-any.whl.metadata (2.4 kB)
Collecting jsonschema-specifications>=2023.03.6 (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit>=1.35.0->-r requirements.txt (line 8))
  Using cached jsonschema_specifications-2025.9.1-py3-none-any.whl.metadata (2.9 kB)
Collecting referencing>=0.28.4 (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit>=1.35.0->-r requirements.txt (line 8))
  Using cached referencing-0.37.0-py3-none-any.whl.metadata (2.8 kB)
Collecting rpds-py>=0.25.0 (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit>=1.35.0->-r requirements.txt (line 8))
  Using cached rpds_py-0.30.0-cp311-cp311-win_amd64.whl.metadata (4.2 kB)
Collecting six>=1.5 (from python-dateutil>=2.8.2->pandas<4,>=1.4.0->streamlit>=1.35.0->-r requirements.txt (line 8))
  Using cached six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Collecting markdown-it-py>=2.2.0 (from rich>=12.3.0->typer->huggingface-hub>=0.23.0->-r requirements.txt (line 4))
  Using cached markdown_it_py-4.0.0-py3-none-any.whl.metadata (7.3 kB)
Collecting pygments<3.0.0,>=2.13.0 (from rich>=12.3.0->typer->huggingface-hub>=0.23.0->-r requirements.txt (line 4))
  Using cached pygments-2.20.0-py3-none-any.whl.metadata (2.5 kB)
Collecting mypy-extensions>=0.3.0 (from typing-inspect<1,>=0.4.0->dataclasses-json<0.7.0,>=0.6.7->langchain-community>=0.2.0->-r requirements.txt (line 3))
  Using cached mypy_extensions-1.1.0-py3-none-any.whl.metadata (1.1 kB)
Collecting mdurl~=0.1 (from markdown-it-py>=2.2.0->rich>=12.3.0->typer->huggingface-hub>=0.23.0->-r requirements.txt (line 4))
  Using cached mdurl-0.1.2-py3-none-any.whl.metadata (1.6 kB)
Using cached langgraph-1.1.6-py3-none-any.whl (169 kB)
Using cached langchain-1.2.15-py3-none-any.whl (112 kB)
Using cached langchain_community-0.4.1-py3-none-any.whl (2.5 MB)
Using cached huggingface_hub-1.9.2-py3-none-any.whl (637 kB)
Using cached python_dotenv-1.2.2-py3-none-any.whl (22 kB)
Using cached python_docx-1.2.0-py3-none-any.whl (252 kB)
Using cached langchain_huggingface-1.2.1-py3-none-any.whl (30 kB)
Using cached streamlit-1.56.0-py3-none-any.whl (9.1 MB)
Using cached aiohttp-3.13.5-cp311-cp311-win_amd64.whl (462 kB)
Using cached altair-6.0.0-py3-none-any.whl (795 kB)
Using cached blinker-1.9.0-py3-none-any.whl (8.5 kB)
Using cached cachetools-7.0.5-py3-none-any.whl (13 kB)
Using cached click-8.3.2-py3-none-any.whl (108 kB)
Using cached dataclasses_json-0.6.7-py3-none-any.whl (28 kB)
Using cached filelock-3.25.2-py3-none-any.whl (26 kB)
Using cached fsspec-2026.3.0-py3-none-any.whl (202 kB)
Using cached gitpython-3.1.46-py3-none-any.whl (208 kB)
Using cached hf_xet-1.4.3-cp37-abi3-win_amd64.whl (3.7 MB)
Using cached httpx-0.28.1-py3-none-any.whl (73 kB)
Using cached httpcore-1.0.9-py3-none-any.whl (78 kB)
Using cached httpx_sse-0.4.3-py3-none-any.whl (9.0 kB)
Using cached langchain_classic-1.0.3-py3-none-any.whl (1.0 MB)
Using cached langchain_core-1.2.28-py3-none-any.whl (508 kB)
Using cached langgraph_checkpoint-4.0.1-py3-none-any.whl (50 kB)
Using cached langgraph_prebuilt-1.0.9-py3-none-any.whl (35 kB)
Using cached langgraph_sdk-0.3.13-py3-none-any.whl (96 kB)
Using cached langsmith-0.7.27-py3-none-any.whl (360 kB)
Using cached lxml-6.0.2-cp311-cp311-win_amd64.whl (4.0 MB)
Using cached numpy-2.4.4-cp311-cp311-win_amd64.whl (12.6 MB)
Using cached packaging-26.0-py3-none-any.whl (74 kB)
Using cached pandas-3.0.2-cp311-cp311-win_amd64.whl (9.9 MB)
Using cached pillow-12.2.0-cp311-cp311-win_amd64.whl (7.1 MB)
Using cached protobuf-7.34.1-cp310-abi3-win_amd64.whl (437 kB)
Using cached pyarrow-23.0.1-cp311-cp311-win_amd64.whl (27.5 MB)
Using cached pydantic-2.12.5-py3-none-any.whl (463 kB)
Using cached pydantic_core-2.41.5-cp311-cp311-win_amd64.whl (2.0 MB)
Using cached pydantic_settings-2.13.1-py3-none-any.whl (58 kB)
Using cached pydeck-0.9.1-py2.py3-none-any.whl (6.9 MB)
Using cached pyyaml-6.0.3-cp311-cp311-win_amd64.whl (158 kB)
Using cached requests-2.33.1-py3-none-any.whl (64 kB)
Using cached sqlalchemy-2.0.49-cp311-cp311-win_amd64.whl (2.1 MB)
Using cached tenacity-9.1.4-py3-none-any.whl (28 kB)
Using cached tokenizers-0.22.2-cp39-abi3-win_amd64.whl (2.7 MB)
Using cached toml-0.10.2-py2.py3-none-any.whl (16 kB)
Using cached tornado-6.5.5-cp39-abi3-win_amd64.whl (448 kB)
Using cached tqdm-4.67.3-py3-none-any.whl (78 kB)
Using cached typing_extensions-4.15.0-py3-none-any.whl (44 kB)
Using cached watchdog-6.0.0-py3-none-win_amd64.whl (79 kB)
Using cached xxhash-3.6.0-cp311-cp311-win_amd64.whl (31 kB)
Using cached typer-0.24.1-py3-none-any.whl (56 kB)
Using cached aiohappyeyeballs-2.6.1-py3-none-any.whl (15 kB)
Using cached aiosignal-1.4.0-py3-none-any.whl (7.5 kB)
Using cached annotated_doc-0.0.4-py3-none-any.whl (5.3 kB)
Using cached annotated_types-0.7.0-py3-none-any.whl (13 kB)
Using cached attrs-26.1.0-py3-none-any.whl (67 kB)
Using cached certifi-2026.2.25-py3-none-any.whl (153 kB)
Using cached charset_normalizer-3.4.7-cp311-cp311-win_amd64.whl (159 kB)
Using cached frozenlist-1.8.0-cp311-cp311-win_amd64.whl (44 kB)
Using cached gitdb-4.0.12-py3-none-any.whl (62 kB)
Using cached greenlet-3.4.0-cp311-cp311-win_amd64.whl (238 kB)
Using cached idna-3.11-py3-none-any.whl (71 kB)
Using cached jinja2-3.1.6-py3-none-any.whl (134 kB)
Using cached jsonpatch-1.33-py2.py3-none-any.whl (12 kB)
Using cached jsonschema-4.26.0-py3-none-any.whl (90 kB)
Using cached langchain_text_splitters-1.1.1-py3-none-any.whl (35 kB)
Using cached marshmallow-3.26.2-py3-none-any.whl (50 kB)
Using cached multidict-6.7.1-cp311-cp311-win_amd64.whl (45 kB)
Using cached narwhals-2.19.0-py3-none-any.whl (446 kB)
Using cached orjson-3.11.8-cp311-cp311-win_amd64.whl (127 kB)
Using cached ormsgpack-1.12.2-cp311-cp311-win_amd64.whl (117 kB)
Using cached propcache-0.4.1-cp311-cp311-win_amd64.whl (41 kB)
Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Using cached requests_toolbelt-1.0.0-py2.py3-none-any.whl (54 kB)
Using cached rich-14.3.3-py3-none-any.whl (310 kB)
Using cached shellingham-1.5.4-py2.py3-none-any.whl (9.8 kB)
Using cached typing_inspect-0.9.0-py3-none-any.whl (8.8 kB)
Using cached typing_inspection-0.4.2-py3-none-any.whl (14 kB)
Using cached urllib3-2.6.3-py3-none-any.whl (131 kB)
Using cached uuid_utils-0.14.1-cp39-abi3-win_amd64.whl (187 kB)
Using cached yarl-1.23.0-cp311-cp311-win_amd64.whl (87 kB)
Using cached zstandard-0.25.0-cp311-cp311-win_amd64.whl (506 kB)
Using cached anyio-4.13.0-py3-none-any.whl (114 kB)
Using cached colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Using cached tzdata-2026.1-py2.py3-none-any.whl (348 kB)
Using cached h11-0.16.0-py3-none-any.whl (37 kB)
Using cached jsonpointer-3.1.1-py3-none-any.whl (7.7 kB)
Using cached jsonschema_specifications-2025.9.1-py3-none-any.whl (18 kB)
Using cached markdown_it_py-4.0.0-py3-none-any.whl (87 kB)
Using cached markupsafe-3.0.3-cp311-cp311-win_amd64.whl (15 kB)
Using cached mypy_extensions-1.1.0-py3-none-any.whl (5.0 kB)
Using cached pygments-2.20.0-py3-none-any.whl (1.2 MB)
Using cached referencing-0.37.0-py3-none-any.whl (26 kB)
Using cached rpds_py-0.30.0-cp311-cp311-win_amd64.whl (236 kB)
Using cached six-1.17.0-py2.py3-none-any.whl (11 kB)
Using cached smmap-5.0.3-py3-none-any.whl (24 kB)
Using cached mdurl-0.1.2-py3-none-any.whl (10.0 kB)
Installing collected packages: zstandard, xxhash, watchdog, uuid-utils, urllib3, tzdata, typing-extensions, tornado, toml, tenacity, smmap, six, shellingham, rpds-py, PyYAML, python-dotenv, pygments, pyarrow, protobuf, propcache, pillow, packaging, ormsgpack, orjson, numpy, narwhals, mypy-extensions, multidict, mdurl, MarkupSafe, lxml, jsonpointer, idna, httpx-sse, hf-xet, h11, greenlet, fsspec, frozenlist, filelock, colorama, charset_normalizer, certifi, cachetools, blinker, attrs, annotated-types, annotated-doc, aiohappyeyeballs, yarl, typing-inspection, typing-inspect, tqdm, SQLAlchemy, requests, referencing, python-docx, python-dateutil, pydantic-core, marshmallow, markdown-it-py, jsonpatch, jinja2, httpcore, gitdb, click, anyio, aiosignal, rich, requests-toolbelt, pydeck, pydantic, pandas, jsonschema-specifications, httpx, gitpython, dataclasses-json, aiohttp, typer, pydantic-settings, langsmith, langgraph-sdk, jsonschema, langchain-core, huggingface-hub, altair, tokenizers, streamlit, langgraph-checkpoint, langchain-text-splitters, langgraph-prebuilt, langchain-huggingface, langchain-classic, langgraph, langchain-community, langchain
Successfully installed MarkupSafe-3.0.3 PyYAML-6.0.3 SQLAlchemy-2.0.49 aiohappyeyeballs-2.6.1 aiohttp-3.13.5 aiosignal-1.4.0 altair-6.0.0 annotated-doc-0.0.4 annotated-types-0.7.0 anyio-4.13.0 attrs-26.1.0 blinker-1.9.0 cachetools-7.0.5 certifi-2026.2.25 charset_normalizer-3.4.7 click-8.3.2 colorama-0.4.6 dataclasses-json-0.6.7 filelock-3.25.2 frozenlist-1.8.0 fsspec-2026.3.0 gitdb-4.0.12 gitpython-3.1.46 greenlet-3.4.0 h11-0.16.0 hf-xet-1.4.3 httpcore-1.0.9 httpx-0.28.1 httpx-sse-0.4.3 huggingface-hub-1.9.2 idna-3.11 jinja2-3.1.6 jsonpatch-1.33 jsonpointer-3.1.1 jsonschema-4.26.0 jsonschema-specifications-2025.9.1 langchain-1.2.15 langchain-classic-1.0.3 langchain-community-0.4.1 langchain-core-1.2.28 langchain-huggingface-1.2.1 langchain-text-splitters-1.1.1 langgraph-1.1.6 langgraph-checkpoint-4.0.1 langgraph-prebuilt-1.0.9 langgraph-sdk-0.3.13 langsmith-0.7.27 lxml-6.0.2 markdown-it-py-4.0.0 marshmallow-3.26.2 mdurl-0.1.2 multidict-6.7.1 mypy-extensions-1.1.0 narwhals-2.19.0 numpy-2.4.4 orjson-3.11.8 ormsgpack-1.12.2 packaging-26.0 pandas-3.0.2 pillow-12.2.0 propcache-0.4.1 protobuf-7.34.1 pyarrow-23.0.1 pydantic-2.12.5 pydantic-core-2.41.5 pydantic-settings-2.13.1 pydeck-0.9.1 pygments-2.20.0 python-dateutil-2.9.0.post0 python-docx-1.2.0 python-dotenv-1.2.2 referencing-0.37.0 requests-2.33.1 requests-toolbelt-1.0.0 rich-14.3.3 rpds-py-0.30.0 shellingham-1.5.4 six-1.17.0 smmap-5.0.3 streamlit-1.56.0 tenacity-9.1.4 tokenizers-0.22.2 toml-0.10.2 tornado-6.5.5 tqdm-4.67.3 typer-0.24.1 typing-extensions-4.15.0 typing-inspect-0.9.0 typing-inspection-0.4.2 tzdata-2026.1 urllib3-2.6.3 uuid-utils-0.14.1 watchdog-6.0.0 xxhash-3.6.0 yarl-1.23.0 zstandard-0.25.0

[notice] A new release of pip is available: 24.0 -> 26.0.1
[notice] To update, run: python.exe -m pip install --upgrade pip
(myenv) PS E:\Github\nda-generator-mvp\nda-generator-mvp> python -m src.main --interactive
============================================================
  NDA GENERATOR MVP
============================================================

📂 Input file: None

============================================================
  NDA GENERATOR — Input Collection
============================================================
  Please provide the following details.

  Disclosing Party Name (e.g. TechCorp Inc.): Kishore
  Receiving Party Name (e.g. DataSolutions Ltd.): Kvell Dynamics

  Relationship Type:
    [1] Technology Partnership
    [2] Vendor / Supplier
    [3] Employment
    [4] Investor / Funding
    [5] Merger / Acquisition
    [6] Other
  Enter number: 3         

  Use today's date as Effective Date? [Y/n]: Y

  Purpose of this NDA (describe in 1–2 sentences): Kishore is selected for job

  Types of Confidential Information (comma-separated numbers, e.g. 1,3):
    [1] Technical (source code, algorithms, architecture)
    [2] Financial (projections, budgets, revenue data)
    [3] Business (strategies, plans, market research)
    [4] Customer Data (names, contacts, purchase history)
    [5] Legal (contracts, IP filings, compliance docs)
    [6] Other
  Enter choices: 1,2,3,4,5

  Confidentiality Duration (e.g. 3 years): 3
  Governing Law / Country (e.g. India): India
  Industry (e.g. Software and Technology): Software

------------------------------------------------------------
  ✅ Inputs collected. Summary:
     Parties:       Kishore (Disclosing Party) and Kvell Dynamics (Receiving Party)
     Relationship:  Employment
     Purpose:       Kishore is selected for job
     Info Types:    Technical (source code, algorithms, architecture), Financial (projections, budgets, revenue data), Business (strategies, plans, market research), Customer Data (names, contacts, purchase history), Legal (contracts, IP filings, compliance docs)
     Duration:      3
     Governing Law: India
     Industry:      Software
------------------------------------------------------------


[2/4] Building LangGraph workflow...
      ✓ Workflow compiled (7 section nodes + merge node)

[3/4] Executing NDA generation pipeline...
      Sections will be generated in parallel.

  → Generating Section 1: Purpose, Parties, and Context
  → Generating Section 2: Definition of Confidential Information
  → Generating Section 4: Obligations of the Receiving Party
  → Generating Section 5: Permitted Disclosures and Exceptions
  → Generating Section 3: Categories and Scope of Confidential Information
  → Generating Section 6: Breach, Remedies, and Liability
  → Generating Section 7: Miscellaneous and General Legal Terms
  ✓ Section 2 saved → E:\Github\nda-generator-mvp\nda-generator-mvp\outputs\drafts\section_2.txt
  ✓ Section 6 saved → E:\Github\nda-generator-mvp\nda-generator-mvp\outputs\drafts\section_6.txt
  ✓ Section 3 saved → E:\Github\nda-generator-mvp\nda-generator-mvp\outputs\drafts\section_3.txt
  ✓ Section 4 saved → E:\Github\nda-generator-mvp\nda-generator-mvp\outputs\drafts\section_4.txt
  ✓ Section 7 saved → E:\Github\nda-generator-mvp\nda-generator-mvp\outputs\drafts\section_7.txt
  ✓ Section 5 saved → E:\Github\nda-generator-mvp\nda-generator-mvp\outputs\drafts\section_5.txt
  ✓ Section 1 saved → E:\Github\nda-generator-mvp\nda-generator-mvp\outputs\drafts\section_1.txt

📋 Sections completed: [1, 2, 3, 4, 5, 6, 7]

📎 Merging all sections into final document...
✅ Final NDA document saved → E:\Github\nda-generator-mvp\nda-generator-mvp\outputs\final\nda_final.txt

[4/4] Pipeline complete.

✅ Final NDA document: E:\Github\nda-generator-mvp\nda-generator-mvp\outputs\final\nda_final.txt

============================================================
  DONE
============================================================

(myenv) PS E:\Github\nda-generator-mvp\nda-generator-mvp> 



```