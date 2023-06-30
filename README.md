# SELF-referencIng Embedded Strings

String representation of small molecules that is more robust than SMILES, since, by design, all SELFIES strings are valid molecules. It is particularly helpful when applied in generative models, as all the SELFIES proposed are valid molecules. The authors also found that on generative models, SELFIES produces more diverse molecules than compared to SMILES.

## Identifiers

* EOS model ID: `eos6pbf`
* Slug: `selfies`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Representation`
* Output: `Compound`
* Output Type: `String`
* Output Shape: `Single`
* Interpretation: String representation of a molecule (SELFIE)

## References

* [Publication](https://arxiv.org/pdf/1905.13741)
* [Source Code](https://github.com/aspuru-guzik-group/selfies)
* Ersilia contributor: [brosular](https://github.com/brosular)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos6pbf)
* [AWS S3](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos6pbf.zip)
* [DockerHub](https://hub.docker.com/r/ersiliaos/eos6pbf) (AMD64)

## Citation

If you use this model, please cite the [original authors](https://arxiv.org/pdf/1905.13741) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a Apache-2.0 license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!