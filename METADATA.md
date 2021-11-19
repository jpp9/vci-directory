# Issuer Metadata

[vci-issuer-metadata.json](vci-issuers-metadata.json) represents metadata about an Issuer that may be useful to applications and websites.

| Attribute | Meaning |
|-----------|---------|
| `canonical_iss` | The matches the `iss` or `canonical_iss` of the issuer in `vci-issuers.json` |
| `website` | A website where the consumer can get their SMART Health Card or learn where they can get their SMART Health Card |
| `help_line` | A phone number a consumer can call for assistance |
| `issuer_type` | The type of issuer |
| `state` | Which state, province, territory, or other administrative division within a country the issuer represents |
| `country` | The country the issuer represents as ISO 3166 2 or 3 letter code |

[example-metadata.json](example-metadata.json) shows basic example representing what an entry in the metadata file would look like.
