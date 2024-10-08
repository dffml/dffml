## 2023-01-24 @pdxjohnny Engineering Logs

- https://github.com/carzum/termviz
- https://github.com/Byron/gitoxide
  - Commitment to vendoring, rust (safer and faster) implementation of git
- https://github.com/neondatabase/neon#running-local-installation
  - Serverless (cattle based) postgres
- https://github.com/zurawiki/gptcommit
  - AI generated commit messages (nice)
- https://github.com/launchbadge/sqlx
- https://github.com/njsmith/posy
  - For bootstrapping landed on Eden nodes
- https://www.datasciencecentral.com/preconditions-for-decoupled-and-decentralized-data-centric-systems/
  - > “APIs have proven quite useful, but require developers to learn aspects of each API owner’s data model and quirks of each API, one by one. Decoupling in a broader, more complete sense implies more of an automated, any-to-any, plug-and-play capability. That’s where digital twins and agents enter the picture"
  - > “With such a method, the twins are documented in ways that APIs and relational databases are not. RDF (standard triple semantic graph) enables a self-describing graph in a uniform format–what Wharton calls a “lingua franca”. You can do things like share a bundle of 20 triples in this environment, and they can be plug and play with the entity you’re sharing with.”
  - > “That’s a little bit of ad-hoc contextized data sharing that could make all the difference between reusable and single purpose. In that sense, there’s enough intelligence at the node and in each agent to interact in a loosely coupled, less centrally controlled way. That means easier scaling and fewer headaches from trying to grow and manage a large system.“
  - EdenCI (Extensible Dynamic Edge Network Collective Intelligence)
  - Digital Twin (see last weekends GPT2 outputs, LOL)
  - Manifest ADRs and schema
- Yup, Deep Learning Meets Sparse Regularization: A Signal Processing Perspective
  - ref: redpill
- https://twitter.com/TheSeaMouse/status/1617973204445982721
  - How to query PDFs with GPT
- https://mailarchive.ietf.org/arch/msg/scitt/NQ9lYhrxUf5FFEYXBVNpF1diM64/
  - > he eNotary part of SCITT thus replaces a timestamp with a "receipt", which can be refreshed and always time valid.  Meaning that there is no need to support the extension case to solve the problem.   This could be adopted by SigStore as well (thus why the push to standardize) and means that the "originating" signature form can be short lived or not and validation is based on the policy of the eNotary.
- https://github.com/kubernetes/sig-security/issues/new/choose
  - https://lwkd.info/2023/20230124
  - https://github.com/kubernetes/kubernetes/pull/115246/files#diff-149dfe7bb29d1191dceae3a52915e750e64b7f87257a5fb309c29d3056e2a95d
- https://myst-parser.readthedocs.io/en/latest/docutils.html
- https://myst-parser.readthedocs.io/en/latest/syntax/roles-and-directives.html
- https://myst-parser.readthedocs.io/en/latest/faq/index.html#include-markdown-files-into-an-rst-file
- Everything as a container build
  - FROM rebuild chains
    - VEX NVDStyle
  - Everything as a melange build
    - #1426
- What are we doing, why are we doing it, where does it help us go?
- Vol 3: https://web.archive.org/web/20130721011202/http://agile2003.agilealliance.org/files/R1Paper.pdf
- https://github.com/google-research/tuning_playbook
- https://github.com/jerryjliu/gpt_index/tree/main/gpt_index/indices/tree
- https://github.com/jerryjliu/gpt_index/blob/main/examples/gatsby/TestGatsby.ipynb
- https://github.com/jerryjliu/gpt_index/blob/main/examples/data_connectors/MongoDemo.ipynb
  - https://github.com/jerryjliu/gpt_index/blob/a796f1e50ba60e47ccb35c9d9d6d85d54ab696bf/gpt_index/readers/mongo.py#L58
  - https://github.com/jerryjliu/gpt_index/blob/3cf19e1e69c49b1aca243c01a515c410927709b5/docs/how_to/data_connectors.md
- https://github.com/brycedrennan/imaginAIry
- https://github.com/mage-ai/mage-ai
- `Rolling Alice: Coach Alice: Versioning Learning`
  - https://github.com/dffml/dffml/blob/main/docs/arch/0010-schema.rst
  - *For continuous improvement*
    - Related
      - https://github.com/lysander07/Presentations/raw/main/EGC2023_Symbolic%20and%20Subsymbolic%20AI%20%20-%20an%20Epic%20Dilemma.pdf
  - Target data model is generated from manifest schema
  - Given an `OperationImplementation` output of target manifest data model type
    - On dataflow operation input dependency tree changes (before: Down the Dependency Rabbit Hold Again, before: Cartographer Extraordinaire) update `/schema/*` via `datamodel-code-gen.py`
      - If code or tree changes, bump minor
        - Can always manually rename and commit file to dot
      - If input tree changes, bump major
      - Pre-commit hook / CI Job to validate