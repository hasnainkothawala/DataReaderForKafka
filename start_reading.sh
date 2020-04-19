#!/bin/bash

cd /opt/gen_logs
lib/DataframeToJsonReader.py > logs/credit_card_access.log &
exit 0