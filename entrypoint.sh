#!/bin/bash

prisma db push --force-reset --accept-data-loss

python run.py