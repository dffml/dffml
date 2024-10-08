## 2023-03-15 @pdxjohnny Engineering Logs

- https://github.com/scitt-community/scitt-api-emulator/issues/20#issuecomment-1470278224
  - Here is an example of using a file (workflow) as a payload: https://github.com/dffml/dffml/blob/main/docs/tutorials/rolling_alice/0000_architecting_alice/0002_shes_ariving_when.md#scitt-api-emulator-spin-up
- https://github.com/w3c/vc-jwt/pull/61
- https://github.com/oauth-wg/oauth-selective-disclosure-jwt
- https://github.com/credential-handler/credential-handler-polyfill#demo
  - Summary of end-to-end demo of secure build to boot to usage
    - We'll want `did:keri` support for the end-to-end flow where we have software built within a TEE with KERI tied to the TEE's hardware root of trust.
    - We'll export SCITT to a flat file format, we'll send it to the browser
    - The browser will be able to auth to the software stack by pulling down the git repos involved and matching up the transparency service receipts/records with the git repos.
      - Fully isolated (SLSA4+) setup
        - This cuts out like, most of the way everything is done today in software.
  - https://github.com/credential-handler/authn.io
  - https://wallet.example.chapi.io/
  - https://issuer.example.chapi.io/
  - https://verifier.example.chapi.io/
  - https://github.com/TBD54566975/dwn-sdk-js
  - https://github.com/TBD54566975/ssi-sdk-wasm
  - https://github.com/TBD54566975/web5-js
  - https://github.com/TBD54566975/web5-wallet-browser
- https://github.com/TBD54566975/ftl/pull/3#issue-1623361276
  - This looks like they are building distributed compute
- https://github.com/ggerganov/llama.cpp
- https://github.com/exaloop/codon
- [RFCv3.2: IETF SCITT: Use Case: OpenSSF Metrics: activitypub extensions for security.txt](https://github.com/ietf-scitt/use-cases/blob/da838e39cac8f5e2a444e7ac1d3c723e8ddd49ed/openssf_metrics.md#openssf-metrics)
- TODO
  - [ ] Add `FROM scratch` image examples
    - [ ] Add schema to output for the flow based on `Definition`s at `/schema.json`
      - Use `@context` with zeroith index pointing to a manifest ADR schema
        - Example: https://github.com/dffml/dffml/blob/main/schema/github/actions/build/images/containers/0.0.0.schema.json
  - [ ] Find Source URL -> CVE mapping code as example of depth of field mapping in action
    - https://github.com/pdxjohnny/dffml/branches
  - [x] docs: tutorials: rolling alice: coach alice: down: the dependency rabbit hole again: plan: Threat model generation based on SBOM
    - https://github.com/dffml/dffml/blob/main/docs/tutorials/rolling_alice/0001_coach_alice/0001_down_the_dependency_rabbit_hole_again.md
    - https://github.com/dffml/dffml/commit/02502ff3be0118a19ef83fbc71f17fd9403cb26a
    - @Cat-Katze Just FYI, this tutorial, which is meant to be the creation of a basic/high-level threat model from a Software Bill Of Materials, is closely related to the https://github.com/intel/cve-bin-tool/issues/2639 activity. We'll eventually use the threat model plus the triage mechanism together as we preform automated vuln analysis.
      - For more background, the https://github.com/ietf-scitt/use-cases/issues/14 is about how we can have the transparency service, which will be the source of truth for "is CVE-XYZ a vuln that affects product ABC" can interact with CI/CD systems to trigger auto triage per federated CI/CD eventing: https://codeberg.org/forgejo-contrib/discussions/issues/12. Since Open Source Software projects have different threat models based on how they might be deployed, each project will get an event, "new vuln!" when there is a new vuln. The downstream projects (projects which use a project, for example: dffml-model-tensorflow is downstream of DFFML) will get notifications of new vulns, the hope is we can bake in a pattern of analysis which can be followed as vulns cascade downstream for analysis / remediation within different contexts per their usage.
      - [2023-03-02 SBOM, VEX, VDR, Threat Modeling, Open Architecture](https://github.com/intel/dffml/discussions/1406?sort=new#discussioncomment-5179079)
        - https://tomalrichblog.blogspot.com/2023/02/is-vulnerability-exploitable-when-its.html