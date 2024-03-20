#!/bin/bash

prisma migrate dev

prisma generate

python run.py