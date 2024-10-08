# Volume 1: Chapter 3: Strategic Principles as Game Plan

We'd like to be able to ask Alice for a rolled up view of how our org
health looks. When we run the following command, we want her to
produce a markdown file, `INNERSOURCE.md`, which describes the health
of the org at the scope desired. By default this is the repo scope,
this would mean the repo and it's dependencies.

Our intent here is to assit developers with organization and prioritization
of their workstreams. Our report generation will be scopable and context
aware. We'll later source data from the knowledge graph (our stream of
consiousness) to enable cached commnuication across agents and procesess.
We want to enable developers to have an at a glance view of the alignment
status of a project or workstreams strategic principles, plans, and values.

At time of writing we do not yet have dependency tree creation flushed
out from ShouldI / CVE Bin Tool / SBOM traversal. We will instead add
an overlay which specifies we should pull repos to report on from the
source which we developed for the InnerSource collector example.

```console
$ alice please contribute report on innersource health
```
- References
  - [Rolling Alice: Coach Alice: Down the Dependency Rabbit Hole Again](../0001_coach_alice/0001_down_the_dependency_rabbit_hole_again.md)
  - [intel/dffml#1287: docs: examples: innersource: Org health and issue prioritization](https://github.com/intel/dffml/issues/1287)
  - [intel/dffml#1315: service: sw: src: change: notify: Service to facilitate poly repo pull model dev tooling](https://github.com/intel/dffml/issues/1315#issuecomment-1066814280)
    - [Rolling Alice: Architecting Alice: Stream of Consciousness](../0000_architecting_alice/0005_stream_of_consciousness.md)

The following is an example report

---

# InnerSource Org Health

Overall maps to our general Good/Bad for a train of thought.

`"Minimum health or above"` if `has_readme and has_contributing`

```mermaid
pie title Overall
    "Minimum health or above" : 100
    "Less than minimum health" : 100
```

Show dataflow of only connections to the overall calculation.

```mermaid
graph LR
    overall[Overall]
    has_readme[Has Readme]
    has_code_of_conduct[Has Code of Conduct]
    has_security[Has Security]
    has_contributing[Has Contributing]
    has_license[Has License]

    has_readme --> overall
    has_code_of_conduct --> overall
    has_security --> overall
    has_contributing --> overall
    has_license --> overall
```

<details>
<summary>Links to Repo Metric Visualizations</summary>

| Repo                           | Report URL                                         |
|--------------------------------|----------------------------------------------------|
| https://github.com/dffml/dffml | https://chadig.com/did/repo/github.com/dffml/dffml |
| https://github.com/dffml/dffml | https://nahdig.com/did/repo/github.com/dffml/dffml |

</details>
