#!/bin/bash

mongoimport -d unipt-stats -c brazil --type tsv --headerline --file userstats-br.csv --upsert --upsertFields uid
mongoimport -d unipt-stats -c portugal --type tsv --headerline --file userstats-pt.csv --upsert --upsertFields uid
