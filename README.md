# SELF-referencIng Embedded Strings

Converts a molecule into SELFIES, a string representation in which every possible sequence corresponds to a valid molecule. Krenn and colleagues designed the grammar so that generative models cannot emit invalid structures, removing a persistent failure mode of SMILES-based generation where ring closures and valences go unsatisfied. The transformation is deterministic and reversible, changing only how the molecule is written rather than anything about the molecule itself.

This model was incorporated on 2022-07-14.Last packaged on 2026-03-20.

## Information
### Identifiers
- **Ersilia Identifier:** `eos6pbf`
- **Slug:** `selfies`

### Domain
- **Task:** `Representation`
- **Subtask:** `Featurization`
- **Biomedical Area:** `Any`
- **Target Organism:** `Any`
- **Tags:** `Chemical notation`, `Chemical language model`, `Compound generation`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1`
- **Output Consistency:** `Fixed`
- **Interpretation:** SELFIES string encoding the input molecule in a fully robust syntax.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| selfies | string |  | SELFIES representation of the input molecule |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos6pbf](https://hub.docker.com/r/ersiliaos/eos6pbf)
- **Docker Architecture:** `AMD64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos6pbf.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos6pbf.zip)

### Resource Consumption
- **Model Size (Mb):** `1`
- **Environment Size (Mb):** `309`
- **Image Size (Mb):** `290.95`

**Computational Performance (seconds):**
- 10 inputs: `39.91`
- 100 inputs: `22.74`
- 10000 inputs: `32.23`

### References
- **Source Code**: [https://github.com/aspuru-guzik-group/selfies](https://github.com/aspuru-guzik-group/selfies)
- **Publication**: [https://doi.org/10.1039/D3DD00044C](https://doi.org/10.1039/D3DD00044C)
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
