# Cumulus Geo-processor Test Data Sets
Each acquirable has its own directory with an example file(s) and json configuration file describing the test file(s). pytest fixtures is used to read each configuration json file, aggregate them into a single fixture, and uses them to define testing. There is a one-to-one releation between the processor and testing data.

The tar.gz also containes some helper scripts, `gen_markdown.py` and `tar_test_data.sh`. `gen_markdown.py` is a Python script creating Markdown from each json configuration creating TESTDATA.md. The `shell script tar_test_data.sh` creates cumulus-geoproc-test-data.tar.gz if changes are added for a new release.

To tag a geoproc-test-data release, in the geoproc-test-data repo use these commands: 
`git tag -a 2025-10-31`
`git push origin 2025-10-31`

# Fixture List

See [fixtures](./FIXTURES.md)
