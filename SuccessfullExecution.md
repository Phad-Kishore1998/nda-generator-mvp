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
  Downloading langgraph-1.1.6-py3-none-any.whl.metadata (8.0 kB)
Collecting langchain>=0.2.0 (from -r requirements.txt (line 2))
  Downloading langchain-1.2.15-py3-none-any.whl.metadata (5.8 kB)
Collecting langchain-community>=0.2.0 (from -r requirements.txt (line 3))
  Using cached langchain_community-0.4.1-py3-none-any.whl.metadata (3.0 kB)
Collecting huggingface-hub>=0.23.0 (from -r requirements.txt (line 4))
  Downloading huggingface_hub-1.9.2-py3-none-any.whl.metadata (14 kB)
Collecting python-dotenv>=1.0.0 (from -r requirements.txt (line 5))
  Using cached python_dotenv-1.2.2-py3-none-any.whl.metadata (27 kB)
Collecting python-docx>=1.1.0 (from -r requirements.txt (line 6))
  Downloading python_docx-1.2.0-py3-none-any.whl.metadata (2.0 kB)
Collecting langchain-core>=0.1 (from langgraph>=0.2.0->-r requirements.txt (line 1))
  Downloading langchain_core-1.2.28-py3-none-any.whl.metadata (4.4 kB)
Collecting langgraph-checkpoint<5.0.0,>=2.1.0 (from langgraph>=0.2.0->-r requirements.txt (line 1))
  Using cached langgraph_checkpoint-4.0.1-py3-none-any.whl.metadata (4.9 kB)
Collecting langgraph-prebuilt<1.1.0,>=1.0.9 (from langgraph>=0.2.0->-r requirements.txt (line 1))
  Downloading langgraph_prebuilt-1.0.9-py3-none-any.whl.metadata (5.2 kB)
Collecting langgraph-sdk<0.4.0,>=0.3.0 (from langgraph>=0.2.0->-r requirements.txt (line 1))
  Downloading langgraph_sdk-0.3.13-py3-none-any.whl.metadata (1.6 kB)
Collecting pydantic>=2.7.4 (from langgraph>=0.2.0->-r requirements.txt (line 1))
  Using cached pydantic-2.12.5-py3-none-any.whl.metadata (90 kB)
Collecting xxhash>=3.5.0 (from langgraph>=0.2.0->-r requirements.txt (line 1))
  Using cached xxhash-3.6.0-cp311-cp311-win_amd64.whl.metadata (13 kB)
Collecting langchain-classic<2.0.0,>=1.0.0 (from langchain-community>=0.2.0->-r requirements.txt (line 3))
  Downloading langchain_classic-1.0.3-py3-none-any.whl.metadata (4.8 kB)
Collecting SQLAlchemy<3.0.0,>=1.4.0 (from langchain-community>=0.2.0->-r requirements.txt (line 3))
  Downloading sqlalchemy-2.0.49-cp311-cp311-win_amd64.whl.metadata (9.8 kB)
Collecting requests<3.0.0,>=2.32.5 (from langchain-community>=0.2.0->-r requirements.txt (line 3))
  Downloading requests-2.33.1-py3-none-any.whl.metadata (4.8 kB)
Collecting PyYAML<7.0.0,>=5.3.0 (from langchain-community>=0.2.0->-r requirements.txt (line 3))
  Using cached pyyaml-6.0.3-cp311-cp311-win_amd64.whl.metadata (2.4 kB)
Collecting aiohttp<4.0.0,>=3.8.3 (from langchain-community>=0.2.0->-r requirements.txt (line 3))
  Downloading aiohttp-3.13.5-cp311-cp311-win_amd64.whl.metadata (8.4 kB)
Collecting tenacity!=8.4.0,<10.0.0,>=8.1.0 (from langchain-community>=0.2.0->-r requirements.txt (line 3))
  Using cached tenacity-9.1.4-py3-none-any.whl.metadata (1.2 kB)
Collecting dataclasses-json<0.7.0,>=0.6.7 (from langchain-community>=0.2.0->-r requirements.txt (line 3))
  Using cached dataclasses_json-0.6.7-py3-none-any.whl.metadata (25 kB)
Collecting pydantic-settings<3.0.0,>=2.10.1 (from langchain-community>=0.2.0->-r requirements.txt (line 3))
  Using cached pydantic_settings-2.13.1-py3-none-any.whl.metadata (3.4 kB)
Collecting langsmith<1.0.0,>=0.1.125 (from langchain-community>=0.2.0->-r requirements.txt (line 3))
  Downloading langsmith-0.7.27-py3-none-any.whl.metadata (15 kB)
Collecting httpx-sse<1.0.0,>=0.4.0 (from langchain-community>=0.2.0->-r requirements.txt (line 3))
  Using cached httpx_sse-0.4.3-py3-none-any.whl.metadata (9.7 kB)
Collecting numpy>=1.26.2 (from langchain-community>=0.2.0->-r requirements.txt (line 3))
  Downloading numpy-2.4.4-cp311-cp311-win_amd64.whl.metadata (6.6 kB)
Collecting filelock>=3.10.0 (from huggingface-hub>=0.23.0->-r requirements.txt (line 4))
  Using cached filelock-3.25.2-py3-none-any.whl.metadata (2.0 kB)
Collecting fsspec>=2023.5.0 (from huggingface-hub>=0.23.0->-r requirements.txt (line 4))
  Downloading fsspec-2026.3.0-py3-none-any.whl.metadata (10 kB)
Collecting hf-xet<2.0.0,>=1.4.3 (from huggingface-hub>=0.23.0->-r requirements.txt (line 4))
  Downloading hf_xet-1.4.3-cp37-abi3-win_amd64.whl.metadata (4.9 kB)
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
Collecting aiohappyeyeballs>=2.5.0 (from aiohttp<4.0.0,>=3.8.3->langchain-community>=0.2.0->-r requirements.txt (line 3))
  Using cached aiohappyeyeballs-2.6.1-py3-none-any.whl.metadata (5.9 kB)
Collecting aiosignal>=1.4.0 (from aiohttp<4.0.0,>=3.8.3->langchain-community>=0.2.0->-r requirements.txt (line 3))
  Using cached aiosignal-1.4.0-py3-none-any.whl.metadata (3.7 kB)
Collecting attrs>=17.3.0 (from aiohttp<4.0.0,>=3.8.3->langchain-community>=0.2.0->-r requirements.txt (line 3))
  Downloading attrs-26.1.0-py3-none-any.whl.metadata (8.8 kB)
Collecting frozenlist>=1.1.1 (from aiohttp<4.0.0,>=3.8.3->langchain-community>=0.2.0->-r requirements.txt (line 3))
  Using cached frozenlist-1.8.0-cp311-cp311-win_amd64.whl.metadata (21 kB)
Collecting multidict<7.0,>=4.5 (from aiohttp<4.0.0,>=3.8.3->langchain-community>=0.2.0->-r requirements.txt (line 3))
  Using cached multidict-6.7.1-cp311-cp311-win_amd64.whl.metadata (5.5 kB)
Collecting propcache>=0.2.0 (from aiohttp<4.0.0,>=3.8.3->langchain-community>=0.2.0->-r requirements.txt (line 3))
  Using cached propcache-0.4.1-cp311-cp311-win_amd64.whl.metadata (14 kB)
Collecting yarl<2.0,>=1.17.0 (from aiohttp<4.0.0,>=3.8.3->langchain-community>=0.2.0->-r requirements.txt (line 3))
  Using cached yarl-1.23.0-cp311-cp311-win_amd64.whl.metadata (82 kB)
Collecting marshmallow<4.0.0,>=3.18.0 (from dataclasses-json<0.7.0,>=0.6.7->langchain-community>=0.2.0->-r requirements.txt (line 3))
  Using cached marshmallow-3.26.2-py3-none-any.whl.metadata (7.3 kB)
Collecting typing-inspect<1,>=0.4.0 (from dataclasses-json<0.7.0,>=0.6.7->langchain-community>=0.2.0->-r requirements.txt (line 3))
  Using cached typing_inspect-0.9.0-py3-none-any.whl.metadata (1.5 kB)
Collecting anyio (from httpx<1,>=0.23.0->huggingface-hub>=0.23.0->-r requirements.txt (line 4))
  Downloading anyio-4.13.0-py3-none-any.whl.metadata (4.5 kB)
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
  Downloading orjson-3.11.8-cp311-cp311-win_amd64.whl.metadata (43 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 43.1/43.1 kB 2.1 MB/s eta 0:00:00
Collecting requests-toolbelt>=1.0.0 (from langsmith<1.0.0,>=0.1.125->langchain-community>=0.2.0->-r requirements.txt (line 3))
  Using cached requests_toolbelt-1.0.0-py2.py3-none-any.whl.metadata (14 kB)
Collecting zstandard>=0.23.0 (from langsmith<1.0.0,>=0.1.125->langchain-community>=0.2.0->-r requirements.txt (line 3))
  Using cached zstandard-0.25.0-cp311-cp311-win_amd64.whl.metadata (3.3 kB)
Collecting annotated-types>=0.6.0 (from pydantic>=2.7.4->langgraph>=0.2.0->-r requirements.txt (line 1))
  Using cached annotated_types-0.7.0-py3-none-any.whl.metadata (15 kB)
Collecting pydantic-core==2.41.5 (from pydantic>=2.7.4->langgraph>=0.2.0->-r requirements.txt (line 1))
  Using cached pydantic_core-2.41.5-cp311-cp311-win_amd64.whl.metadata (7.4 kB)
Collecting typing-inspection>=0.4.2 (from pydantic>=2.7.4->langgraph>=0.2.0->-r requirements.txt (line 1))
  Using cached typing_inspection-0.4.2-py3-none-any.whl.metadata (2.6 kB)
Collecting charset_normalizer<4,>=2 (from requests<3.0.0,>=2.32.5->langchain-community>=0.2.0->-r requirements.txt (line 3))
  Downloading charset_normalizer-3.4.7-cp311-cp311-win_amd64.whl.metadata (41 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 41.7/41.7 kB 2.0 MB/s eta 0:00:00
Collecting urllib3<3,>=1.26 (from requests<3.0.0,>=2.32.5->langchain-community>=0.2.0->-r requirements.txt (line 3))
  Using cached urllib3-2.6.3-py3-none-any.whl.metadata (6.9 kB)
Collecting greenlet>=1 (from SQLAlchemy<3.0.0,>=1.4.0->langchain-community>=0.2.0->-r requirements.txt (line 3))
  Downloading greenlet-3.4.0-cp311-cp311-win_amd64.whl.metadata (3.8 kB)
Collecting colorama (from tqdm>=4.42.1->huggingface-hub>=0.23.0->-r requirements.txt (line 4))
  Using cached colorama-0.4.6-py2.py3-none-any.whl.metadata (17 kB)
Collecting click>=8.2.1 (from typer->huggingface-hub>=0.23.0->-r requirements.txt (line 4))
  Downloading click-8.3.2-py3-none-any.whl.metadata (2.6 kB)
Collecting shellingham>=1.3.0 (from typer->huggingface-hub>=0.23.0->-r requirements.txt (line 4))
  Using cached shellingham-1.5.4-py2.py3-none-any.whl.metadata (3.5 kB)
Collecting rich>=12.3.0 (from typer->huggingface-hub>=0.23.0->-r requirements.txt (line 4))
  Using cached rich-14.3.3-py3-none-any.whl.metadata (18 kB)
Collecting annotated-doc>=0.0.2 (from typer->huggingface-hub>=0.23.0->-r requirements.txt (line 4))
  Using cached annotated_doc-0.0.4-py3-none-any.whl.metadata (6.6 kB)
Collecting jsonpointer>=1.9 (from jsonpatch<2.0.0,>=1.33.0->langchain-core>=0.1->langgraph>=0.2.0->-r requirements.txt (line 1))
  Downloading jsonpointer-3.1.1-py3-none-any.whl.metadata (2.4 kB)
Collecting markdown-it-py>=2.2.0 (from rich>=12.3.0->typer->huggingface-hub>=0.23.0->-r requirements.txt (line 4))
  Using cached markdown_it_py-4.0.0-py3-none-any.whl.metadata (7.3 kB)
Collecting pygments<3.0.0,>=2.13.0 (from rich>=12.3.0->typer->huggingface-hub>=0.23.0->-r requirements.txt (line 4))
  Downloading pygments-2.20.0-py3-none-any.whl.metadata (2.5 kB)
Collecting mypy-extensions>=0.3.0 (from typing-inspect<1,>=0.4.0->dataclasses-json<0.7.0,>=0.6.7->langchain-community>=0.2.0->-r requirements.txt (line 3))
  Using cached mypy_extensions-1.1.0-py3-none-any.whl.metadata (1.1 kB)
Collecting mdurl~=0.1 (from markdown-it-py>=2.2.0->rich>=12.3.0->typer->huggingface-hub>=0.23.0->-r requirements.txt (line 4))
  Using cached mdurl-0.1.2-py3-none-any.whl.metadata (1.6 kB)
Downloading langgraph-1.1.6-py3-none-any.whl (169 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 169.8/169.8 kB 1.5 MB/s eta 0:00:00
Downloading langchain-1.2.15-py3-none-any.whl (112 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 112.7/112.7 kB 595.8 kB/s eta 0:00:00
Using cached langchain_community-0.4.1-py3-none-any.whl (2.5 MB)
Downloading huggingface_hub-1.9.2-py3-none-any.whl (637 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 637.3/637.3 kB 956.0 kB/s eta 0:00:00
Using cached python_dotenv-1.2.2-py3-none-any.whl (22 kB)
Downloading python_docx-1.2.0-py3-none-any.whl (252 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 253.0/253.0 kB 535.9 kB/s eta 0:00:00
Downloading aiohttp-3.13.5-cp311-cp311-win_amd64.whl (462 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 462.9/462.9 kB 445.9 kB/s eta 0:00:00
Using cached dataclasses_json-0.6.7-py3-none-any.whl (28 kB)
Using cached filelock-3.25.2-py3-none-any.whl (26 kB)
Downloading fsspec-2026.3.0-py3-none-any.whl (202 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 202.6/202.6 kB 241.3 kB/s eta 0:00:00
Downloading hf_xet-1.4.3-cp37-abi3-win_amd64.whl (3.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.7/3.7 MB 321.9 kB/s eta 0:00:00
Using cached httpx-0.28.1-py3-none-any.whl (73 kB)
Using cached httpcore-1.0.9-py3-none-any.whl (78 kB)
Using cached httpx_sse-0.4.3-py3-none-any.whl (9.0 kB)
Downloading langchain_classic-1.0.3-py3-none-any.whl (1.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.0/1.0 MB 488.9 kB/s eta 0:00:00
Downloading langchain_core-1.2.28-py3-none-any.whl (508 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 508.7/508.7 kB 725.6 kB/s eta 0:00:00
Using cached langgraph_checkpoint-4.0.1-py3-none-any.whl (50 kB)
Downloading langgraph_prebuilt-1.0.9-py3-none-any.whl (35 kB)
Downloading langgraph_sdk-0.3.13-py3-none-any.whl (96 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 96.7/96.7 kB 691.4 kB/s eta 0:00:00
Downloading langsmith-0.7.27-py3-none-any.whl (360 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 360.3/360.3 kB 497.9 kB/s eta 0:00:00
Using cached lxml-6.0.2-cp311-cp311-win_amd64.whl (4.0 MB)
Downloading numpy-2.4.4-cp311-cp311-win_amd64.whl (12.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12.6/12.6 MB 401.6 kB/s eta 0:00:00
Using cached packaging-26.0-py3-none-any.whl (74 kB)
Using cached pydantic-2.12.5-py3-none-any.whl (463 kB)
Using cached pydantic_core-2.41.5-cp311-cp311-win_amd64.whl (2.0 MB)
Using cached pydantic_settings-2.13.1-py3-none-any.whl (58 kB)
Using cached pyyaml-6.0.3-cp311-cp311-win_amd64.whl (158 kB)
Downloading requests-2.33.1-py3-none-any.whl (64 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 64.9/64.9 kB 868.4 kB/s eta 0:00:00
Downloading sqlalchemy-2.0.49-cp311-cp311-win_amd64.whl (2.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 404.0 kB/s eta 0:00:00
Using cached tenacity-9.1.4-py3-none-any.whl (28 kB)
Using cached tqdm-4.67.3-py3-none-any.whl (78 kB)
Using cached typing_extensions-4.15.0-py3-none-any.whl (44 kB)
Using cached xxhash-3.6.0-cp311-cp311-win_amd64.whl (31 kB)
Using cached typer-0.24.1-py3-none-any.whl (56 kB)
Using cached aiohappyeyeballs-2.6.1-py3-none-any.whl (15 kB)
Using cached aiosignal-1.4.0-py3-none-any.whl (7.5 kB)
Using cached annotated_doc-0.0.4-py3-none-any.whl (5.3 kB)
Using cached annotated_types-0.7.0-py3-none-any.whl (13 kB)
Downloading attrs-26.1.0-py3-none-any.whl (67 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 67.5/67.5 kB 183.7 kB/s eta 0:00:00
Using cached certifi-2026.2.25-py3-none-any.whl (153 kB)
Downloading charset_normalizer-3.4.7-cp311-cp311-win_amd64.whl (159 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 159.3/159.3 kB 298.1 kB/s eta 0:00:00
Downloading click-8.3.2-py3-none-any.whl (108 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 108.4/108.4 kB 570.6 kB/s eta 0:00:00
Using cached frozenlist-1.8.0-cp311-cp311-win_amd64.whl (44 kB)
Downloading greenlet-3.4.0-cp311-cp311-win_amd64.whl (238 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 238.2/238.2 kB 270.5 kB/s eta 0:00:00
Using cached idna-3.11-py3-none-any.whl (71 kB)
Using cached jsonpatch-1.33-py2.py3-none-any.whl (12 kB)
Using cached langchain_text_splitters-1.1.1-py3-none-any.whl (35 kB)
Using cached marshmallow-3.26.2-py3-none-any.whl (50 kB)
Using cached multidict-6.7.1-cp311-cp311-win_amd64.whl (45 kB)
Downloading orjson-3.11.8-cp311-cp311-win_amd64.whl (127 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 127.4/127.4 kB 227.1 kB/s eta 0:00:00
Using cached ormsgpack-1.12.2-cp311-cp311-win_amd64.whl (117 kB)
Using cached propcache-0.4.1-cp311-cp311-win_amd64.whl (41 kB)
Using cached requests_toolbelt-1.0.0-py2.py3-none-any.whl (54 kB)
Using cached rich-14.3.3-py3-none-any.whl (310 kB)
Using cached shellingham-1.5.4-py2.py3-none-any.whl (9.8 kB)
Using cached typing_inspect-0.9.0-py3-none-any.whl (8.8 kB)
Using cached typing_inspection-0.4.2-py3-none-any.whl (14 kB)
Using cached urllib3-2.6.3-py3-none-any.whl (131 kB)
Using cached uuid_utils-0.14.1-cp39-abi3-win_amd64.whl (187 kB)
Using cached yarl-1.23.0-cp311-cp311-win_amd64.whl (87 kB)
Using cached zstandard-0.25.0-cp311-cp311-win_amd64.whl (506 kB)
Downloading anyio-4.13.0-py3-none-any.whl (114 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 114.4/114.4 kB 302.7 kB/s eta 0:00:00
Using cached colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Using cached h11-0.16.0-py3-none-any.whl (37 kB)
Downloading jsonpointer-3.1.1-py3-none-any.whl (7.7 kB)
Using cached markdown_it_py-4.0.0-py3-none-any.whl (87 kB)
Using cached mypy_extensions-1.1.0-py3-none-any.whl (5.0 kB)
Downloading pygments-2.20.0-py3-none-any.whl (1.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 348.8 kB/s eta 0:00:00
Using cached mdurl-0.1.2-py3-none-any.whl (10.0 kB)
Installing collected packages: zstandard, xxhash, uuid-utils, urllib3, typing-extensions, tenacity, shellingham, PyYAML, python-dotenv, pygments, propcache, packaging, ormsgpack, orjson, numpy, mypy-extensions, multidict, mdurl, lxml, jsonpointer, idna, httpx-sse, hf-xet, h11, greenlet, fsspec, frozenlist, filelock, colorama, charset_normalizer, certifi, attrs, annotated-types, annotated-doc, aiohappyeyeballs, yarl, typing-inspection, typing-inspect, tqdm, SQLAlchemy, requests, python-docx, pydantic-core, marshmallow, markdown-it-py, jsonpatch, httpcore, click, anyio, aiosignal, rich, requests-toolbelt, pydantic, httpx, dataclasses-json, aiohttp, typer, pydantic-settings, langsmith, langgraph-sdk, langchain-core, huggingface-hub, langgraph-checkpoint, langchain-text-splitters, langgraph-prebuilt, langchain-classic, langgraph, langchain-community, langchain
Successfully installed PyYAML-6.0.3 SQLAlchemy-2.0.49 aiohappyeyeballs-2.6.1 aiohttp-3.13.5 aiosignal-1.4.0 annotated-doc-0.0.4 annotated-types-0.7.0 anyio-4.13.0 attrs-26.1.0 certifi-2026.2.25 charset_normalizer-3.4.7 click-8.3.2 colorama-0.4.6 dataclasses-json-0.6.7 filelock-3.25.2 frozenlist-1.8.0 fsspec-2026.3.0 greenlet-3.4.0 h11-0.16.0 hf-xet-1.4.3 httpcore-1.0.9 httpx-0.28.1 httpx-sse-0.4.3 huggingface-hub-1.9.2 idna-3.11 jsonpatch-1.33 jsonpointer-3.1.1 langchain-1.2.15 langchain-classic-1.0.3 langchain-community-0.4.1 langchain-core-1.2.28 langchain-text-splitters-1.1.1 langgraph-1.1.6 langgraph-checkpoint-4.0.1 langgraph-prebuilt-1.0.9 langgraph-sdk-0.3.13 langsmith-0.7.27 lxml-6.0.2 markdown-it-py-4.0.0 marshmallow-3.26.2 mdurl-0.1.2 multidict-6.7.1 mypy-extensions-1.1.0 numpy-2.4.4 orjson-3.11.8 ormsgpack-1.12.2 packaging-26.0 propcache-0.4.1 pydantic-2.12.5 pydantic-core-2.41.5 pydantic-settings-2.13.1 pygments-2.20.0 python-docx-1.2.0 python-dotenv-1.2.2 requests-2.33.1 requests-toolbelt-1.0.0 rich-14.3.3 shellingham-1.5.4 tenacity-9.1.4 tqdm-4.67.3 typer-0.24.1 typing-extensions-4.15.0 typing-inspect-0.9.0 typing-inspection-0.4.2 urllib3-2.6.3 uuid-utils-0.14.1 xxhash-3.6.0 yarl-1.23.0 zstandard-0.25.0

[notice] A new release of pip is available: 24.0 -> 26.0.1
[notice] To update, run: python.exe -m pip install --upgrade pip
(myenv) PS E:\Github\nda-generator-mvp\nda-generator-mvp> python -m src.main
============================================================
  NDA GENERATOR MVP
============================================================

📂 Input file: inputs/sample.json

[1/4] Building NDA context from input...
      Parties:          TechCorp Inc. (Disclosing Party) and DataSolutions Ltd. (Rec...
      Purpose:          Evaluating a potential technology partnership for developing...
      Governing Law:    India
      Industry:         Software and Technology
      Duration:         3 years from the date of signing

[2/4] Building LangGraph workflow...
      ✓ Workflow compiled (7 section nodes + merge node)

[3/4] Executing NDA generation pipeline...
      Sections will be generated in parallel.

  → Generating Section 1: Purpose, Parties, and Context
  → Generating Section 2: Definition of Confidential Information
  → Generating Section 3: Categories and Scope of Confidential Information
  → Generating Section 4: Obligations of the Receiving Party
  → Generating Section 5: Permitted Disclosures and Exceptions
  → Generating Section 6: Breach, Remedies, and Liability
  → Generating Section 7: Miscellaneous and General Legal Terms
  ✗ Section 1 failed: HuggingFace API call failed for section 1: Model mistralai/Mistral-7B-Instruct-v0.3 is not supported for task text-generation and provider novita. Supported task: conversational.
  ✗ Section 2 failed: HuggingFace API call failed for section 2: Model mistralai/Mistral-7B-Instruct-v0.3 is not supported for task text-generation and provider novita. Supported task: conversational.
  ✗ Section 3 failed: HuggingFace API call failed for section 3: Model mistralai/Mistral-7B-Instruct-v0.3 is not supported for task text-generation and provider novita. Supported task: conversational.
  ✗ Section 4 failed: HuggingFace API call failed for section 4: Model mistralai/Mistral-7B-Instruct-v0.3 is not supported for task text-generation and provider novita. Supported task: conversational.
  ✗ Section 5 failed: HuggingFace API call failed for section 5: Model mistralai/Mistral-7B-Instruct-v0.3 is not supported for task text-generation and provider novita. Supported task: conversational.
  ✗ Section 6 failed: HuggingFace API call failed for section 6: Model mistralai/Mistral-7B-Instruct-v0.3 is not supported for task text-generation and provider novita. Supported task: conversational.
  ✗ Section 7 failed: HuggingFace API call failed for section 7: Model mistralai/Mistral-7B-Instruct-v0.3 is not supported for task text-generation and provider novita. Supported task: conversational.
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "E:\Github\nda-generator-mvp\nda-generator-mvp\src\main.py", line 112, in <module>
    main()
  File "E:\Github\nda-generator-mvp\nda-generator-mvp\src\main.py", line 79, in main
    final_state = workflow.invoke(context)
                  ^^^^^^^^^^^^^^^^^^^^^^^^
  File "E:\Github\nda-generator-mvp\nda-generator-mvp\myenv\Lib\site-packages\langgraph\pregel\main.py", line 3309, in invoke
    for chunk in self.stream(
  File "E:\Github\nda-generator-mvp\nda-generator-mvp\myenv\Lib\site-packages\langgraph\pregel\main.py", line 2753, in stream
    loop.after_tick()
  File "E:\Github\nda-generator-mvp\nda-generator-mvp\myenv\Lib\site-packages\langgraph\pregel\_loop.py", line 544, in after_tick
    self.updated_channels = apply_writes(
                            ^^^^^^^^^^^^^
  File "E:\Github\nda-generator-mvp\nda-generator-mvp\myenv\Lib\site-packages\langgraph\pregel\_algo.py", line 297, in apply_writes
    if channels[chan].update(vals) and next_version is not None:
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "E:\Github\nda-generator-mvp\nda-generator-mvp\myenv\Lib\site-packages\langgraph\channels\last_value.py", line 64, in update
    raise InvalidUpdateError(msg)
langgraph.errors.InvalidUpdateError: At key 'parties': Can receive only one value per step. Use an Annotated key to handle multiple values.
For troubleshooting, visit: https://docs.langchain.com/oss/python/langgraph/errors/INVALID_CONCURRENT_GRAPH_UPDATE
(myenv) PS E:\Github\nda-generator-mvp\nda-generator-mvp> pip install langchain-huggingface
Collecting langchain-huggingface
  Using cached langchain_huggingface-1.2.1-py3-none-any.whl.metadata (3.3 kB)
Requirement already satisfied: huggingface-hub<2.0.0,>=0.33.4 in e:\github\nda-generator-mvp\nda-generator-mvp\myenv\lib\site-packages (from langchain-huggingface) (1.9.2)
Requirement already satisfied: langchain-core<2.0.0,>=1.2.11 in e:\github\nda-generator-mvp\nda-generator-mvp\myenv\lib\site-packages (from langchain-huggingface) (1.2.28)
Collecting tokenizers<1.0.0,>=0.19.1 (from langchain-huggingface)
  Using cached tokenizers-0.22.2-cp39-abi3-win_amd64.whl.metadata (7.4 kB)
Requirement already satisfied: filelock>=3.10.0 in e:\github\nda-generator-mvp\nda-generator-mvp\myenv\lib\site-packages (from huggingface-hub<2.0.0,>=0.33.4->langchain-huggingface) (3.25.2)
Requirement already satisfied: fsspec>=2023.5.0 in e:\github\nda-generator-mvp\nda-generator-mvp\myenv\lib\site-packages (from huggingface-hub<2.0.0,>=0.33.4->langchain-huggingface) (2026.3.0)
Requirement already satisfied: hf-xet<2.0.0,>=1.4.3 in e:\github\nda-generator-mvp\nda-generator-mvp\myenv\lib\site-packages (from huggingface-hub<2.0.0,>=0.33.4->langchain-huggingface) (1.4.3)
Requirement already satisfied: httpx<1,>=0.23.0 in e:\github\nda-generator-mvp\nda-generator-mvp\myenv\lib\site-packages (from huggingface-hub<2.0.0,>=0.33.4->langchain-huggingface) (0.28.1)
Requirement already satisfied: packaging>=20.9 in e:\github\nda-generator-mvp\nda-generator-mvp\myenv\lib\site-packages (from huggingface-hub<2.0.0,>=0.33.4->langchain-huggingface) (26.0)
Requirement already satisfied: pyyaml>=5.1 in e:\github\nda-generator-mvp\nda-generator-mvp\myenv\lib\site-packages (from huggingface-hub<2.0.0,>=0.33.4->langchain-huggingface) (6.0.3)
Requirement already satisfied: tqdm>=4.42.1 in e:\github\nda-generator-mvp\nda-generator-mvp\myenv\lib\site-packages (from huggingface-hub<2.0.0,>=0.33.4->langchain-huggingface) (4.67.3)
Requirement already satisfied: typer in e:\github\nda-generator-mvp\nda-generator-mvp\myenv\lib\site-packages (from huggingface-hub<2.0.0,>=0.33.4->langchain-huggingface) (0.24.1)
Requirement already satisfied: typing-extensions>=4.1.0 in e:\github\nda-generator-mvp\nda-generator-mvp\myenv\lib\site-packages (from huggingface-hub<2.0.0,>=0.33.4->langchain-huggingface) (4.15.0)
Requirement already satisfied: jsonpatch<2.0.0,>=1.33.0 in e:\github\nda-generator-mvp\nda-generator-mvp\myenv\lib\site-packages (from langchain-core<2.0.0,>=1.2.11->langchain-huggingface) (1.33)
Requirement already satisfied: langsmith<1.0.0,>=0.3.45 in e:\github\nda-generator-mvp\nda-generator-mvp\myenv\lib\site-packages (from langchain-core<2.0.0,>=1.2.11->langchain-huggingface) (0.7.27)
Requirement already satisfied: pydantic<3.0.0,>=2.7.4 in e:\github\nda-generator-mvp\nda-generator-mvp\myenv\lib\site-packages (from langchain-core<2.0.0,>=1.2.11->langchain-huggingface) (2.12.5)
Requirement already satisfied: tenacity!=8.4.0,<10.0.0,>=8.1.0 in e:\github\nda-generator-mvp\nda-generator-mvp\myenv\lib\site-packages (from langchain-core<2.0.0,>=1.2.11->langchain-huggingface) (9.1.4)
Requirement already satisfied: uuid-utils<1.0,>=0.12.0 in e:\github\nda-generator-mvp\nda-generator-mvp\myenv\lib\site-packages (from langchain-core<2.0.0,>=1.2.11->langchain-huggingface) (0.14.1)
Requirement already satisfied: anyio in e:\github\nda-generator-mvp\nda-generator-mvp\myenv\lib\site-packages (from httpx<1,>=0.23.0->huggingface-hub<2.0.0,>=0.33.4->langchain-huggingface) (4.13.0)
Requirement already satisfied: certifi in e:\github\nda-generator-mvp\nda-generator-mvp\myenv\lib\site-packages (from httpx<1,>=0.23.0->huggingface-hub<2.0.0,>=0.33.4->langchain-huggingface) (2026.2.25)
Requirement already satisfied: httpcore==1.* in e:\github\nda-generator-mvp\nda-generator-mvp\myenv\lib\site-packages (from httpx<1,>=0.23.0->huggingface-hub<2.0.0,>=0.33.4->langchain-huggingface) (1.0.9)
Requirement already satisfied: idna in e:\github\nda-generator-mvp\nda-generator-mvp\myenv\lib\site-packages (from httpx<1,>=0.23.0->huggingface-hub<2.0.0,>=0.33.4->langchain-huggingface) (3.11)
Requirement already satisfied: h11>=0.16 in e:\github\nda-generator-mvp\nda-generator-mvp\myenv\lib\site-packages (from httpcore==1.*->httpx<1,>=0.23.0->huggingface-hub<2.0.0,>=0.33.4->langchain-huggingface) (0.16.0)
Requirement already satisfied: jsonpointer>=1.9 in e:\github\nda-generator-mvp\nda-generator-mvp\myenv\lib\site-packages (from jsonpatch<2.0.0,>=1.33.0->langchain-core<2.0.0,>=1.2.11->langchain-huggingface) (3.1.1)
Requirement already satisfied: orjson>=3.9.14 in e:\github\nda-generator-mvp\nda-generator-mvp\myenv\lib\site-packages (from langsmith<1.0.0,>=0.3.45->langchain-core<2.0.0,>=1.2.11->langchain-huggingface) (3.11.8)
Requirement already satisfied: requests-toolbelt>=1.0.0 in e:\github\nda-generator-mvp\nda-generator-mvp\myenv\lib\site-packages (from langsmith<1.0.0,>=0.3.45->langchain-core<2.0.0,>=1.2.11->langchain-huggingface) (1.0.0)
Requirement already satisfied: requests>=2.0.0 in e:\github\nda-generator-mvp\nda-generator-mvp\myenv\lib\site-packages (from langsmith<1.0.0,>=0.3.45->langchain-core<2.0.0,>=1.2.11->langchain-huggingface) (2.33.1)
Requirement already satisfied: xxhash>=3.0.0 in e:\github\nda-generator-mvp\nda-generator-mvp\myenv\lib\site-packages (from langsmith<1.0.0,>=0.3.45->langchain-core<2.0.0,>=1.2.11->langchain-huggingface) (3.6.0)
Requirement already satisfied: zstandard>=0.23.0 in e:\github\nda-generator-mvp\nda-generator-mvp\myenv\lib\site-packages (from langsmith<1.0.0,>=0.3.45->langchain-core<2.0.0,>=1.2.11->langchain-huggingface) (0.25.0)
Requirement already satisfied: annotated-types>=0.6.0 in e:\github\nda-generator-mvp\nda-generator-mvp\myenv\lib\site-packages (from pydantic<3.0.0,>=2.7.4->langchain-core<2.0.0,>=1.2.11->langchain-huggingface) (0.7.0)
Requirement already satisfied: pydantic-core==2.41.5 in e:\github\nda-generator-mvp\nda-generator-mvp\myenv\lib\site-packages (from pydantic<3.0.0,>=2.7.4->langchain-core<2.0.0,>=1.2.11->langchain-huggingface) (2.41.5)
Requirement already satisfied: typing-inspection>=0.4.2 in e:\github\nda-generator-mvp\nda-generator-mvp\myenv\lib\site-packages (from pydantic<3.0.0,>=2.7.4->langchain-core<2.0.0,>=1.2.11->langchain-huggingface) (0.4.2)
Requirement already satisfied: colorama in e:\github\nda-generator-mvp\nda-generator-mvp\myenv\lib\site-packages (from tqdm>=4.42.1->huggingface-hub<2.0.0,>=0.33.4->langchain-huggingface) (0.4.6)
Requirement already satisfied: click>=8.2.1 in e:\github\nda-generator-mvp\nda-generator-mvp\myenv\lib\site-packages (from typer->huggingface-hub<2.0.0,>=0.33.4->langchain-huggingface) (8.3.2)
Requirement already satisfied: shellingham>=1.3.0 in e:\github\nda-generator-mvp\nda-generator-mvp\myenv\lib\site-packages (from typer->huggingface-hub<2.0.0,>=0.33.4->langchain-huggingface) (1.5.4)
Requirement already satisfied: rich>=12.3.0 in e:\github\nda-generator-mvp\nda-generator-mvp\myenv\lib\site-packages (from typer->huggingface-hub<2.0.0,>=0.33.4->langchain-huggingface) (14.3.3)
Requirement already satisfied: annotated-doc>=0.0.2 in e:\github\nda-generator-mvp\nda-generator-mvp\myenv\lib\site-packages (from typer->huggingface-hub<2.0.0,>=0.33.4->langchain-huggingface) (0.0.4)
Requirement already satisfied: charset_normalizer<4,>=2 in e:\github\nda-generator-mvp\nda-generator-mvp\myenv\lib\site-packages (from requests>=2.0.0->langsmith<1.0.0,>=0.3.45->langchain-core<2.0.0,>=1.2.11->langchain-huggingface) (3.4.7)
Requirement already satisfied: urllib3<3,>=1.26 in e:\github\nda-generator-mvp\nda-generator-mvp\myenv\lib\site-packages (from requests>=2.0.0->langsmith<1.0.0,>=0.3.45->langchain-core<2.0.0,>=1.2.11->langchain-huggingface) (2.6.3)
Requirement already satisfied: markdown-it-py>=2.2.0 in e:\github\nda-generator-mvp\nda-generator-mvp\myenv\lib\site-packages (from rich>=12.3.0->typer->huggingface-hub<2.0.0,>=0.33.4->langchain-huggingface) (4.0.0)
Requirement already satisfied: pygments<3.0.0,>=2.13.0 in e:\github\nda-generator-mvp\nda-generator-mvp\myenv\lib\site-packages (from rich>=12.3.0->typer->huggingface-hub<2.0.0,>=0.33.4->langchain-huggingface) (2.20.0)
Requirement already satisfied: mdurl~=0.1 in e:\github\nda-generator-mvp\nda-generator-mvp\myenv\lib\site-packages (from markdown-it-py>=2.2.0->rich>=12.3.0->typer->huggingface-hub<2.0.0,>=0.33.4->langchain-huggingface) (0.1.2)
Using cached langchain_huggingface-1.2.1-py3-none-any.whl (30 kB)
Using cached tokenizers-0.22.2-cp39-abi3-win_amd64.whl (2.7 MB)
Installing collected packages: tokenizers, langchain-huggingface
Successfully installed langchain-huggingface-1.2.1 tokenizers-0.22.2

[notice] A new release of pip is available: 24.0 -> 26.0.1
[notice] To update, run: python.exe -m pip install --upgrade pip
(myenv) PS E:\Github\nda-generator-mvp\nda-generator-mvp> python -m src.main
============================================================
  NDA GENERATOR MVP
============================================================

📂 Input file: inputs/sample.json

[1/4] Building NDA context from input...
      Parties:          TechCorp Inc. (Disclosing Party) and DataSolutions Ltd. (Rec...
      Purpose:          Evaluating a potential technology partnership for developing...
      Governing Law:    India
      Industry:         Software and Technology
      Duration:         3 years from the date of signing

[2/4] Building LangGraph workflow...
      ✓ Workflow compiled (7 section nodes + merge node)

[3/4] Executing NDA generation pipeline...
      Sections will be generated in parallel.

  → Generating Section 1: Purpose, Parties, and Context
  → Generating Section 2: Definition of Confidential Information
  → Generating Section 3: Categories and Scope of Confidential Information
  → Generating Section 4: Obligations of the Receiving Party
  → Generating Section 5: Permitted Disclosures and Exceptions
  → Generating Section 6: Breach, Remedies, and Liability
  → Generating Section 7: Miscellaneous and General Legal Terms
  ✓ Section 1 saved → E:\Github\nda-generator-mvp\nda-generator-mvp\outputs\drafts\section_1.txt
  ✓ Section 2 saved → E:\Github\nda-generator-mvp\nda-generator-mvp\outputs\drafts\section_2.txt
  ✓ Section 5 saved → E:\Github\nda-generator-mvp\nda-generator-mvp\outputs\drafts\section_5.txt
  ✓ Section 7 saved → E:\Github\nda-generator-mvp\nda-generator-mvp\outputs\drafts\section_7.txt
  ✓ Section 4 saved → E:\Github\nda-generator-mvp\nda-generator-mvp\outputs\drafts\section_4.txt
  ✓ Section 3 saved → E:\Github\nda-generator-mvp\nda-generator-mvp\outputs\drafts\section_3.txt
  ✓ Section 6 saved → E:\Github\nda-generator-mvp\nda-generator-mvp\outputs\drafts\section_6.txt

📋 Sections completed: [1, 2, 3, 4, 5, 6, 7]

📎 Merging all sections into final document...
✅ Final NDA document saved → E:\Github\nda-generator-mvp\nda-generator-mvp\outputs\final\nda_final.txt

[4/4] Pipeline complete.

✅ Final NDA document: E:\Github\nda-generator-mvp\nda-generator-mvp\outputs\final\nda_final.txt

============================================================
  DONE
============================================================

(myenv) PS E:\Github\nda-generator-mvp\nda-generator-mvp> 




(myenv) PS E:\Github\nda-generator-mvp\nda-generator-mvp> python -m src.main --interactive
============================================================
  NDA GENERATOR MVP
============================================================

📂 Input file: None

============================================================
  NDA GENERATOR — Input Collection
============================================================
  Please provide the following details.

  Disclosing Party Name (e.g. TechCorp Inc.): kishore
  Receiving Party Name (e.g. DataSolutions Ltd.): kvell

  Relationship Type:
    [1] Technology Partnership
    [2] Vendor / Supplier
    [3] Employment
    [4] Investor / Funding
    [5] Merger / Acquisition
    [6] Other
  Enter number: 3

  Use today's date as Effective Date? [Y/n]: y

  Purpose of this NDA (describe in 1–2 sentences): kishore is hired at kvell

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
  Industry (e.g. Software and Technology): Software and Technology

------------------------------------------------------------
  ✅ Inputs collected. Summary:
     Parties:       kishore (Disclosing Party) and kvell (Receiving Party)
     Relationship:  Employment
     Purpose:       kishore is hired at kvell
     Info Types:    Technical (source code, algorithms, architecture), Financial (projections, budgets, revenue data), Business (strategies, plans, market research), Customer Data (names, contacts, purchase history), Legal (contracts, IP filings, compliance docs)
     Duration:      3
     Governing Law: India
     Industry:      Software and Technology
------------------------------------------------------------


[2/4] Building LangGraph workflow...
      ✓ Workflow compiled (7 section nodes + merge node)

[3/4] Executing NDA generation pipeline...
      Sections will be generated in parallel.

  → Generating Section 1: Purpose, Parties, and Context
  → Generating Section 2: Definition of Confidential Information
  → Generating Section 3: Categories and Scope of Confidential Information
  → Generating Section 5: Permitted Disclosures and Exceptions
  → Generating Section 4: Obligations of the Receiving Party
  → Generating Section 6: Breach, Remedies, and Liability
  → Generating Section 7: Miscellaneous and General Legal Terms
  ✓ Section 1 saved → E:\Github\nda-generator-mvp\nda-generator-mvp\outputs\drafts\section_1.txt
  ✓ Section 2 saved → E:\Github\nda-generator-mvp\nda-generator-mvp\outputs\drafts\section_2.txt
  ✓ Section 4 saved → E:\Github\nda-generator-mvp\nda-generator-mvp\outputs\drafts\section_4.txt
  ✓ Section 7 saved → E:\Github\nda-generator-mvp\nda-generator-mvp\outputs\drafts\section_7.txt
  ✓ Section 3 saved → E:\Github\nda-generator-mvp\nda-generator-mvp\outputs\drafts\section_3.txt
  ✓ Section 6 saved → E:\Github\nda-generator-mvp\nda-generator-mvp\outputs\drafts\section_6.txt
  ✓ Section 5 saved → E:\Github\nda-generator-mvp\nda-generator-mvp\outputs\drafts\section_5.txt

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