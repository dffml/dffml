## 2023-11-17 Metaschema Language APIs

- https://pages.nist.gov/metaschema/specification/overview/
- Small team committed to support many formats
  - OSCAL, 7 models * 3 different formats
  - > ![image](https://github.com/dffml/dffml/assets/5950433/eec830a8-aa5f-4df3-8421-429823855680)
- Abstract modeling out of schema
- Came out of IETF RFC3344 learnings
- How do we create and information model about how different data relates to each other, pin down semantics, from that produce data models we represent data in
- Key objects, how they relate to each other, abstract objects and how they relate to each other, constraints and rules against objects and combinations of data points that exist between objects used as input to schema generator for XML and JSON schema, Documentation, Code generators for programming language specific parsing code (Java and TypeScript first target), can support conversion from one format to another. With a robust enough format you can support conversion to the common abstract format to any format.
- Has been useful to them and working to better define and operationalize to help make useful to other efforts, looking for more folks to help test and feed requirements
- Some XML, XSLT prototypes, a Java class based implementation
  - https://github.com/usnistgov/metaschema
  - https://github.com/usnistgov/metaschema-xslt
  - https://github.com/usnistgov/metaschema-java
- A.J. Stein: Supply Chain-y things, OSCAL, SCITT, data formatting data wrangling, automation
- Dave Waltermire: OSCAL, Metaschema, supply chain and asset use cases, FedRamp automation
- Wendell Piez: Documentary data publishing systems, Open Source XML XSLT publishing, very interested in applications of metaschema outside security space, digital humanities - digital publishing activities, co-founded journals in digital humanities space
- Nikita Wootten: Working on typescript and tooling, interested on metaschema outside OSCAL
- Dmitry Cousin: Math and AI at NIST, support OSCAL efforts, mainly working on AI, ramping up on metaschema integration and parsing
- Indices and constraints
  - POCs working
  - Ideally looking to apply OSCAL modeling techniques for this to SBOM and VEX with SCITT feeds/subjects
    - https://github.com/usnistgov/OSCAL/blob/1d8a9a01ba89d21973908046532dded85b5944ef/src/metaschema/oscal_ssp_metaschema.xml#L48-L51
    - https://github.com/pdxjohnny/scitt-api-emulator/blob/7ec55acd2b09bb2e08df9c56aa90cfb431aa3fd2/docs/sbom_and_vex.md
    - https://github.com/usnistgov/OSCAL/tree/1d8a9a01ba89d21973908046532dded85b5944ef/src/metaschema
  - https://github.com/usnistgov/metaschema/pull/413
    - Describes approach that is assumed with the OSCAL content
    - Documented use of allowed value constraints in a way that supports existing OSCAL paths
  - https://github.com/usnistgov/metaschema/pull/478
- 7 or 8 different models in OSCAL that represent different security docs
  - System Security Plan, currently XML, but in not so distant future JSON and YAML will be possibilities
  - XML entities are like macros
    - https://github.com/usnistgov/OSCAL/blob/1d8a9a01ba89d21973908046532dded85b5944ef/src/metaschema/oscal_ssp_metaschema.xml#L8-L12
  - Root of the metaschema
    - https://github.com/usnistgov/OSCAL/blob/1d8a9a01ba89d21973908046532dded85b5944ef/src/metaschema/oscal_ssp_metaschema.xml#L13-L26
  - Field vs flag is like element vs attribute
  - Assembly are nodes and translate into objects or arrays in JSON
  - System security plans have repeatable peices of infra we call components
  - Inside an instance of a SSP document there is a section called control implementation, and they can be nested, looks recursively down, by-component is a way inside of the implemented requirement, find a UUID and make sure it exists in another document, that UUID must better exist in an SSP doc, modern XPATH `doc(` says must exist within this doc. When you layer an app on top of CSP, someone has a blessed version of CSP, do they cover threat XYZ which I may have in scoped or out of scoped. If you have one SSP that referes to another SSP, you can look recursivly turtles all the way down. You don't have to look just at SSPs, you can look at multiple document format types. Will look at other SSPs you reference by URLs, implementations will resolve those and look across other document instances. oscal_complete_metadata.xml, if you load things that are not an SSP then it will look in other doc types. Metaschema is the only system that supports this reusablity and sharabilty across implementaions. Dave's implementation does the cross document indexing.
  - Metapath is heavily criping from XPATH, we need a fairly robust pathing langauge to support that, JSONPATH, JSONPOINTER, etc. were all looked at, XPATH was the only thing that provied the robustness needed, but it was tied to an underlying XML data model, recasting XPATH to work on top of the node defintions metaschema uses
  - oscal-cli
  - A.J. live demo
    - ![live-demo-for-the-live-demo-god](https://user-images.githubusercontent.com/5950433/226699339-45b82b38-a7fc-4f2f-a858-e52ee5a6983d.png)
    - ![image](https://github.com/dffml/dffml/assets/5950433/942ecf6b-c263-40ff-a625-bc72d5c60764)
    - ![image](https://github.com/dffml/dffml/assets/5950433/64fc6d0f-f051-4b71-a51a-c7a034cd1c18)
    - ![image](https://github.com/dffml/dffml/assets/5950433/564e3eca-1ede-450b-b76b-605335161607)
    - ![image](https://github.com/dffml/dffml/assets/5950433/edef5bff-9144-40ef-83e0-b040b075ba60)
    - ![image](https://github.com/dffml/dffml/assets/5950433/ebc0c0d0-0695-46d8-841f-6fab2249b906)
      - Codegen of validators, then instantiate to validate
  - metaschema-cli
    - oscal-cli is metaschema-cli with the oscal metaschema embedded
  - Reads metaschema and dynamicly builds a validation environment
  - https://pages.nist.gov/OSCAL/learn/tutorials/
  - OSCAL: Profiling
    - Generates requirements
    - Supported via XPATH in metaschema
- If you can put an URL in there, then the java implementation will resolve it
- Might have to metaschema-ize the data
- CBOR support is on their list
- Goals would be to traverse everything across federated SCITT logs
- CSV, SQL databases, additional format support
- https://gitter.im/usnistgov/OSCAL_metaschema
- https://app.element.io/#/room/#usnistgov-OSCAL_metaschema:gitter.im
- https://matrix.to/#/#usnistgov-OSCAL_metaschema:gitter.im