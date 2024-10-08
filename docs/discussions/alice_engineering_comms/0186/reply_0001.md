## 2023-02-22 CVE Bin Tool Monthly Meeting

- Anthony and John
- Different SBOMs for different versions of python
- CycloneDX progressing more smoothly than SPDX
- CVEs are component level, VEX is a product level
- VEX is negative, prove that it's not right
- VDR and VEX need to be combined in some way
- The triage process is critical
- We can get a list of products that don't have vulns
- In your context of your product, is it vuln? IT depends on the deployment context, what's the environment
- When you do a scan can you give a indication about where it's deployed? Threat model
  - Internal or public network
    - If public then threat model attack surface is bigger
- VEX doesn't address vuln chaining
- Threat model
  - Architecture
    - VEX/VDR, does this effect this component within the architecture?
    - You need the call graphs, chaining, coverage
- Meta analysis of OSS usage of libraries to understand what the call graphs are
- https://github.com/dffml/dffml/blob/main/docs/tutorials/rolling_alice/0001_coach_alice/0001_down_the_dependency_rabbit_hole_again.md#plan
  - Talked about CVE Bin Tool triage process
- Input validation on trust boundries
  - What is I/O for top level system context?
    - https://intel.github.io/dffml/main/concepts/dataflow.html#benefits-of-dataflows security
- Some consumers understand that suppliers make assumptions that aren't valid in downstream environments
  - End users only interested in their N-1 supplier, their direct supplier
  - How can we aggregate the information down the chain
- Medical having to look heavily at this, different SBOMs for different consumers
  - Wanting to provide minimal info
    - Could consumer provide threat model?
      - https://github.com/johnlwhiteman/living-threat-models
      - [WIP: IETF SCITT: Use Case: OpenSSF Metrics: activitypub extensions for security.txt](https://github.com/ietf-scitt/use-cases/blob/bcecb48ddebf8d08dd10b24b8061deb46491d0c5/openssf_metrics.md#activitypub-extensions-for-securitytxt)
- TODO
  - [ ] https://github.com/anthonyharrison?tab=repositories
  - [ ] Check out FOSDEM talks, Siemens SBOMs for vuln management
  - [ ] Check out Anthony's SBOM audit
    - Checks for valid license, up to date versions, etc.
  - [ ] Meet next week