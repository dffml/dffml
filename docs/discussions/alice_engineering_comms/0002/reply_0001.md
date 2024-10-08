# 2022-07-20 Identifying Security Threats WG

- Mike leading
- Marta
  - Office hours
    - Place for Open Source maintainers to be able to ask community of security experts
    - Idea is to run first two sessions in August and September
    - Proposing two different timeslots to cover all geos
    - Question is will be be well staffed for both of those
    - She is collecting feedback right now on possibilities for those dates
    - Pinging folks who have shown interest in the past
    - What format?
      - People just show up and ask
      - Registration with topic they want to talk about
        - Allows us to prepare, consensus is currently we like this
        - Can grab right experts beforehand this way
    - Reaching out to logistics team for how we can communicate
      zoom links, etc.
    - Will test registration beginning of August
    - Will do doodle poll or something for slots
    - Jen is the one for the Zoom setup
    - Amir from ostif.org volunteering to answer questions
    - May want to do a blog in addition to twitter
    - Outreach maybe 4th or 5th, have the twitter points back
      to the blog to capture that.
- Meeting time update
  - We have been doing this at this time for about a year or so
  - We previously alternated between two timeslots for Europe and Asia
  - Should we keep this 10 AM Pacific timeslot?
    - Alternate between US and APAC friendly timezone
  - Most other WGs are morning Pacific time
- Technical Advisory Committee (TAC) update
  - They are tasked with making sure we are delivering on our
    cohesive promise, part of that is visuabliity and transparency
    into the work that we do.
  - We now have a formal reporting process
  - It's not a periodic we're all invited to show up to the TAC meeting
    one slide per project.
     - What we're doing
     - Why we're doing it
  - It's meant as an FYI, we are not asking for approval, we're letting them
    know what we're up to.
  - Everyone who is driving a process or project or thing, please send Mike
    a single slide, what is it, why are we doing it, what the status is,
    what's coming next, and if you need anything
  - Christine on metrics
  - Luigi for SECURITY-INSIGHTS.yml`
  - Mike will send out a template
    - Please fill and respond by Monday
  - Mike says the metrics work should live under a working group, maybe this one, maybe best practices
  - CRob might have an opinion here, as long as work gets done
  - As an org OpenSSF would benefit by being less siloed
  - Question on if we should align to streams?
  - LFX specific definition of metrics in mobilization paper
  - AR for Christine to sync with CRob and see what he thinks.
  - Will raise with TAC next week.
- A few action items for metrics from Christine
  - Working groups are adopting streams from the mobilization plans
- Mike: Alpha Omega
  - A few people were on the public call earlier
  - The recording will be on YouTube
  - Mike will give the fast version of the presentation right now
  - They are still hiring
  - Exploring ways of allocating headcount other than direct hiring
  - If you know anyone or are interested please apply or ping them!
  - Alpha
    - Announced Node, Python, Eclipse
  - Omega
    - Toolchain is pending
    - Waiting for legal approval due to the way the license for CodeQL works
    - Had a CVE in Node that got fixed earlier this month
    - RCE in JSHint that was bitrotted (unused) we removed
    - Two CVEs discloudsed yetserday and two more in the works (couple weeks to release ETA)
    - Found NodeJS vuln via systemcall tracing
      - It tires to query `openssl.cnf` and dumps strace logs to a repo
      - You then have a one stop show of show me every link package of when a binary starts, it does a DNS query
        - John: Sounds aligned with Alice's goals
  - https://sos.dev coming under Alpha-Omega
    - Allows us to compensate dev directly
  - How to participate
    - Improve security tools
    - https://sos.dev
    - Join working groups
    - Get on slack
- Amir: Security Reviews
  - Repo is looking good
  - Updating with four new audits that ostif.org published last week
  - At almost 100 reviews from Mike (Omega work), ostif.org, and community
  - We're gaining traction, getting good stuff in there all the time
  - Might need some help with the automated testing that get's done
    when we upload reviews.
  - Feedback always welcome.
- John: Collection of metric / Alpha-Omega data into shared DB
  - https://github.com/dffml/dffml/tree/main/docs/tutorials/rolling_alice
  - https://datatracker.ietf.org/doc/html/draft-birkholz-scitt-architecture
  - https://www.w3.org/2022/07/pressrelease-did-rec.html.en
  - https://docs.microsoft.com/en-us/azure/confidential-ledger/architecture
  - Mike
    - Mike has been thinking about SCITT as a schema and rules on how one would assert facts, weither it's confidential compute or traditional permissions is impelmenetation details.
    - If metircs runs across you're repo and you have 30 contributors, great
    - As consumer, how can I discover that fact and trust that it's accruate
    - Could immaiget a world where things like Scorecard express the data as as SCITT assursion
    - You go and query that store and you say tell me everythig you know about foo and you get it all back
    - Until we have an implementation with WEb5 that's at at least beta, we could expore what that looks like.
      - John: We can do rekor for now, we'll bridge it all later target 1-2 years out
      - John: We have alignment. Time to execute. rekor + sigstore for metric data atteststation signed with github odic tokens. We care about data provenance. We will later bridge into web5 space used as central points of comms given DID as effectively  the URL or the future. This is in realtion to what we talked to Melvin about with data provenance. We need to start planning how we are going to build up this space now so we can have provenance on thoughts later. This provenance could be for example on inference derived from provenance from training data and model training env and config. This will allow us to ensure the prioritizer make decisions based on Sprit of the law / aka intent based policy derived from Trinity of Static Analysis, Dynamic Analysis, and Human Intent.
        - Living Threat Model threats, mitigations, trust boundaries as initial data set for cross domain conceptual mapping of the the trinity to build pyramid of thought alignment to strategic principles.
        - One of our strategic plans / principles says: "We must be able to trust the sources of all input data used for all model training was done from research studies with these ethical certifications"
          - This allows us to write policies (Open Policy Agent to JSON to DID/VC/SCITT translation/application exploration still in progress) for the organizations we form and apply them as overlays to flows we execute where context appropriate. These overlaid flows define the trusted parties within that context as applicable to the active organizational policies as applicable to the top level system context.
          - The policy associated with the principle that consumes the overlaid trust attestations we will implement and LTM auditor for which checks the SCITT provenance information associated with the operation implementations and the operation implementation network, input network, etc. within the orchestrators trust boundary (TODO need to track usages / `reuse` of contexts `ictx`, `nctx`, etc. with something predeclared, aka at runtime if your `Operation` data structure doesn't allowlist your usage of it you can pass it to a subflow for reuse. This allows us to use the format within our orchrestration and for static analysis because we can use this same format to describe the trust boundry proeprties that other domain sepcific represenatations of architecture have, for instance we could if we were doing and Open Architecture (OA) Intermediate Representation (IR) for and ELF file we might note that the input network context is not reused from the top level system context. Where as if we did an OA IR for Python code we would say that the input network is reused from the top level system context (it has access to that memory region, whereas when you launch and ELF you look access to the parents memory region, typically).
    - Christine
      - Looking at trying to connect all the different data sources
- References
  - [Meeting Notes](https://docs.google.com/document/d/1AfI0S6VjBCO0ZkULCYZGHuzzW8TPqO3zYxRjzmKvUB4/edit?usp=sharing)
  - [GitHub Workgroup Page](https://github.com/ossf/wg-identifying-security-threats)
  - [OpenSSF Slack](https://slack.openssf.org)
  - [Metric Dashboard](https://metrics.openssf.org)
- TODO
  - @pdxjohnny
    - [ ] Reach out to Christine about metrics collaboration
    - [ ] Respond with slides for Mike if he asks