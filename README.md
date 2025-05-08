# SELF-referencIng Embedded Strings

String representation of small molecules that is more robust than SMILES, since, by design, all SELFIES strings are valid molecules. It is particularly helpful when applied in generative models, as all the SELFIES proposed are valid molecules. The authors also found that on generative models, SELFIES produces more diverse molecules than compared to SMILES.

This model was incorporated on 2022-07-14.

## Information
### Identifiers
- **Ersilia Identifier:** `eos6pbf`
- **Slug:** `selfies`

### Domain
- **Task:** `Representation`
- **Subtask:** `Featurization`
- **Biomedical Area:** `Any`
- **Target Organism:** `Not Applicable`
- **Tags:** `Chemical notation`, `Chemical language model`, `Compound generation`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1`
- **Output Consistency:** `Fixed`
- **Interpretation:** String representation of a molecule (SELFIE)

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| selfies | string |  | SELFIES representation of the input molecule |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos6pbf](https://hub.docker.com/r/ersiliaos/eos6pbf)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos6pbf.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos6pbf.zip)

### Resource Consumption
- **Model Size (Mb):** `1`
- **Environment Size (Mb):** `245`
- **Image Size (Mb):** `207.27`

**Computational Performance (seconds):**
- 10 inputs: `28.86`
- 100 inputs: `18.72`
- 10000 inputs: `181.43`

### References
- **Source Code**: [https://github.com/aspuru-guzik-group/selfies](https://github.com/aspuru-guzik-group/selfies)
- **Publication**: [https://pubs.rsc.org/en/content/articlehtml/2023/dd/d3dd00044c](https://pubs.rsc.org/en/content/articlehtml/2023/dd/d3dd00044c)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2023`
- **Ersilia Contributor:** [brosular](https://github.com/brosular)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [Apache-2.0](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos6pbf
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos6pbf
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
