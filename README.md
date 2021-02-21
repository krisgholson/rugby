# rugby

## deploy

one-time setup for domain
```bash
sls create_domain --stage prod --aws-profile lowcountry_rugby
```

```bash
sls client deploy --stage prod --aws-profile lowcountry_rugby
sls deploy --stage prod --aws-profile lowcountry_rugby
```